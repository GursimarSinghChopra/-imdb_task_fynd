import json

from imdb_app.models import Movie, Genre


def add_product():
    f = open('/home/chopra/Desktop/personal_project/imdb_task/imdb_task/imdb.json')
    data = json.load(f)

    for i in data:
        movie_obj = Movie.objects.create(name=i['name'], director=i['director'], score=i['imdb_score'], popularity=i['99popularity'])

        for genre in i['genre']:
            Genre.objects.create(name=genre, movie=movie_obj)
        print(i)

    f.close()
