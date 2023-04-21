from movie_scraper import MovieScraper
from movie_writer import MovieWriter

def main():
    # ejecuta el programa dandole el url y ejecutando primero la obtencion de la data y luego el guardarla en el archivo csv

    # Downloading imdb top 250 movie's data
    url = 'http://www.imdb.com/chart/top'

    scraper = MovieScraper(url)
    scraper.scrape_movies()

    writer = MovieWriter("movie_results.csv")
    writer.write_to_csv(scraper.movies)

if __name__ == '__main__':
    main()
