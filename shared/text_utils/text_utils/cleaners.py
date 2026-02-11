from bs4 import BeautifulSoup
import re

HTML_ENTITY_PATTERN = re.compile(r"&\w+;")

def clean_html(text):
    if not isinstance(text, str) or not text:
        return ""
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    text = HTML_ENTITY_PATTERN.sub("", text)
    return text
