import os
from Movie_Recommendation_system import logger
import pandas as pd
from Movie_Recommendation_system.entity.config_entity import DataValidationConfig
from pathlib import Path

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            schema = self.config.all_schema
            unzip_dir = self.config.unzip_data_dir

            for dataset_name, dataset_schema in schema.items():
                file_path = file_path = Path(unzip_dir) / dataset_schema["file_name"]

                print(f"\n Validating dataset: {dataset_name}")
                print(f"File path: {file_path}")

                # File existence
                if not file_path.exists():
                    print("File does NOT exist")
                    validation_status = False
                    break

                data = pd.read_csv(file_path)
                data_columns = set(data.columns)

                expected_columns = set(dataset_schema["columns"].keys())

                print("Expected columns:", expected_columns)
                print("Actual columns:", data_columns)

                missing_cols = expected_columns - data_columns
                if missing_cols:
                    print("Missing columns:", missing_cols)
                    validation_status = False
                    break
                else:
                    print("All columns matched")

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
