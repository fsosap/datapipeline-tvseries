import session      as session
import loader       as loader
import file_handler as hdlr


if __name__ == "__main__":

    daterange = session.daterange()
    print(f"Data extraction will be performed for the data range: {str(daterange.start_date)} to {str(daterange.end_date)}")
    session.set_date_range(daterange)

    # Data ingestion
    loader.load_raw_data_for_timerange(daterange.start_date, daterange.end_date)

    # Clear output
    
    # if bool(input("Do you want to remove json results? True/False")) == True:
    # hdlr.clear_files_from_directory("json/")