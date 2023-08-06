from typing import List


class EvaluationState:
    QUEUED = 'queued'
    RUNNING = 'running'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'
    VALID_STATES = [QUEUED, RUNNING, SUCCEEDED, FAILED]


class EvaluationParameters:
    def __init__(self, test_dataset_names: List[str]) -> None:
        assert test_dataset_names

        self.test_dataset_names = test_dataset_names

        self._params = {
            'TestDatasetNames': self.test_dataset_names,
        }

    @property
    def params(self) -> dict:
        return self._params


class Evaluation:
    def __init__(self, name, model_name, dataset_name) -> None:
        assert name
        assert model_name
        assert dataset_name

        self.name = name
        self.model_name = model_name
        self.eval_params = EvaluationParameters([dataset_name])

    @property
    def params(self) -> dict:
        return {'EvaluationParameters': self.eval_params.params}


class EvaluationResponse(Evaluation):
    def __init__(
            self, name: str, model_name: str, evaluationParams: EvaluationParameters, state: str, created_date_time: str,
            last_modified_date_time: str, model_performance: dict, error_code: str) -> None:
        super().__init__(name, model_name, evaluationParams['testDatasetNames'][0])
        self.state = state
        self.created_date_time = created_date_time
        self.last_modified_date_time = last_modified_date_time
        self.model_performance = model_performance
        self.error_code = error_code

    @staticmethod
    def from_response(json):
        print(json)
        return EvaluationResponse(
            json['name'],
            json['modelName'],
            json['evaluationParameters'],
            json['state'],
            json['createdDateTime'],
            json['lastModifiedDateTime'],
            json.get('modelPerformance'),
            json.get('error_code'))
