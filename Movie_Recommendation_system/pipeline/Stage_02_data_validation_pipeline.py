from Movie_Recommendation_system.components.data_validation import DataValidation
from Movie_Recommendation_system.configuration.configuration import ConfigurationManager
from Movie_Recommendation_system import logger


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        validation_status = data_validation.validate_all_columns()
