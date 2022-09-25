import sqlite3
from pprint import pprint

def main():
    con = sqlite3.connect('bills.db')
    c = con.cursor()

    with con:
        c.execute('''
        CREATE TABLE IF NOT EXISTS bills
        (bill_id INTEGER PRIMARY KEY, bank_account TEXT NOT NULL, provider TEXT, amount NUMBER, date_paid TEXT)
        ''')

        data = []
        values = c.execute("SELECT * FROM bills").fetchall()
        keys = ('bill_id', 'bank_account', 'provider', 'amount', 'date_paid')

        for row in values:
            data.append({k: v for k, v in zip(keys, row)})

        pprint(data)

if __name__ == '__main__':
    main()
