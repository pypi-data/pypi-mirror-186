import csv

def load_from_file(path, func, **kwargs):
    """
    Loads the contents of a file

    :param path: Path of the file to be read from
    :param func: Callable function which will be passed the file object
    :param kwargs:
    :return: Result of the callable function
    """
    file = open(path, **kwargs)
    try:
        result = func(file)
    finally:
        file.close()
    return result


def load_list_from_file(path, delimiter, **kwargs):
    """
    Loads a file containing a list of strings as it contents with a string in every new line

    :param str path: path of the file
    :param str delimiter: Delimiter for the strings
    :return: a list of words in the file
    """
    return load_from_file(path, lambda x: set(x.read().split(delimiter)), **kwargs)


def write_to_csv(path, mode, rows):
    """
    Write rows to a CSV file

    :param str path: path of the file
    :param str mode: file mode in which the file is to be opened
    :param list(tuple) rows: Rows which have to be written to the CSV
    """
    file = open(path, mode)
    try:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
    finally:
        file.close()


def read_from_csv(path):
    """
    Reads the values from a CSV file

    :param str path: Path of the CSV file on the local machine
    :return: a list of tuples representing the rows of the CSV file
    """
    csvfile = open(path)
    rows = []
    try:
        readCSV = csv.reader(csvfile, delimiter=',')
        rows = [row for row in readCSV]
    finally:
        csvfile.close()
    return rows


def remove_duplicates(path, index):
    """
    Remove duplicate rows from a CSV file

    :param str path: path of the CSV file
    :param int index: index of the row whose values are to be unique
    """
    csvfile = open(path)
    row_dict = {}
    unique_rows = []
    try:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            try:
                row_dict[row[index].strip()] = row
            except IndexError:
                unique_rows.append(row)
                print('[{}]Unable to parse row : {}'.format(path, row))
        # Adding all the unique rows to the list of unique rows
        for key, value in row_dict.items():
            unique_rows.append(value)
    finally:
        # close connection to the file
        csvfile.close()
    write_to_csv(path, 'w', unique_rows)
