import requests     as req
import json         as json
import session      as session


def get_tvseries_from_date(date:str):
    api_params = {"date":date}
    api_response = req.get(url="https://api.tvmaze.com/schedule/web", params=api_params)

    return json.loads(api_response.content)


if __name__ == "__main__":
    daterange = session.daterange()
    print(f"Data extraction will be performed for the data range: {str(daterange.start_date)} to {str(daterange.end_date)}")
    session.set_date_range(daterange)