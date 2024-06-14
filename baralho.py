import random

class Carta:
    def __init__(self, nome, valor, naipe):
        self.nome = nome
        self.valor = valor
        self.naipe = naipe

class Baralho:
    def __init__(self):
        naipes = ['Espadas', 'Copas', 'Paus', 'Ouros']
        valores = {
            'A': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10
        }
        self.cartas = []
        for naipe in naipes:
            for valor in valores:
                self.cartas.append(Carta(valor, valores[valor], naipe))

    def embaralhar(self):
        random.shuffle(self.cartas)
