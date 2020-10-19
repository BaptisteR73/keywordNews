# -*- coding: Utf-8 -*-
from flask import Flask, jsonify, json, render_template
from collections import OrderedDict
import requests

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # Pour éviter que Flask réordonne notre dictionnaire par ordre alphabétique

from functions import extractWords

NEWS_API_KEY = "3ddb16b4b9cc4349bee1349bfbea326b"

if NEWS_API_KEY is None:
	exit()
else:
	NEWS_API_URL = "http://newsapi.org/v2/top-headlines?country=fr&apiKey="+NEWS_API_KEY

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/news/")
def get_news():

	response = requests.get(NEWS_API_URL)
	content  =json.loads(response.content.decode('utf-8'))

	keywords = extractWords(content["articles"])

	return jsonify({
        'status'   : 'ok',
        'data'     :{
            'keywords' : keywords # On retourne uniquement les 100 premiers mots
        }
    })

@app.route('/dashboard/')
def dashboard():
    return render_template('main.html')

@app.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(debug=True)