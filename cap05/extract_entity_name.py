__author__ = 'helder'
# coding: utf-8

import sys

def main(filename):
    return filename.split('.')[0]

if __name__ == '__main__':
    main(sys.argv(1))