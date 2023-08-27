import datetime
from icalendar import Calendar, Event, vText
import os
import pandas as pd
from pathlib import Path

def retrieve_current_date() -> str:
    """Return current date in MM/DD/YYYY format"""
    return datetime.datetime.now().strftime("%m/%d/%Y")

def calendar_generation(paydate_dataframe):
    paydate_dataframe.rename(columns={"Checks Released":"Released"})
    generated_calendar = Calendar()
    generated_calendar.add('prodid', '-//WUSTL DBBS PhD Stipend Pay Dates//EN')
    generated_calendar.add('version', '2.0')
    paydate_dict = dict(zip(paydate_dataframe.Month, paydate_dataframe.Released))
    for month, date in paydate_dict.items():
        calendar_event = Event()
        calendar_event.add('name', f'{month} Stipend Pay Date')
        calendar_event.add('description', f'WUSTL DBBS Stipend Pay Date for {month}')
        calendar_event.add('dtstart', f'{date}')
        calendar_event.add('dtend', f'{date}')
        generated_calendar.add_component(calendar_event)

def date_string_to_int(date: str, initial_format: str, desired_format: str):
    datetime_conversion = datetime.strptime(date, initial_format)
    date_as_integer = int(datetime_conversion.strftime(desired_format))
    return date_as_integer


# def check_closest_paydate(paydate_dataframe, current_date):
#     paydate_dataframe["Checks Released"] = pd.to_datetime(
#         paydate_dataframe["Checks Released"]
#     ).date()
#     paydates_array = paydate_dataframe["Checks Released"].to_list()
#     sorted_paydates_array = paydates_array.sort()
#     for date in sorted_paydates_array:
#         if current_date > date: