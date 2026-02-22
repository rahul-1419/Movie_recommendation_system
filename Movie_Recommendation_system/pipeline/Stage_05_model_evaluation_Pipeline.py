from Movie_Recommendation_system.components.model_evaluation import ModelEvaluation
from Movie_Recommendation_system.configuration.configuration import ConfigurationManager
from Movie_Recommendation_system import logger
from pathlib import Path

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_eval_config = config.get_model_evaluation_config()

            model_evaluation = ModelEvaluation(model_eval_config)
            model_evaluation.evaluate_model()

        except Exception as e:
            raise e
