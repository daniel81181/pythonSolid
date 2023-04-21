
# Es creada una clase movie para guardar los datos de cada pelicula y use para guardar la info de estas
class Movie:
    def __init__(self, movie_title, year, place, star_cast, rating, vote, link, preference_key):
        self.movie_title = movie_title
        self.year = year
        self.place = place
        self.star_cast = star_cast
        self.rating = rating
        self.vote = vote
        self.link = link
        self.preference_key = preference_key