import pandas   as pd
import json     as json
import os
import json_reader as reader

class Master_dataframe():
    def __init__(self):
        self.df = pd.DataFrame()

    def agg_to_master_df(self, incoming_df:pd.DataFrame):
        self.df = pd.concat([self.df, incoming_df], ignore_index=True, sort=False)
    
    # def extract_custom_df(self, column_name:str):
    #     custom_df = self.df[column_name]



def clean_df(incoming_df: pd.DataFrame) -> pd.DataFrame:
    # drop empty columns
    cleaned_df = incoming_df.dropna(axis=1, how="all")
    # cast ended column
    cleaned_df["_embedded.show.ended"] = cleaned_df["_embedded.show.ended"].astype('datetime64[ns]')
    # drop excluded columns based on human criteria
    COLS_TO_DROP = ['_embedded.show.externals.tvrage', '_embedded.show.externals.thetvdb', '_embedded.show.externals.imdb',\
                 '_embedded.show.image.medium', '_embedded.show.image.original', 'image.medium', 'image.original',\
                 '_embedded.show._links.previousepisode.href', '_embedded.show._links.nextepisode.href']

    cleaned_df.drop(COLS_TO_DROP, axis=1, inplace=True)
    
    return cleaned_df


def integrate_dfs() -> pd.DataFrame:
    json_file_path = "json/"
    file_list = os.listdir(json_file_path)

    master = Master_dataframe()

    for json_file in file_list:
        data = reader.read_json_from_path(f"json/{json_file}")
        incoming_df = reader.json_to_dataframe(data)
        
        cleaned_df = clean_df(incoming_df)

        master.agg_to_master_df(cleaned_df)

        return master.df