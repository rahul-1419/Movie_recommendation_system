import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Movie_Recommendation_system import logger
from Movie_Recommendation_system.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def build_model(self):
        # Load transformed data
        movies = pd.read_csv(self.config.transformed_data_path)

        logger.info('Load Transformed data')

        # Vectorize tags
        cv = CountVectorizer(max_features=5000, stop_words="english")
        vectors = cv.fit_transform(movies["tags"]).toarray()

        # Compute cosine similarity
        similarity = cosine_similarity(vectors)

        logger.info('Compute cosine similarity')

        # Save vectorizer
        with open(self.config.vectorizer_path, "wb") as f:
            pickle.dump(cv, f)

        logger.info('Save Vectorizer')

        # Save similarity matrix
        with open(self.config.similarity_path, "wb") as f:
            pickle.dump(similarity, f)

        logger.info('Save similarity matrix')

        print("✅ Model build completed successfully")
