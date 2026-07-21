from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from google import genai
import requests

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    word: str
    sentence: str



@app.get("/word")
async def word_d(query: str):
    dictionary = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{query}")
    if dictionary.status_code != 200:
        return {"message": "Word not found"}
    if("example" in dictionary.json()[0]["meanings"][0]["definitions"][0]):
        return {"Definition": dictionary.json()[0]["meanings"][0]["definitions"][0]["definition"], "Example": dictionary.json()[0]["meanings"][0]["definitions"][0]["example"]}
    else:
        return {"Definition": dictionary.json()[0]["meanings"][0]["definitions"][0]["definition"], "Example": "No example for this word"}

@app.post("/check-sentence")
async def ex_check(item: Item):
    interaction = client.interactions.create(
        model = "gemini-3.5-flash",
        input = f"The word is {item.word}. The user wrote: {item.sentence}. Is this correct usage? Explain simply."
        )
    print(interaction.output_text)
    return {"feedback": interaction.output_text}


