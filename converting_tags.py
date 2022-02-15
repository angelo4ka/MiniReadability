import re

class TagConverter():
    def __init__(self, text):
        self.text = text

    def strip_tags(self, marker=""):
        re_tags = re.compile(r"<([^>]+)>", re.UNICODE)

        return re_tags.sub(marker, self.text)