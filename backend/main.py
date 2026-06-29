from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"message" : "FastAPI is working"}


@app.get("/word")
async def word_d(query: str):
    return {"word":"Lethargic", "definition":"experiencing a state of sluggishness, profound weariness, and a lack of mental alertness or energy", "example":"I feel lethergic if I sleep during the day"}
