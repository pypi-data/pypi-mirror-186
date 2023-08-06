import requests
import time
import logging

from .client import Client
from ..models import Model, ModelResponse, ModelState


class TrainingClient(Client):
    def __init__(self, resource_type, resource_name: str, multi_service_endpoint, resource_key: str) -> None:
        super().__init__(resource_type, resource_name, multi_service_endpoint, resource_key)
        self._endpoint = f'{self._endpoint}/models/'

    def train_model(self, model: Model) -> ModelResponse:
        r = self._request_wrapper(lambda: requests.put(self._endpoint + model.name, json=model.params, timeout=self.TIMEOUT_SEC, headers=self.headers))
        return ModelResponse.from_response(r.json())

    def query_model(self, name) -> ModelResponse:
        r = self._request_wrapper(lambda: requests.get(self._endpoint + name, timeout=self.TIMEOUT_SEC, headers=self.headers))
        return ModelResponse.from_response(r.json())

    def cancel_model_training(self, name):
        self._request_wrapper(lambda: requests.post(self._endpoint + name + "/:cancel", timeout=self.TIMEOUT_SEC, headers=self.headers))

    def delete_model(self, name):
        self._request_wrapper(lambda: requests.delete(self._endpoint + name, timeout=self.TIMEOUT_SEC, headers=self.headers))

    def wait_for_completion(self, model_name, check_wait_in_secs: int) -> ModelResponse:
        total_elapsed = 0
        state = None
        while state not in [ModelState.FAILED, ModelState.SUCCEEDED]:
            model = self.query_model(model_name)
            state = model.state
            time.sleep(check_wait_in_secs)
            total_elapsed += check_wait_in_secs
            logging.info(f'Training {model_name} for {total_elapsed} seconds. State {state}.')

        model = self.query_model(model_name)
        logging.info(f'Training finished with state {model.state}.')

        if model.state == ModelState.FAILED:
            logging.warning(f'Failure code: {model.failure_error_code}, {model.error_message}.')
        else:
            logging.info(f'Wall-clock time {total_elapsed / 60} minutes, actual training compute time billed {model.training_cost_in_minutes} minutes.')
            logging.info(f'Model performance: {model.model_performance}')

        return model
