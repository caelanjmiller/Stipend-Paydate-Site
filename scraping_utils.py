from bs4 import BeautifulSoup
import requests
import pandas as pd
import camelot


def payroll_beautiful_parser(URL):
    """Parse given URL into a BeautifulSoup Object"""
    payroll_html = requests.get(URL).content
    parsed_payroll_html = BeautifulSoup(payroll_html, "html.parser")
    return parsed_payroll_html


def anchor_tag_URL_extraction(parsed_html_webpage, year: str):
    """Extract URL from anchor tags on WUSTL Payroll Site with PDF content"""
    payroll_dates_pdf_url = ""
    for anchor in parsed_html_webpage.find_all("a"):
        if (
            f"{year} Payroll Processing" in anchor.text
        ):  # Filter Specifically for Year of Interest
            if str(anchor.get("href")).endswith(".pdf"):
                payroll_dates_pdf_url = anchor.get("href")
                break
        else:
            continue
    return payroll_dates_pdf_url


def pdf_to_dataframe_processing(pdf_file, calendar_year: int):
    """Process PDF File (.pdf) for Pay Dates"""
    pdf_tables = camelot.read_pdf(pdf_file, pages="1,2")  # Two pages worth of pay dates
    table_one_dataframe = pdf_tables[0].df  # Convert Camelot object from PDF page 1 into dataframe
    table_two_dataframe = pdf_tables[1].df
    table_one_dataframe = table_one_dataframe.rename(
        columns=table_one_dataframe.iloc[0]
    )  # Set Column Header Names From 1st Row Values
    table_two_dataframe = table_two_dataframe.rename(
        columns=table_two_dataframe.iloc[0]
    )
    table_one_dataframe = (
        table_one_dataframe.drop(
            list(table_one_dataframe)[1:8], axis=1
        )  # Drop all rows from position 1 up to but not include position 8
        .dropna(axis=0)
        .query("`P/R` == 'MON/STP'")
        .reset_index(drop=True)
    )
    table_two_dataframe = (
        table_two_dataframe.drop(list(table_two_dataframe)[1:8], axis=1)
        .dropna(axis=0)
        .query("`P/R` == 'MON/STP'")
        .reset_index(drop=True)
    )
    payroll_dataframe = pd.concat(
        [table_one_dataframe, table_two_dataframe], ignore_index=True
    ).rename(columns={"P/R": "Payroll Type", "Pay Date": "Checks Released"})
    payroll_dataframe["Checks Released"] = (
        payroll_dataframe["Checks Released"] + f"/{str(calendar_year)}"
    )
    payroll_dataframe["Month"] = pd.to_datetime(
        payroll_dataframe["Checks Released"]
    ).dt.strftime(
        "%B"
    )  # Create Month Column
    payroll_dataframe = payroll_dataframe[["Month", "Payroll Type", "Checks Released"]]
    return payroll_dataframe


PAYROLL_URL: str = (
    "https://financialservices.wustl.edu/wfin-topic/payroll/payroll-deadlines/"
)

parsed_html = payroll_beautiful_parser(PAYROLL_URL)
payroll_pdf_url = anchor_tag_URL_extraction(parsed_html, "2024")
processed_dataframe = pdf_to_dataframe_processing(payroll_pdf_url, 2024)
