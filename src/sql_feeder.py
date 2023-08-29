import pandas as pd
import loader as loader
import file_handler as hndl
import db_operations as db_ops
import os

SCHEMA = \
    {
        "Episode":
        
        {
            'id':'id', 
            'url':'url', 
            'name':'name', 
            'season':'season', 
            'number':'number', 
            'type':'type', 
            'airdate':'airdate', 
            'airtime':'airtime',
            'airstamp':'airstamp', 
            'runtime':'runtime', 
            'summary':'summary', 
            'rating.average':'ratingAverage',
            '_embedded.show.id':'show_id'
        }
        ,"Show":
        {
            '_embedded.show.id':'id', 
            '_embedded.show.url':'url',
            '_embedded.show.name':'name', 
            '_embedded.show.type':'type', 
            '_embedded.show.language':'language',
            '_embedded.show.status':'status',
            '_embedded.show.runtime':'runtime', 
            '_embedded.show.averageRuntime':'averageRuntime',
            '_embedded.show.premiered':'premiered', 
            '_embedded.show.ended':'ended',
            '_embedded.show.officialSite':'officialSite', 
            '_embedded.show.rating.average':'ratingAverage',
            '_embedded.show.weight':'weight', 
            '_embedded.show.summary':'summary',
            '_embedded.show.updated':'updated',
            '_embedded.show.webChannel.id':'webChannel_id',
            '_embedded.show.network.id':'network_id'
        }
        ,"webChannel":
        {
            '_embedded.show.webChannel.id':'id',
            '_embedded.show.webChannel.name':'name',
            '_embedded.show.webChannel.officialSite':'officialSite',
            '_embedded.show.webChannel.country.code':'country_id'
        }
        ,"Network":
        {
            '_embedded.show.network.id':'id',
            '_embedded.show.network.name':'name', 
            '_embedded.show.network.officialSite':'officialSite',
            '_embedded.show.webChannel.country.code':'country_id'
        }
        ,"Country":
        {
            '_embedded.show.webChannel.country.name':'name',
            '_embedded.show.webChannel.country.code':'code',
            '_embedded.show.webChannel.country.timezone':'timezone'
        }
        ,"GenrexShow":
        {
            '_embedded.show.genres':'genre_id',
            '_embedded.show.id':'show_id'
        }
        , "SchedulexShow":
        {
            '_embedded.show.schedule.days':'schedule_id',
            '_embedded.show.id':'show_id',
            '_embedded.show.schedule.time':'time'
        }
    }


def set_df_schema(df: pd.DataFrame, table_name: str):
    df.rename(columns = SCHEMA[table_name], inplace=True)

def orquestrate():
    parquet_path = "data/"
    file_list = os.listdir(parquet_path)
    file_list = hndl.clean_file_list(file_list, '.parquet')

    for parquet_table in file_list:
        if parquet_table:
            df = loader.read_from_parquet(parquet_path+parquet_table)
            table_name = parquet_table.split('.')[0]
            # rename columns 
            if table_name in SCHEMA:
                set_df_schema(df, table_name)
            # load df to sqlite
            db_ops.write_table_from_df(table_name, df)
            print(f"Sucess upload {parquet_table} table to sqlite!")