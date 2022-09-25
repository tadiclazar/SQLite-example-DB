import sqlite3
import sys

from file_utils import get_data_from_file
from file_utils import verify_data


def main():
    if len(sys.argv) != 2:
        print("Must have one argument!")
        print("Usage: py update_data.py data [file]")
        return None

    mode = 'update'
    pname, data_file = sys.argv[0], sys.argv[1]

    data = get_data_from_file(data_file)

    print(data)
    try:
        data, row_ids = verify_data(mode, data)
    except:
        print("Fatal error, aborting...")
        sys.exit(1)

    print(f"Rows to update:\n{row_ids}")

    con = sqlite3.connect('bills.db')
    c = con.cursor()

    with con:
        c.execute('''
        CREATE TABLE IF NOT EXISTS bills
        (bill_id INTEGER PRIMARY KEY, bank_account TEXT NOT NULL, provider TEXT, amount NUMBER, date_paid TEXT)
        ''')

        if all(rid for rid in row_ids if rid is not None):
            for row in data:
                bank_acc, prov, amount, date, row_id = row
                c.execute(
                    '''
                    UPDATE bills SET bank_account = ?, provider = ?, amount = ?, date_paid = ?
                    WHERE bill_id = ?
                    ''', (bank_acc, prov, amount, date, row_id)
                )
        else:
            print('All row ids must not be None')
            sys.exit(1)

if __name__ == '__main__':
    main()
