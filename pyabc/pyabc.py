import csvload
from pyabc.config import *

def main():
    csv_load_list = [
        'kraj_0',
        'ku_0',
        'obec_0',
        'okres_0',
        'sr_0'
    ]

    for item in csv_load_list:
        csvload.create_load_tbl(db_params, item)

if __name__ == '__main__':
    main()
