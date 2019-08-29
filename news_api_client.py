#!/usr/bin/env python

from flask import Flask, request
import requests
from news import News
import json
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Index!"


@app.route("/recentNews", methods=['GET', 'POST'])
def recent_news():
    if request.method == 'GET':
        return "Get not supported"
    if request.method == 'POST':
        title_json = request.get_json()
        title = title_json.get('title', '')
        print(getsNewsBasedOnTitle(title))
        json_str = json.dumps([e.to_json() for e in getsNewsBasedOnTitle(title)])
        return json_str


def getsNewsBasedOnTitle(user_input_title):
    main_url = "https://newsapi.org/v2/everything?q="+user_input_title+"&from="+get_two_weeks_ago_date()+"&sortBy=publishedAt&apiKey="
    open_page = requests.get(main_url).json()
    article = open_page["articles"]
    results = []

    for ar in article:
        results.append(News(ar["title"], ar["source"]["name"], ar["author"], ar["description"], ar["url"],
                            ar["urlToImage"], ar["publishedAt"], ar["content"]))

    return results


def get_two_weeks_ago_date():
    today_date = datetime.today()
    two_weeks_ago = today_date - timedelta(days=14)
    return str(two_weeks_ago.date())


if __name__ == '__main__':
    app.run()

