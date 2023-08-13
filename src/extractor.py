import requests     as request
import json         as json

def get_tvseries_from_date(date:str) -> json:
    api_params = {"date":date}
    api_response = request.get(url="https://api.tvmaze.com/schedule/web", params=api_params)

    return json.loads(api_response.content)