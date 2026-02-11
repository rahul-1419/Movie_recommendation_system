import os
from Movie_Recommendation_system import logger
from Movie_Recommendation_system.entity.config_entity import DataTransformationConfig
import pandas as pd
import ast


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # 🔹 helper: extract names from JSON-like string
    def _convert(self, obj):
        try:
            return [i["name"] for i in ast.literal_eval(obj)]
        except Exception:
            return []

    # 🔹 helper: extract director name
    def _fetch_director(self, obj):
        try:
            for i in ast.literal_eval(obj):
                if i.get("job") == "Director":
                    return i.get("name")
        except Exception:
            pass
        return ""

    def transform_data(self):
        # 1️⃣ load datasets
        movies = pd.read_csv(self.config.movies_data_path)
        credits = pd.read_csv(self.config.credits_data_path)

        credits = credits.drop(columns=["title"])

        logger.info('Dataset Loaded.....')

        # 2️⃣ merge (correct stage)
        movies = movies.merge(
            credits,
            left_on="id",
            right_on="movie_id"
        )

        logger.info('Merge two files......')

        # 3️⃣ select required columns
        movies = movies[
            ["id", "title", "overview", "genres", "keywords", "cast", "crew"]
        ]

        logger.info('selected columns....')

        # 4️⃣ drop missing rows
        movies.dropna(inplace=True)

        # 5️⃣ feature extraction
        movies["genres"] = movies["genres"].apply(self._convert)
        movies["keywords"] = movies["keywords"].apply(self._convert)
        movies["cast"] = movies["cast"].apply(lambda x: self._convert(x)[:3])
        movies["director"] = movies["crew"].apply(self._fetch_director)

        logger.info('Feature Extraction Done....')

        # 6️⃣ create tags column
        movies["tags"] = (
            movies["overview"]
            + " "
            + movies["genres"].apply(lambda x: " ".join(x))
            + " "
            + movies["keywords"].apply(lambda x: " ".join(x))
            + " "
            + movies["cast"].apply(lambda x: " ".join(x))
            + " "
            + movies["director"]
        )

        logger.info('Create tags Columns')

        # 7️⃣ final clean
        movies["tags"] = movies["tags"].str.lower()
        final_df = movies[["id", "title", "tags"]]

        # 8️⃣ save transformed data
        final_df.to_csv(
            self.config.transformed_data_path,
            index=False
        )

        logger.info('Save transformed Data in Artifacts')
        print(final_df.head())