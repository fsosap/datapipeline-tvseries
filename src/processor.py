import pandas   as pd
import json     as json
import os
import json_operations as json_ops
import file_handler as hndl

class Master_dataframe():
    def __init__(self):
        self.df = pd.DataFrame()

    def agg_to_master_df(self, incoming_df: pd.DataFrame):
        self.df = pd.concat([self.df, incoming_df], ignore_index=True, sort=False)
    
    def post_clean(self):
        # drop empty columns
        self.df.dropna(axis=1, how="all", inplace=True)
        # drop columns with a considerable presence of NaN
        total_rows = len(self.df.index)
        for column in self.df.columns:
            if self.df[column].isna().sum()/total_rows > 0.98:
                self.df.drop(column, axis=1)


def clean_df(incoming_df: pd.DataFrame) -> pd.DataFrame:
    # cast 'ended' column
    incoming_df["_embedded.show.ended"] = incoming_df["_embedded.show.ended"].astype('datetime64[ns]')
    # drop excluded columns based on human criteria
    COLS_TO_DROP = ['_embedded.show.externals.tvrage', '_embedded.show.externals.thetvdb', '_embedded.show.externals.imdb',\
                 '_embedded.show.image.medium', '_embedded.show.image.original', 'image.medium', 'image.original',\
                 '_embedded.show._links.previousepisode.href', '_embedded.show._links.nextepisode.href']
    incoming_df_cols = incoming_df.columns
    for col in COLS_TO_DROP:
        if col not in incoming_df_cols:
            COLS_TO_DROP.remove(col)

    cleaned_df = incoming_df.drop(incoming_df.loc[:, COLS_TO_DROP], axis=1, errors='ignore')
    
    return cleaned_df


def integrate_dfs() -> pd.DataFrame:
    json_file_path = "json/"
    file_list = os.listdir(json_file_path)
    file_list = hndl.clean_file_list(file_list,'.json')

    master = Master_dataframe()

    for json_file in file_list:
        if json_file:
            data = json_ops.read_json_from_path(f"json/{json_file}")
            incoming_df = json_ops.json_to_dataframe(data)
            cleaned_df = clean_df(incoming_df)
            master.agg_to_master_df(cleaned_df)

    master.post_clean()
    print("Successful dataset integration!\n","#rows:",len(master.df.index),"#cols:",len(master.df.columns))
    return master.df