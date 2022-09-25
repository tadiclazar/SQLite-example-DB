import csv

def get_data_from_file(data_filename):
    data = []
    try:
        with open(data_filename, 'r') as csvfile:
            reader = csv.reader(csvfile, dialect='excel', delimiter=',')
            # skip headers
            next(reader)
            for row in reader:
                data.append(tuple(row))

    except FileNotFoundError:
        print("No input file provided, aborting...")
        return None

    return data


def verify_data(mode, data):
    query_data = []
    row_ids = []

    if mode == 'insert':
        for row in data:
            (bank_acc, prov, amount, date), row_id = row, None
            query_data.append((bank_acc, prov, float(amount), date))

    elif mode == 'update':
        for row in data:
            (bank_acc, prov, amount, date, row_id) = row
            query_data.append((bank_acc, prov, float(amount), date, int(row_id)))
            row_ids.append(int(row_id))
    else:
        print("Wrong data format provided, aborting...")
        print("mode [update/insert] data [tuple[tuple[string, string, float, string]]]")
        return None, None

    return query_data, row_ids