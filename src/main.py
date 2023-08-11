import requests     as req
import json         as json
from datetime import date, timedelta


def get_tvseries_from_date(date:str):
    api_params = {"date":date}
    api_response = req.get(url="https://api.tvmaze.com/schedule/web", params=api_params)

    return json.loads(api_response.content)


if __name__ == "__main__":
    date_init = date(2022,12,1)
    date_end = date(2022,12,31)

    print(get_tvseries_from_date(str(date_init)))
    # main()