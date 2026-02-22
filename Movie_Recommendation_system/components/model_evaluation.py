import pandas as pd
import pickle
from pathlib import Path
from Movie_Recommendation_system.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_model(self):
        movies = pd.read_csv(self.config.transformed_data_path)

        with open(self.config.similarity_path, "rb") as f:
            similarity = pickle.load(f)

        test_movies = ["Avatar", "Batman Begins", "Titanic"]

        print("\n🔎 Model Evaluation Results:\n")

        for movie_name in test_movies:
            if movie_name not in movies["title"].values:
                print(f"{movie_name} not found")
                continue

            index = movies[movies["title"] == movie_name].index[0]
            distances = similarity[index]

            movie_list = sorted(
                list(enumerate(distances)),
                reverse=True,
                key=lambda x: x[1]
            )[1:6]

            print(f"\nTop recommendations for {movie_name}:")

            for i in movie_list:
                print("  -", movies.iloc[i[0]].title)