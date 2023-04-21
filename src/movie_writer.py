import csv
from movie import Movie

#Se encarga de acomodar todos los datos que se obtuvieron de las peliculas en el archivo csv
class MovieWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_csv(self, movies):
        fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
        with open(self.file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for movie in movies:
                writer.writerow({field: getattr(movie, field) for field in fields})
