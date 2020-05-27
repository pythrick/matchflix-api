import csv

import dataset

db = dataset.connect("sqlite:///db.sqlite")
table = db["releases"]


with open("catalog.csv") as f:
    reader = csv.reader(f)

    for row in reader:
        movie = {
            "id": row[0],
            "category": row[1],
            "title": row[2],
            "director": row[3],
            "cast": row[4],
            "country": row[5],
            "date_added": row[6],
            "release_year": row[7],
            "maturity": row[8],
            "duration": row[9],
            "genre": row[10],
            "description": row[11],
            # default poster just so we see something
            "image": "https://live.staticflickr.com/4422/36193190861_93b15edb32_z.jpg",
            "imdb": "Not Available",
        }

        table.insert(movie)
        print(movie)
