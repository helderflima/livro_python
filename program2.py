__author__ = 'helder'
# coding: utf-8


import os


def main():
    meta = {}
    for meta_data_file in os.listdir("data/meta-data"):
        table_name = meta_data_file.split('.')[0]
        print(table_name)

if __name__ == '__main__':
    main()
