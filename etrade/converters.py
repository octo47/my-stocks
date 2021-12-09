from datetime import datetime


def us_to_uk_date_str(date: str) -> str:
    return us_to_uk_date(date).strftime('%d/%m/%Y')


def us_to_uk_date(date: str) -> datetime:
    return datetime.strptime(date, '%m/%d/%Y')


def dollars_to_number(dollars: str) -> float:
    return float(dollars.replace("US$", "").replace(",", ""))
