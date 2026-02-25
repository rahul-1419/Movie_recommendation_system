from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load data once at startup
movies = pd.read_csv("artifacts/data_transformation/merged_tmdb.csv")

movies["title_lower"] = movies["title"].str.lower()

with open("artifacts/model_build/similarity.pkl", "rb") as f:
    similarity = pickle.load(f)


def recommend(movie_name):
    movie_name = movie_name.lower().strip()

    matches = movies[movies["title_lower"].str.contains(movie_name)]

    if matches.empty:
        return []

    index = matches.index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = [movies.iloc[i[0]].title for i in movie_list]
    return recommendations


@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        movie_name = request.form["movie"]
        recommendations = recommend(movie_name)

    return render_template("index.html", recommendations=recommendations)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)