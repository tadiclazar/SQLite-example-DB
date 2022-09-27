import sqlite3
from pprint import pprint

def main():
    con = sqlite3.connect('bills.db')
    c = con.cursor()

    with con:
        values = c.execute("SELECT * FROM bills").fetchall()
        keys = ('bill_id', 'bank_account', 'provider', 'amount', 'date_paid')

        data = [dict(zip(keys, row)) for row in values]

        pprint(data)

if __name__ == '__main__':
    main()
