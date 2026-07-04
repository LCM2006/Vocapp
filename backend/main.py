from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

words = {
    "Ephemeral" : {
        "Definition" : "Lasting for a very short time; fleeting or transient.",
        "Example" : "The beautiful colors of the sunset were ephemeral, fading into darkness within minutes."},
    "Adept" : {
        "Definition" : "Highly skilled or proficient at something.",
        "Example" : "She is highly adept at coding and can solve complex software bugs in seconds."},
    "Dwindle" : {
        "Definition" : "To gradually diminish in size, amount, or strength.",
        "Example" : "Our water supplies began to dwindle as the hot summer days dragged on."},
    "Mitigate" : {
        "Definition": "To make something less severe, harmful, or painful.",
        "Example" : "Planting more trees helps to mitigate the effects of climate change by absorbing carbon dioxide."},
    "Ambiguous" : {
        "Definition" : "Open to more than one interpretation; having a double meaning.",
        "Example" : "The instructions were ambiguous, leaving the team confused about what to do next."}
}

class Item(BaseModel):
    word: str
    sentence: str

@app.get("/")
async def root():
    return{"message" : "FastAPI is working"}


@app.get("/word")
async def word_d(query: str):
    if (words.get(query.capitalize()) == None):
        return{"message" : "Word not found in dictionary"}
    else:
        return words.get(query.capitalize())

@app.post("/check-sentence")
async def ex_check(item: Item):
    return {"feedback": "AI feedback coming soon"}
