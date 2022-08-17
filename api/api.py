from fastapi import FastAPI
from utils.articles import Articles

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/articles/{category}/{page_no}")
async def get_articles(category: str, page_no: int):
    return  Articles.all_articles(page=page_no, category = category)

@app.get("/api/story/")
async def get_story(endpoint: str):
    return Articles.articles_body(endpoint=endpoint)


# http://127.0.0.1:8000/api/story/?endpoint=/sports/zimbabwe-tour-5-indians-to-watch-out-for-9571-17-08-2022

