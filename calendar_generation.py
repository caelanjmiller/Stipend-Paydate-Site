from datetime import datetime
from ics import Calendar, Event
import bisect


def retrieve_current_date() -> str:
    """Return current date in MM/DD/YYYY format"""
    return datetime.now().strftime("%m/%d/%Y")


def date_string_to_datetime(date: str, initial_format: str):
    datetime_conversion = datetime.strptime(date, initial_format)
    return datetime_conversion


def calendar_generation(paydate_dataframe):
    generated_calendar = Calendar()
    paydate_dict = dict(
        zip(paydate_dataframe["Month"], paydate_dataframe["Checks Released"])
    )
    for month, date in paydate_dict.items():
        event_date_start = datetime.strptime(date, "%m/%d/%Y").date()
        calendar_event = Event()
        calendar_event.name = f"{month} Stipend Pay Date"
        calendar_event.description = f"WUSTL DBBS Stipend Pay Date for {month}"
        calendar_event.begin = event_date_start  # type: ignore
        calendar_event.make_all_day()
        generated_calendar.events.add(calendar_event)
    final_calendar = generated_calendar.serialize()
    return final_calendar


def date_string_to_int(date: str, initial_format: str, desired_format: str):
    datetime_conversion = datetime.strptime(date, initial_format)
    date_as_integer = int(datetime_conversion.strftime(desired_format))
    return date_as_integer


def check_closest_paydate(paydate_dataframe, current_date_int: int):
    int_dates_array = []
    date_string_array = paydate_dataframe["Checks Released"].tolist()
    for date in date_string_array:
        int_date = date_string_to_int(date, "%m/%d/%Y", "%m%d%Y")
        int_dates_array.append(int_date)
    int_dates_array.sort()
    paydate_index: int = bisect.bisect(int_dates_array, current_date_int)
    next_pay_date_datetime = datetime.strptime(
        str(int_dates_array[paydate_index]), "%m%d%Y"
    ).date()
    next_pay_date = next_pay_date_datetime.strftime("%m/%d/%Y")
    return next_pay_date
