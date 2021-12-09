import csv
import typing as t
from datetime import datetime

from converters import us_to_uk_date_str, dollars_to_number, us_to_uk_date


def convert(input_file: t.IO):
    csv_reader = iter(csv.DictReader(input_file, dialect='excel-tab'))
    symbol = None
    price = None
    splitAt = datetime(2020, 8, 31)
    for row in csv_reader:
        if row['Record Type'] != 'Sell':
            continue
        symbol = row['Symbol']
        date = us_to_uk_date_str(row['Date Sold'])
        qty = int(row['Qty.'])
        price = dollars_to_number(row['Proceeds Per Share'])
        txn_date = us_to_uk_date(row['Date Sold'])
        if txn_date < splitAt:
            price = price / 4
            qty = qty * 4

        print("SELL %s %s %d %f 0" % (date, symbol, qty, price))
