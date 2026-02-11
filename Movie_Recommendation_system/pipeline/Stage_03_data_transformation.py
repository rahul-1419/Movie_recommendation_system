from Movie_Recommendation_system.components.data_transformation import DataTransformation
from Movie_Recommendation_system.configuration.configuration import ConfigurationManager
from Movie_Recommendation_system import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.transform_data()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)