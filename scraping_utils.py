from bs4 import BeautifulSoup
import requests
import pandas as pd
import io


def payroll_beautiful_parser(URL):
    """Parse given URL into a BeautifulSoup Object"""
    payroll_html = requests.get(URL).content
    parsed_payroll_html = BeautifulSoup(payroll_html, "html.parser")
    return parsed_payroll_html


def anchor_tag_URL_extraction(parsed_html_webpage) -> str:
    """Extract URL from anchor tags on WUSTL Payroll Site with .xlsx content"""
    payroll_dates_excel_url: str = None
    for anchor in parsed_html_webpage.find_all("a"):
        if str(anchor.get("href")).endswith(".xlsx"):
            payroll_dates_excel_url = anchor.get("href")
            break
        else:
            continue
    return payroll_dates_excel_url


def excel_extraction_from_URL(excel_url: str) -> bytes:
    """Extract Excel file from URL & convert to in-memory binary stream"""
    excel_file: bytes = io.BytesIO(requests.get(excel_url).content)
    return excel_file


def excel_processing(excel_file: bytes, calendar_year: int):
    """Process Excel File (.xlsx) for Payable Dates"""
    payroll_dataframe = pd.read_excel(
        excel_file,
        skiprows=1,
    )
    payroll_dataframe["Month"] = payroll_dataframe["Month"].replace(
        "Setpember", "September"
    )
    payroll_dataframe["Checks Released"] = payroll_dataframe[
        "Checks Released"
    ].dt.strftime(
        "%m/%d"
    )  # Administration added wrong year for some dates; had to truncate & manually add years
    payroll_dataframe["Checks Released"] = (
        payroll_dataframe["Checks Released"] + f"/{str(calendar_year)}"
    )
    final_dataframe = (
        payroll_dataframe.drop(payroll_dataframe.columns[[0, 3, 4, 5]], axis=1)
        .dropna(axis=0)
        .query("`Payroll Type` == 'MON/STP'")
        .reset_index(drop=True)
    )
    return final_dataframe


PAYROLL_URL: str = (
    "https://financialservices.wustl.edu/wfin-topic/payroll/payroll-deadlines/"
)

parsed_html = payroll_beautiful_parser(PAYROLL_URL)
payroll_excel_url = anchor_tag_URL_extraction(parsed_html)
initial_payroll_excel_file = excel_extraction_from_URL(payroll_excel_url)
processed_excel_file = excel_processing(initial_payroll_excel_file, 2023)
