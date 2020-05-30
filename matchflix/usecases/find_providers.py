import requests
import urllib.parse
from pprint import pprint


def find_providers(title, tmdb_id):
    query = urllib.parse.quote(title)
    url = f"https://apis.justwatch.com/content/titles/pt_BR/popular?body=%7B%22page_size%22:5,%22page%22:1,%22query%22:%22{query}%22,%22content_types%22:[%22movie%22]%7D"
    result = requests.get(url).json()

    for item in result["items"]:
        for score in item["scoring"]:
            if score["provider_type"] == "tmdb:id" and str(score["value"]) == str(
                tmdb_id
            ):
                urls = set()
                for offer in item["offers"]:
                    urls.add(offer["urls"]["standard_web"].split("?")[0])
                return urls
