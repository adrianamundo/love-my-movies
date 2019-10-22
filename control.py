from flask import Flask, jsonify, render_template, request
import yaml, os 
app = Flask(__name__)

environment=os.getenv("ENVIRONMENT","development")
info = {}

@app.route("/")
def about():
    return render_template("index.html", info=info)


if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    #print("Local change")
    app.run(host="0.0.0.0",debug=debug)
