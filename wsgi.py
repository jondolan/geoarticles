import os
#print(os.environ['MONGODB_CONNECTION_STRING'])
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import pprint

application = Flask(__name__)
client = MongoClient(os.environ['MONGODB_CONNECTION_STRING'])
# client = MongoClient('localhost', 27017)
articles_db = client.articles
syriahr = articles_db.syriahr

@application.route("/")
def homepage():
    return render_template('homepage.html')

@application.route('/search', methods = ['POST'])
def search():
    global syriahr
    if request.method == 'POST':
        value = request.form['query']
        results = syriahr.find({"$text": {"$search": value}})
        i = 0
        rtn = {}
        for result in results:
            rtn[str(i)] = result
            i+=1
        # print(rtn)
        # print(jsonify(rtn))
        return jsonify(rtn)

@application.route('/article', methods = ['GET'])
def display():
    _id = request.args.get('id')
    _query = request.args.get('query')
    print("ID:")
    print(_id)
    result = syriahr.find_one({"_id": _id})
    print(result)
    return render_template('display_article.html', title=result['title'], date=result['date'], body=result['body'], url=result['url'], query=_query)


if __name__ == "__main__":
    application.run()