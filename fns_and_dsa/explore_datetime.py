from datetime import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.date.today() + datetime.timedelta(days)
    print(f"Future date: {future_date}")
display_current_datetime()
calculate_future_date()
