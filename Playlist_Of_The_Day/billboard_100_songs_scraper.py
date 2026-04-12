





import html

from bs4 import BeautifulSoup

class BillboardTop100SongsScraper:
    def __init__(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        self.songs = soup.select("h3")






