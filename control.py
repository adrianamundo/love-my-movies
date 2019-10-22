from flask import Flask, jsonify, render_template, request
from flask_caching import Cache
import os, optparse, sys
import json
import requests
from tmdbv3api import TMDb
from tmdbv3api import Movie

app = Flask(__name__)

environment=os.getenv("ENVIRONMENT","development")
info = {}
tmdb = TMDb()
tmdb.api_key = '9083cbdd7f380052de7a54baf7d4983b'

movie = Movie()
popular = movie.popular()

for p in popular:
    title = str(p.title)
    release = str(p.release_date)
    popularity = str(p.popularity)

    #print(len(p.title))
    #print(len(p.release_date))
    #print(p.popularity)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

filename = os.path.join(app.static_folder, 'jsons', 'trending_movies.json')
with open(filename) as test_file:
    data = json.load(test_file)

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
