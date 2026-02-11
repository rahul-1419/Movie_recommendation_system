from Movie_Recommendation_system.components.model_building import ModelTrainer
from Movie_Recommendation_system.configuration.configuration import ConfigurationManager
from Movie_Recommendation_system import logger
from pathlib import Path

STAGE_NAME = "Model Building stage"

class ModelBuildingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()

            model_trainer_config = ModelTrainer(config = model_trainer_config)
            model_trainer_config.build_model()

        except Exception as e:
            raise e
