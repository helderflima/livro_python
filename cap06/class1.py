__author__ = 'helder'
# coding: utf-8

class DataTable:
    """ Representa uma tabela de dados

        Essa classe representa uma tabela de dados do portal
        da transparência. Deve ser capaz de validar linhas
        inseridas de acordo com as colunas de possui. As
        linhas inseridas ficam registradas dentro dela.

        Attributes:
            name: Nome da tabela
            columns: [Lista de colunas]
            data: [Lista de dados]
    """
    def __init__(self, name):
        """ Construtor

            Args:
                name: Nome da tabela

        """
        self._name = name
        self._columns = []
        self._data = []
        self._references = []
        self._referenced = []

    def add_column(self, name, kind, description):
        column = Column(name, kind, description)
        self._columns.append(column)
        return column


class Column:
    """ Representa uma coluna em uma DataTable

        Essa classe contém as informações de uma coluna
        e deve validar um dado de acordo com o tipo de
        dado configurado no construtor.

        Attributes:
            name: Nome da Coluna
            kind: Tipo do dado (varchar, bigint, numeric)
            description: Descrição da coluna
    """

    def __init__(self, name, kind, description):
        """ Construtor

            Args:
                name: Nome da Coluna
                kind: Tipodo dado (varchar, bigint, numeric)
                description: Descrição da coluna
        """
        self._name = name
        self._kind = kind
        self._description = description


class Relationship():
    """ Classe que representa um relacionamento entra DataTables

        Essa tem todas as informações que identificam um
        relacionamento entre tabelas. Em qual coluna ele existe,
        de onde ele vem e pra onde ele vai.

        Attributes:
            name: Nome
            from: Tabela de onde sai
            to: Tabela pra onde sai
            on: Instância de coluna onde existe
    """
    def __init__(self, name, _from, to, on):
        self._name = name
        self._from = _from
        self._to = to
        self._on - on

        