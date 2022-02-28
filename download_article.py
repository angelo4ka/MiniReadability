from requests import request
import re, requests
import os

class Website():
    def __init__(self, url):
        self.url = url

    def file_name_generation(self):
        response = requests.get(self.url)
        title = re.findall(r"\"(?:http[s]?://)([^:/\s\"]+)/?[^\"]*\"", response.text)
        title = title[len(title) - 1].replace(".", "_")

        return title

    def get_content_from_url(self):
        title = self.file_name_generation()
        
        # Создаём директорию, если её нет и переходим в неё
        if not os.path.isdir("html_articles"):
            os.mkdir("html_articles")
        os.chdir("html_articles")

        r = request("GET", f"{self.url}").text
        with open(f"{title}.txt", "w", encoding = "utf-8") as f:
            f.write(r)

        # Возвращаемся в первоначальную директорию
        os.chdir("..")