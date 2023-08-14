import pandas as pd
import loader as loader

def create_many2many_df(column_name:str, df:pd.DataFrame) -> pd.DataFrame:
    entity_df = df[column_name]
    entity_names = get_entity_names(entity_df)
    dict_with_id = pd.Series(entity_names, index=range(1,len(entity_names)+1))
    entity_df = pd.DataFrame({"id":dict_with_id.index, "name":dict_with_id.values})
    return entity_df

def get_entity_names(element_list:list) -> list:
    entity_names = []
    for inside_list in element_list:
        if len(inside_list):
            for item in inside_list:
                if item not in entity_names:
                    entity_names.append(item)
    
    return entity_names

def extract_entities_df(columns:list, df:pd.DataFrame) -> pd.DataFrame:
    return df[columns]

def orchestrate(df:pd.DataFrame):
    parquet_path = "data/"
    # create many2many entities
    M2M_ENTITIES = {"_embedded.show.genres":"genre", "_embedded.show.schedule.days":"schedule"}
    for entity in M2M_ENTITIES:
        loader.save_df_to_parquet(parquet_path+M2M_ENTITIES[entity]+'.parquet', create_many2many_df(entity, df))
    
    # create canonical tables
    ENTITIES = \
    {
        "Episode":[
            'id', 
            'url', 
            'name', 
            'season', 
            'number', 
            'type', 
            'airdate', 
            'airtime',
            'airstamp', 
            'runtime', 
            'summary', 
            'rating.average']
        ,"Show":[
            '_embedded.show.id', 
            '_embedded.show.url',
            '_embedded.show.name', 
            '_embedded.show.type', 
            '_embedded.show.language',
            '_embedded.show.status',
            '_embedded.show.runtime', 
            '_embedded.show.averageRuntime',
            '_embedded.show.premiered', 
            '_embedded.show.ended',
            '_embedded.show.officialSite', 
            '_embedded.show.rating.average',
            '_embedded.show.weight', 
            '_embedded.show.summary',
            '_embedded.show.updated']
        ,"webChannel":[
            '_embedded.show.webChannel.id',
            '_embedded.show.webChannel.name',
            '_embedded.show.webChannel.officialSite']
        ,"Network":[
            '_embedded.show.network.id',
            '_embedded.show.network.name', 
            '_embedded.show.network.officialSite']
        ,"Country":[
            '_embedded.show.webChannel.country.name',
            '_embedded.show.webChannel.country.code',
            '_embedded.show.webChannel.country.timezone']
    }
    
    for entity in ENTITIES:
        loader.save_df_to_parquet(parquet_path+entity+'.parquet', extract_entities_df(ENTITIES[entity], df))