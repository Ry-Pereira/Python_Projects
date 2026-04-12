import datetime

from billboard_100_songs_scraper import scrape_billboard_top_100_songs



def main():
    billboard_top_100_songs = scrape_billboard_top_100_songs(datetime.date.today().strftime("%Y-%m-%d"))





if __name__ == "__main__":
    main()