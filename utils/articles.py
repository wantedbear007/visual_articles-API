from scraper import ScrapData

class Articles():

    def all_articles(page = 1, category = ""):
        """Enter page number to fetch"""
        
        if (category !=  ""):
            endpoint = f"{'/' + category}/?page={page}"
        else:
            endpoint =  f"/?page={page}"
        final_data = []
        id = 0;

        try:
            site_content = ScrapData.scrap(endpoint)
            parent_container = site_content.find("div", class_="gallery-wrapper")
            containers = parent_container.find_all("div", class_='gallery-cell')

            for container in containers:
                body_link = container.find("a")
                date = container.find("span")
                img_url = container.find("img")

                data_lst = {
                    "id": id,
                    "title": body_link["title"],
                    "link": body_link["href"],
                    "date": date.text,
                    "image_url": img_url["data-src"]
                }

                final_data.append(data_lst)
                id+=1

            return final_data                


        except Exception as e:
            return e
            



print(Articles.all_articles(page = 1, category = "technology"))