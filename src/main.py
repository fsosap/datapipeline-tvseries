import requests     as req
import json         as json
import user_interaction     as user


def get_tvseries_from_date(date:str):
    api_params = {"date":date}
    api_response = req.get(url="https://api.tvmaze.com/schedule/web", params=api_params)

    return json.loads(api_response.content)


if __name__ == "__main__":
    user.main()
