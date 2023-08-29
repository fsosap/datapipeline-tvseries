import session      as session
import loader       as loader
import processor    as processor
import model        as model
import sql_feeder   as sql_feed


if __name__ == "__main__":

    daterange = session.daterange()
    print(f"Data extraction will be performed for the data range: {str(daterange.start_date)} to {str(daterange.end_date)}")
    session.set_date_range(daterange)

    # Data ingestion
    loader.load_raw_data_for_timerange(daterange.start_date, daterange.end_date)

    # Data integration
    master_df = processor.integrate_dfs()
    
    # Split into data model entities
    model.orchestrate(master_df)

    # Load tables into sqlite db
    sql_feed.orquestrate()