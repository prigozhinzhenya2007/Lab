#http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel, Field, validator
import pyjokes
import wikipedia

wikipedia.set_lang("ru")

app = FastAPI()

class JokeInput(BaseModel):
    friend: str = Field(..., min_length=3, description="Имя друга (минимум 3 символа)")

class Joke(BaseModel):
    friend: str
    joke: str

class WikiInput(BaseModel):
    title: str = Field(..., min_length=1)

@app.get("/", status_code=status.HTTP_200_OK)
def get_joke():
    return {"joke": pyjokes.get_joke()}

@app.get("/{friend}", status_code=status.HTTP_200_OK)
def friends_joke(friend: str):
    return {"message": f"{friend} tells his joke: {pyjokes.get_joke()}"}

@app.get("/multi/{friend}", status_code=status.HTTP_200_OK)
def multi_friends_joke(friend: str, jokes_number: int = Query(..., gt=0, le=10)):
    jokes = [pyjokes.get_joke() for _ in range(jokes_number)]
    return {"friend": friend, "jokes": jokes}

@app.post("/", response_model=Joke, status_code=status.HTTP_201_CREATED)
def create_joke(joke_input: JokeInput):
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())

@app.get("/wiki/path/{title}", status_code=status.HTTP_200_OK)
def get_wiki_path(title: str):
    try:
        summary = wikipedia.summary(title, sentences=2)
        return {"title": title, "summary": summary}
    except wikipedia.exceptions.DisambiguationError:
        raise HTTPException(status_code=400, detail="Ambiguous title")
    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail="Page not found")

@app.get("/wiki/query", status_code=status.HTTP_200_OK)
def get_wiki_query(title: str):
    try:
        summary = wikipedia.summary(title, sentences=2)
        return {"title": title, "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/wiki/body", status_code=status.HTTP_200_OK)
def get_wiki_body(data: WikiInput):
    try:
        summary = wikipedia.summary(data.title, sentences=2)
        return {"title": data.title, "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
