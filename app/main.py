from fastapi import FastAPI

from app.recommender import get_recommendations

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Movie Recommender API is running"}

@app.get("/recommend/{movie_name}")
def recommend(movie_name: str):
    recs = get_recommendations(movie_name)
    return {"recommendations": recs.tolist()}