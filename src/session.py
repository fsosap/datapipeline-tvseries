from datetime import date, datetime

class daterange():
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def set_dates(self, new_start_date, new_end_date):
        self.start_date = new_start_date
        self.end_date = new_end_date

def get_input_params() -> tuple:
    date_format = "%Y-%m-%d"
    start_date_txt = str(input("(format:YYYY-MM-DD)Provide the initial date:"))
    end_date_txt = str(input("(format:YYYY-MM-DD)Provide the final date:"))
    return (datetime.strptime(start_date_txt, date_format).date(), datetime.strptime(end_date_txt, date_format).date())

def set_date_range(daterange:daterange):
    while input("If you want to proceed press the enter key, else you'll modify the date:\n") != "":
        dates = get_input_params()
        start_date, end_date = dates[0], dates[1]

        if start_date > end_date:
            print(f"No valid data range: initial data cannot be greater than the final one \n {start_date} > {end_date}")
        else:
            daterange.set_dates(start_date, end_date)
            print(f"Data extraction will be performed for the data range: {str(daterange.start_date)} to {str(daterange.end_date)}")
