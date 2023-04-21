import requests
import re
from bs4 import BeautifulSoup
from movie import Movie

# La siguinete clase se encarga de obtener la info de la url dada, usando la biblioteca beautiful soup
# una vez obtenida se guarda como data con el formato de la clase Movie
class MovieScraper:
    def __init__(self, url):
        self.url = url
        self.movies = []

    def scrape_movies(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')

        movie_elements = soup.select('td.titleColumn')
        links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

        for index in range(0, len(movie_elements)):
            movie_string = movie_elements[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index)) + 1:-7]
            year = re.search('\((.*?)\)', movie_string).group(1)
            place = movie[:len(str(index)) - (len(movie))]

            data = {"movie_title": movie_title,
                    "year": year,
                    "place": place,
                    "star_cast": crew[index],
                    "rating": ratings[index],
                    "vote": votes[index],
                    "link": links[index],
                    "preference_key": index % 4 + 1}
            self.movies.append(Movie(**data))
