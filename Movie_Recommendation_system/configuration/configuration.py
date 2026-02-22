from Movie_Recommendation_system.constants import *
from Movie_Recommendation_system.utils.common import read_yaml, create_directories
from Movie_Recommendation_system.entity.config_entity import (DataIngestionConfig, DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        # Load FULL schema (important for multi-dataset)
        schema = self.schema

        create_directories([Path(config.root_dir)])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            movies_data_path = config.movies_data_path,
            credits_data_path = config.credits_data_path,
            transformed_data_path = config.transformed_data_path
        )

        return data_transformation_config
    

    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer

        create_directories([Path(config.root_dir)])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            transformed_data_path=config.transformed_data_path,
            vectorizer_path=config.vectorizer_path,
            similarity_path=config.similarity_path,
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([Path(config.root_dir)])

        return ModelEvaluationConfig(
            root_dir=Path(config.root_dir),
            transformed_data_path=Path(config.transformed_data_path),
            similarity_path=Path(config.similarity_path),
        )