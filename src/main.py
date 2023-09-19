import os
import session as session
import loader as loader
import processor as processor
import model as model
import sql_feeder as sql_feed
import db_operations as db_ops
from datetime import datetime

if __name__ == "__main__":
    # Read START_DATE and END_DATE from environment variables
    start_date = os.environ.get("START_DATE")
    end_date = os.environ.get("END_DATE")
    if start_date and end_date:
        # Print the values of environment variables for debugging
        print(f"START_DATE: {start_date}")
        print(f"END_DATE: {end_date}")
        # Parse and validate the environment variables or use default values
        try:
            # Check if the dates are valid
            datetime.strptime(start_date, "%Y-%m-%d").date()
            datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError as e:
            print("Invalid date format in START_DATE or END_DATE environment variables.")
            print(e)
            exit(1)

        # Create a daterange object with the provided or environment dates
        daterange = session.daterange(start_date, end_date)
    else:
        # Define default values if the environment variables are not set
        DEFAULT_START_DATE = "2022-12-01"
        DEFAULT_END_DATE = "2022-12-31"
        # Set the date range using the session module if environment variables are empty
        start_date =  DEFAULT_START_DATE
        end_date = DEFAULT_END_DATE
        # Create a daterange object with the provided or default dates
        daterange = session.daterange(start_date, end_date)
        session.set_date_range(daterange)

    # Inform the user about the selected date range
    print(f"Data extraction will be performed for the data range: {str(daterange.start_date)} to {str(daterange.end_date)}")

    # Data ingestion
    loader.load_raw_data_for_timerange(daterange.start_date, daterange.end_date)

    # Data integration
    master_df = processor.integrate_dfs()

    # Split into data model entities
    model.orchestrate(master_df)

    # Load tables into SQLite db
    sql_feed.orquestrate()

    while True:
        print("Provide the query you want to execute:"
              "\n Example:"
              "\n * SELECT AVG(ratingAverage) FROM Show"
              "\n * SELECT AVG(ratingAverage) FROM Episode"
              "\n * SELECT COUNT(show_id), name FROM GenrexShow INNER JOIN Genre ON Genre.genre_id = GenrexShow.genre_id GROUP BY genre_id")
        print(db_ops.execute_sql_query(input("Your query: ")))
