import random

from flask import Flask
from flask_cors import cross_origin

words = { "clean", "frost", "taste", "grape", "crate"}

api = Flask(__name__)

@api.route('/randomword', methods=['GET'])
@cross_origin(origins=["http://localhost:8080", "http://10.0.0.18:8080"])
def get_random_word():
  return random.choice(tuple(words))

if __name__ == '__main__':
    api.run() 