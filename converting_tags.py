import re

class TagConverter():
    def __init__(self, text):
        self.text = text

    def strip_tags(self, marker=""):
        re_tags = re.compile(r"<([^>]+)>", re.UNICODE)
        text_re_tags = re_tags.sub(marker, self.text)

        with open(f"subtotal.txt", "w", encoding = "utf-8") as f_w:
            f_w.write(text_re_tags)

        with open(f"subtotal.txt", "r", encoding = "utf-8") as f_r:
            my_list = f_r.readlines()
            string = ""

            for item in my_list:
                spaces_score = 0
                for i in item:
                    if i == " ":
                        spaces_score = spaces_score + 1
                
                if spaces_score != (len(item) - 1):
                    words = item.split(' ')
                    
                    for word in words:
                        if word != "":
                            string = string + word
                            if word != words[len(words)-1]:
                                string = string + " "
                
            return string



        #with open(f"html_articles\{name_file}.txt", "r", encoding = "utf-8") as f:
        #        obj_tag_converter = TagConverter(f.read())
        #print(' '.join([ t for t in  text_re_tags.split(' ') if t ]))
        #return re.sub(r'\s+', ' ', text_re_tags)
        #return re_tags.sub(marker, self.text)