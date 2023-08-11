from datetime import date, timedelta

class daterange():
    def __init__(self):
        self.start_date = date(2022,12,1)
        self.end_date = date(2022,12,31)

    def set_dates(self, new_start_date, new_end_date):
        self.start_date = new_start_date
        self.end_date = new_end_date

def set_date_range(daterange:daterange):
    while input("If you want to proceed press the enter key, else you'll modify the date") != "":
        start_date = date(int(input("(YYYYMMDD)Provide the initial date:")))
        end_date = date(int(input("(YYYYMMDD)Provide the final date:")))

        if start_date > end_date:
            print(f"No valid data range: initial data cannot be greater than the final one \n {start_date} > {end_date}")
        else:
            daterange.set_dates(start_date, end_date)

if __name__ == "__main__":
    daterange = daterange()
    print(f"Data extraction will be performed for the data range: {str(daterange.start_date)} to {str(daterange.end_date)}")
    set_date_range(daterange)