import logging
import requests
import time

from .client import Client
from ..models import EvaluationResponse, Evaluation, EvaluationState


class EvaluationClient(Client):
    def __init__(self, resource_type, resource_name: str, multi_service_endpoint, resource_key: str) -> None:
        super().__init__(resource_type, resource_name, multi_service_endpoint, resource_key)
        self._endpoint_format_str = self._endpoint + '/models/{0}/evaluations/{1}'

    def evaluate(self, evaluation: Evaluation) -> EvaluationResponse:
        r = self._request_wrapper(lambda: requests.put(self._endpoint_format_str.format(evaluation.model_name, evaluation.name),
                                  json=evaluation.params, timeout=self.TIMEOUT_SEC, headers=self.headers))
        return EvaluationResponse.from_response(r.json())

    def query_run(self, name, model_name) -> EvaluationResponse:
        r = self._request_wrapper(lambda: requests.get(self._endpoint_format_str.format(model_name, name), timeout=self.TIMEOUT_SEC, headers=self.headers))
        return EvaluationResponse.from_response(r.json())

    def wait_for_completion(self, name: str, model_name: str, check_wait_in_secs: int) -> EvaluationResponse:
        total_elapsed = 0
        state = None
        while state not in [EvaluationState.FAILED, EvaluationState.SUCCEEDED]:
            eval_run = self.query_model(name, model_name)
            state = eval_run.state
            time.sleep(check_wait_in_secs)
            total_elapsed += check_wait_in_secs
            logging.info(f'Training {name} for {total_elapsed} seconds. State {state}.')

        eval_run = self.query_model(name, model_name)
        logging.info(f'Training finished with state {eval_run.state}.')

        if eval_run.state == EvaluationState.FAILED:
            logging.warning(f'Failure code: {eval_run.error_code}.')
        else:
            logging.info(f'Wall-clock time {total_elapsed / 60} minutes.')
            logging.info(f'Model performance: {eval_run.model_performance}')

        return eval_run
