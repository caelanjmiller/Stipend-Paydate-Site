import datetime


def retrieve_current_date() -> str:
    """Return current date in MM/DD/YYYY format"""
    return datetime.datetime.now().strftime("%m/%d/%Y")
