from bs4 import BeautifulSoup
import re

class TagConverter():
    def __init__(self, text):
        self.text = text

    def tag_processing(self, marker=""):
        # Список тегов, из которых будет извлекаться текст.
        text_tags_list = ["p", "a", "span", "b", "i", "u"]
        # Основной тег для извлечения текста
        main_text_tag = ["p"]
        # Основной тег для извлечения ссылки
        main_link_tag = ["a"]
        # Список тегов, из которых будут извлекаться заголовки.
        head_tag_list = ["h1", "h2", "h3", "h4"]
        # Количество символов в строке
        strings_characters = 80
        
        contents = self.text
        soup = BeautifulSoup(contents, "lxml")

        tags = soup.find_all([text_tags_list, head_tag_list])
        
        index_tag = 0
        # Индекс основного тега для извлечения текста
        index_mtt = 0
        for tag in tags:
            if tag.name in head_tag_list:
                print(" ".join(tag.text.split())) # Временно
                print("") # Временно
            elif tag.name in main_text_tag:
                if tag.text != "":
                    tag_text = tag.text
                    root = soup.find_all(main_text_tag)
                    root_childs = [e.name for e in root[index_mtt].children if e.name is not None]
                    
                    if len(root_childs) > 0:
                        # Индекс вложенного тега
                        subtag_index = index_tag + 1
                        
                        for child in root_childs:
                            if child in main_link_tag:
                                # Ссылка разбивается на 2 части: текст и URL-ссылки
                                part_1 = tags[subtag_index].text
                                part_2 = tags[subtag_index].get("href")
                                text_link = f"{part_1} [{part_2}]"

                                tag_text = tag_text.replace(f"{part_1}", f"{text_link}")
                            
                            subtag_index = subtag_index + 1

                    print(" ".join(tag_text.split())) # Временно
                    print("") # Временно
                    index_mtt = index_mtt + 1
                else:
                    if tag.findParent().name not in main_text_tag:
                        print(" ".join(tag.text.split())) # Временно
            
            index_tag = index_tag + 1