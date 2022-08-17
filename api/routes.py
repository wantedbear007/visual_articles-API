from ast import Num
from fastapi import APIRouter
from utils.articles import *

router = APIRouter()
articles = Articles()

@router.get("/stories/{category}/{page_no}")
async def get_stories(page_no: Num, category: str):
    return articles.all_articles(page_no, category)

    
