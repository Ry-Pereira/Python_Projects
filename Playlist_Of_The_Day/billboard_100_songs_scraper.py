



import requests

import html

from bs4 import BeautifulSoup

class BillboardTop100SongsScraper:
    def __init__(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        self.title = soup.find("h1").text.strip()[0:-1]
        self.songs = soup.find_all("h3",class_="c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max")
        self.artists = soup.find_all("span",class_="c-label a-no-trucate a-font-secondary u-font-size-15 u-font-size-13@mobile-max u-line-height-18px@mobile-max u-letter-spacing-0010 u-line-height-21px a-children-link-color-black a-children-link-color-brand-secondary:hover lrv-a-children-link-decoration-underline:hover lrv-u-display-block a-truncate-ellipsis-2line u-max-width-397 u-max-width-230@tablet-only u-max-width-300@mobile-max")





test = BillboardTop100SongsScraper(requests.get("https://www.billboard.com/charts/hot-100", headers={"User-Agent": "Mozilla/5.0"}).text)
print(test.title)

print("Artists:\n")

num = 0

for artist in test.artists:
    num+=1
    print(num, artist.text.strip())

num = 0
for song in test.songs:
    num+=1
    print(num, song.text.strip())
num = 0

while num < 100:

    print(num + 1, test.artists[num].text.strip(), " - ", test.songs[num].text.strip())
    num+=1