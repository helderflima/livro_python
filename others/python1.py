__author__ = 'helderflima'
# coding: utf-8


class Animal:
    """ Classe que representa as características dos animais
    """
    def __init__(self, nome, cor):

        self._nome = nome
        self._cor = cor
        self._som = None

    def emitir_som(self):
        return self._som

    def dormir(self):
        return "ZzzzZZZzzzZZZzzz..."

    def __str__(self):
        return "Sou um animal e você pode me chamar de {}, minha cor é {}!".format(self._nome, self._cor)


class Cachorro(Animal):
    """ Essa classe representa um Animal da espécie Cachorro
    """
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        self._som = "Au au..."

    def __str__(self):
        return "Eu sou um Cachorro, meu nome é {}, minha cor é {} e eu falo {}".format(self._nome, self._cor, self._som)


class Gato(Animal):
    """ Essa classe representa um Animal da espécie gato
    """
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        self._som = "Miau..."

    def __str__(self):
        return "Eu sou um Gato, meu nome é {}, minha cor é {} e eu falo {}".format(self._nome, self._cor, self._som)

    def subir_casa(self):
        return "Subindo em cima da casa."