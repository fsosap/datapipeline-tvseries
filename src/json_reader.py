import json as json
import pandas as pd
from pandas import json_normalize

def json_to_dataframe(json_instance:json) -> pd.DataFrame:
    return json_normalize(json_instance)

def read_json_from_path(file_path:str) -> json:
    with open(file= file_path, mode="r") as fp:
        json_instance = json.load(fp)
    
    fp.close()
    return json_instance