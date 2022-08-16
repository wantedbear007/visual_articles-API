
from bs4 import BeautifulSoup
from requests import get

class ScrapData():
    def scrap(endpoint = "/?page=2"):
        """Enter endpoint of website to scrap data"""
        base_url = f"https://www.indiatoday.in/visualstories{endpoint}"
        
        try:
            site = get(base_url)
            page_connect = BeautifulSoup(site.content, "html.parser")
            return page_connect

        except Exception as e:
            return e

