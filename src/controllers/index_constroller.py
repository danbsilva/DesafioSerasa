import requests
from flask import jsonify
from src.extensions.cache import cache


@cache.cached(timeout=10, query_string=True)
def index():
    API_URL = "http://universities.hipolabs.com/search?country="
    r = requests.get(f"{API_URL}")
    return jsonify(r.json())
