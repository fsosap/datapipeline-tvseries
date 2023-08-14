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
    for inner_list in element_list:
        if len(inner_list):
            for item in inner_list:
                if item not in entity_names:
                    entity_names.append(item)
    
    return entity_names

def extract_entities_df(columns:list, df:pd.DataFrame) -> pd.DataFrame:
    return df[columns]

def fill_m2m_table(df: pd.DataFrame) -> pd.DataFrame:
    parquet_path = "data/"
    M2M_TABLES = {"GenrexShow":['_embedded.show.genres','_embedded.show.id']\
                , "SchedulexShow":['_embedded.show.schedule.days','_embedded.show.id','_embedded.show.schedule.time']}

    for table in M2M_TABLES:
        resultant_df = pd.DataFrame(columns=M2M_TABLES[table])
        m2m_relationship = extract_entities_df(M2M_TABLES[table], df)
        entity_name = table.split("x")[0].lower()
        entity_table = loader.read_from_parquet(f"data/{entity_name}.parquet")["name"].values.tolist()
        for index, row in m2m_relationship.iterrows():
            inner_list = row[M2M_TABLES[table][0]]
            if len(inner_list):
                show_id = row[M2M_TABLES[table][1]]
                for item in inner_list:
                    if item in entity_table:
                        if table.startswith("Genre"):
                            new_row = [entity_table.index(item)+1,show_id]
                        else:
                            new_row = [entity_table.index(item)+1,show_id,row[M2M_TABLES[table][2]]]
                        resultant_df.loc[len(resultant_df)] = new_row

        loader.save_df_to_parquet(parquet_path+table+'.parquet', resultant_df)


def orchestrate(df:pd.DataFrame):
    parquet_path = "data/"
    # create many2many entities
    M2M_ENTITIES = {"_embedded.show.genres":"genre", "_embedded.show.schedule.days":"schedule"}
    
    for entity in M2M_ENTITIES:
        incoming_df = create_many2many_df(entity, df)
        loader.save_df_to_parquet(parquet_path+M2M_ENTITIES[entity]+'.parquet', incoming_df)

    # fill m2m_tables
    fill_m2m_table(df)

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
            'rating.average',
            '_embedded.show.id']
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
            '_embedded.show.updated',
            '_embedded.show.webChannel.id',
            '_embedded.show.network.id']
        ,"webChannel":[
            '_embedded.show.webChannel.id',
            '_embedded.show.webChannel.name',
            '_embedded.show.webChannel.officialSite',
            '_embedded.show.webChannel.country.code']
        ,"Network":[
            '_embedded.show.network.id',
            '_embedded.show.network.name', 
            '_embedded.show.network.officialSite',
            '_embedded.show.webChannel.country.code']
        ,"Country":[
            '_embedded.show.webChannel.country.name',
            '_embedded.show.webChannel.country.code',
            '_embedded.show.webChannel.country.timezone']
    }
    
    for entity in ENTITIES:
        loader.save_df_to_parquet(parquet_path+entity+'.parquet', extract_entities_df(ENTITIES[entity], df))