__author__ = 'helder'

# coding: utf-8
import os


def read_lines(file_name):
    _file = open(file_name, "rt")
    data = _file.read().split("\n")
    _file.close()
    return data


def read_metadata(file_name):
    metadata = []
    for coluna in read_lines(os.path.join("data/meta-data", file_name)):
        if coluna:
            value = coluna.split('\t')
            nome = value[0]
            tipo = value[1]
            desc = value[2]
            metadata.append((nome, tipo, desc))
    return metadata


def main():
    meta = {}
    keys = {}

    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_name(meta_data_file)
        atrributes = read_metadata(meta_data_file)
        identifier = atrributes[0][0]
        meta[table_name] = atrributes
        keys[identifier] = table_name

    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    print("Entidade {} -> {}".format(key, col[0]))


def extract_name(name):
    return name.split('.')[0]


if __name__ == '__main__':
    main()