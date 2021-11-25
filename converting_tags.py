import re
# NameError: name 'self' is not defined

class TagConverter():
    def IsMultiLineTag(text):
        opened_tag = False
        closed_tag = False

        if text[0] == "<":
            opened_tag = True

        for i in text(0, len(text) - 1):
            if text[i] == ">":
                closed_tag = True
        
        return opened_tag, closed_tag

    def strip_tags(text, marker=""):
        re_tags = re.compile(r"<([^>]+)>", re.UNICODE)

        opened_tag, closed_tag = self.IsMultiLineTag(text)
        if ((not closed_tag) and opened_tag) or ((not opened_tag) and closed_tag):
            text = ""

        return re_tags.sub(marker, text)