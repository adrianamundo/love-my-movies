from flask import Flask, jsonify, render_template, request
from flask_caching import Cache
import os, optparse, sys
import json
import requests
from tmdbv3api import TMDb
from tmdbv3api import Movie
from redis import Redis

app = Flask(__name__)

environment=os.getenv("ENVIRONMENT","development")

tmdb = TMDb()
tmdb.api_key = '9083cbdd7f380052de7a54baf7d4983b'

response = requests.get('https://api.themoviedb.org/3/trending/movie/week?api_key=9083cbdd7f380052de7a54baf7d4983b')
data = response.json()
with open('Trending_Movies_API.json', 'w', encoding= 'utf-8') as f:
    json.dump(data, f, ensure_ascii= False, indent=4)

class db:
    key = "9083cbdd7f380052de7a54baf7d4983b"
    redisserver = NONE
    environment = ""

    def __init__(self, key, environment):
        self.key = key
        self.environment = environment
    
    def redisinit(self):
        movie = Movie()
        if self.environment == "development":
            self.environment = "localhost"
        
        self.redisserver = redis.StrictRedis(host= self.environment, port=6379, db=0)
        apisource = TMDb()
        apisource.key = self.key
        self.Popularmovies(movie)

        def Popularmovies(self,movie):
            popular = movie.popular()
            self.saveMovie(popular)
        
        def saveMovie(self, moviesbyeone):
            with self.redisserver.pipeline() as pipe:
                for moviesbyone in moviesbyeone:
                    pipe.hset(moviesbyeone.title, "title", moviesbyeone.title)
                    pipe.hset(moviesbyone.title, "release_date", moviesbyeone.title)
                    pipe.hset(moviesbyone.title, "popularity", moviesbyeone.title)
                    pipe.execute()

database = database(key, environment)
database.redisinit()
redisserver=database.redisserver





cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app)



@app.route("/")
@cache.cached(timeout= 50)
def about():
    return render_template("index.html", data=data)


if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    #print("Local change")
    app.run(host="0.0.0.0",debug=debug)
