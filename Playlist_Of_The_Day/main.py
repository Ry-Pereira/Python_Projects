import datetime

from billboard_100_songs_requests import get_billboard_top_100
from billboard_100_songs_scraper import BillboardTop100SongsScraper



def main():
    billboard_top_100_songs = get_billboard_top_100(datetime.date.today().strftime("%Y-%m-%d"))
    billboard_top_100_song_scraper = BillboardTop100SongsScraper(billboard_top_100_songs)


    







if __name__ == "__main__":
    main()