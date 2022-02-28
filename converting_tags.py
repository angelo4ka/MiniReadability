from bs4 import BeautifulSoup
import re
import os

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

class TagConverter():
    def __init__(self, text):
        self.text = text

    def tag_processing(self):
        contents = self.text
        soup = BeautifulSoup(contents, "lxml")

        tags = soup.find_all([text_tags_list, head_tag_list])
        
        # Сбрасываем текст
        self.text = ""

        # Индекс тега
        index_tag = 0
        # Индекс основного тега для извлечения текста
        index_mtt = 0
        for tag in tags:
            if tag.name in head_tag_list:
                self.text = self.text + " ".join(tag.text.split()) + "\n\n"
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

                    self.text = self.text + " ".join(tag_text.split()) + "\n\n"
                    index_mtt = index_mtt + 1
                else:
                    if tag.findParent().name not in main_text_tag:
                        self.text = self.text + " ".join(tag.text.split()) + "\n\n"
            
            index_tag = index_tag + 1
    
    def text_formatting(self):
        new_text = ""
        for paragraph in self.text.split("\n"):
            if paragraph == "":
                new_text = new_text + "\n"
            
            letter_count = 0 
            word_list = []
            
            for word in paragraph.split():
                if letter_count + len(word) + 1 <= strings_characters:
                    word_list.append(word)
                    letter_count += len(word) + 1 
                else:
                    new_text = new_text + " ".join(word_list) + "\n" 
                    word_list = [word]
                    letter_count = len(word)
            
            if (len(word_list)):
                new_text = new_text + " ".join(word_list) + "\n"
        
        self.text = new_text

    def save_text(self, url, marker=""):
        # Обрабатываем url
        re_url = re.compile(r"https?://(www\.)?")        
        name_file = re_url.sub(marker, url).strip().strip('/')

        # Формируем путь
        directories = name_file.split("/")
        if not os.path.isdir("txt_articles"):
            os.mkdir("txt_articles")
        os.chdir("txt_articles")
        index_dir = 0

        for directory in directories:
            if index_dir != (len(directories) - 1):
                if not os.path.isdir(directory):
                    os.mkdir(f"{directory}")

                os.chdir(f"{directory}")
                index_dir = index_dir + 1
            else:
                with open(f"{directory}.txt", "w", encoding = "utf-8") as f:
                        f.write(self.text)
                        
                        # Возвращаемся в начальную директорию
                        while index_dir >= 0:
                            os.chdir("..")
                            index_dir = index_dir - 1