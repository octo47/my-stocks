import csv
import typing as t
from converters import us_to_uk_date_str, dollars_to_number


def convert(input_file: t.IO):
    csv_reader = iter(csv.DictReader(input_file, dialect='excel-tab'))
    symbol = None
    price = None
    for row in csv_reader:
        if row['Record Type'] == 'Purchase':
            symbol = row['Symbol']
            price = dollars_to_number(row['Purchase Price'])
        if row['Record Type'] == 'Event' and row['Event Type'] == "PURCHASE":
            date = us_to_uk_date_str(row['Date'])
            released = int(row['Qty'])
            print("BUY %s %s %d %f 0" % (date, symbol, released, price))
