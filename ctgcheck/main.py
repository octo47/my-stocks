import fileinput
import re
from datetime import datetime

import click


class Tx(object):
    def __init__(self, symbol: str, tx_type: str, date: datetime, amount: int, price: float, fee: float):
        self.symbol = symbol
        self.tx_type = tx_type
        self.date = date
        self.amount = amount
        self.price = price
        self.fee = fee


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=None))
def check(input_file: str):
    with fileinput.input(input_file) as inp:
        holdings: dict[str, list[Tx]] = {}
        for l in inp:
            l = l.rstrip()
            parts = re.split(' +', l)
            if len(parts) != 6:
                continue
            symbol = parts[2]
            tx = Tx(symbol=symbol,
                    tx_type=parts[0],
                    date=datetime.strptime(parts[1], '%d/%m/%Y'),
                    amount=int(parts[3]),
                    price=float(parts[4]),
                    fee=float(parts[5]))
            if symbol not in holdings:
                holdings[symbol] = []
            holdings[symbol].append(tx)
        for k, v in holdings.items():
            v.sort(key=lambda x: x.date)
        for _, v in holdings.items():
            total = 0
            for tx in v:
                if tx.tx_type == 'BUY':
                    total += tx.amount
                elif tx.tx_type == 'SELL':
                    total -= tx.amount

                print("%s %s %s %d %f %f # %d" % (
                     tx.tx_type, tx.symbol, tx.date, tx.amount, tx.price, tx.fee, total))


if __name__ == '__main__':
    check()
