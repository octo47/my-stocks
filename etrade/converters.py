from datetime import datetime


def us_to_uk_date(date: str) -> str:
    return datetime.strptime(date, '%m/%d/%Y').strftime('%d/%m/%Y')


def dollars_to_number(dollars: str) -> float:
    return float(dollars.replace("US$", "").replace(",", ""))
