import session      as session
import loader       as loader
import file_handler as hdlr
import processor    as processor


if __name__ == "__main__":

    daterange = session.daterange()
    print(f"Data extraction will be performed for the data range: {str(daterange.start_date)} to {str(daterange.end_date)}")
    session.set_date_range(daterange)

    # Data ingestion
    loader.load_raw_data_for_timerange(daterange.start_date, daterange.end_date)

    # Data integration
    master_df = processor.integrate_dfs()
    processor.save_df_to_parquet("data/master_dataset.parquet", master_df)

    # Split into data models entities
