# -*- coding: utf-8 -*-
from flask import Flask, jsonify, json
import requests

app = Flask(__name__)

from functions import extract_word

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

	#keywords, articles = extract_keywords(content["articles"])

	extract_word(content["articles"])

	test = content["articles"][0]

	return content

@app.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(debug=True)