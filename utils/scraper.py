
from bs4 import BeautifulSoup
from requests import get

class ScrapData():
    def scrap(endpoint = "/?page=2"):
        """Enter endpoint of website to scrap data"""
        base_url = f"https://www.indiatoday.in/visualstories{endpoint}"
        headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

        
        try:
            site = get(base_url, headers=headers)
            page_connect = BeautifulSoup(site.content, "html.parser")
            return page_connect

        except Exception as e:
            return e

