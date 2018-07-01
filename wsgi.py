import os

#print(os.environ['MONGODB_CONNECTION_STRING'])

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()