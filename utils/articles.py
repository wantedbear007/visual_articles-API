from utils.scraper import ScrapData
# from scraper import ScrapData

class Articles():

    # Extracting articles from home page
    def all_articles(page = 1, category = "sports"):
        """Enter page number to fetch"""

        if (category != ""):
            if (category == "all"):
                endpoint = f"/?page={page}"
            else:
                endpoint = f"{'/' + category}/?page={page}"

        else:
            endpoint =  f"/?page={page}"

        # dev settings
        # final_data = {"category": category, "endpoint": endpoint, "data": []}
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
                # final_data["data"].append(data_lst)
                final_data.append(data_lst)
                id+=1

            return final_data                


        except Exception as e:
            return e

    
    # Extracting articles details date
    def articles_body(endpoint = "/sports/asia-cup-most-successful-wicketkeepers-9523-15-08-2022"):
        """provide article endpoint to get data"""

        all_stories = []
        id = 0

        try:
            site_content = ScrapData.scrap(endpoint=endpoint)
            containers = site_content.find_all("amp-story-page")

            for container in containers:
                try:
                    image = container.find("amp-img")
                    desc = container.find("p").text

                except:
                    pass
                
                if (image != None and desc != None):

                    story  = {
                        "id" : id,
                        "title": desc,
                        "img": image["src"]
                    }
                    id += 1
                    all_stories.append(story)

            return all_stories[1:]


        except Exception as e:
            return e


            

# print(Articles.all_articles())



    
            



# print(Articles.articles_body("/sports/zimbabwe-tour-5-indians-to-watch-out-for-9571-17-08-2022"))