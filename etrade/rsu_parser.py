import csv
import typing as t
from converters import us_to_uk_date, dollars_to_number


def convert(input_file: t.IO):
    csv_reader = iter(csv.DictReader(input_file, dialect='excel-tab'))
    symbol = None
    for row in csv_reader:
        if row['Record Type'] == 'Grant':
            symbol = row['Symbol']
        if row['Record Type'] == 'Vest Schedule':
            date = us_to_uk_date(row['Vest Date'])
            grant = "%s/%s" % (row['Grant Number'], row['Vest Period'])
            released = int(row['Released Qty'])
            # skip vested only lines
            if released < 1:
                continue
            total = dollars_to_number(next(csv_reader)['Taxable Gain'])
            print("BUY %s %s %d %f 0" % (date, symbol, released, total / float(released)))
