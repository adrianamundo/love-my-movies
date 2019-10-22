from flask import Flask, jsonify, render_template, request
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

@app.route("/")
def about():
    return render_template("index.html", info=info)


if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    #print("Local change")
    app.run(host="0.0.0.0",debug=debug)
