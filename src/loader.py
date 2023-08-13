import extractor    as ext
import pandas       as pd
import json         as json


from datetime import date

def load_raw_data_for_timerange(start_date:date, end_date:date):

    date_list = pd.date_range(start = start_date, end = end_date, freq='D')

    for date_instance in date_list:
        date_instance = date_instance.date()
        # extract raw
        api_response = ext.get_tvseries_from_date(date_instance)
        print(f"Geting tv shows from {str(date_instance)} was successful!")
        # load raw
        write_response_into_file(api_response, date_instance)
        print(f"Writting tv shows from {str(date_instance)} was successful!")

def write_response_into_file(response:json, file_name:str):
    with open(file=f"json/{file_name}.json", mode="w") as fp:
        json.dump(response, fp)
    
    fp.close()