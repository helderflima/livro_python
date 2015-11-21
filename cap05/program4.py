__author__ = 'helder'

# coding: utf-8

import os

def main():
    _file = open(os.path.join('data/data', "batidas.txt"), "rt")
    data = _file.read().split(" ")
    _file.close()
    for i in data:
        print(i)

if __name__ == '__main__':
    main()
