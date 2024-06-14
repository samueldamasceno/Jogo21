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
            'Ás': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Valete': 10,
            'Dama': 10,
            'Rei': 10
        }
        self.cartas = []
        for naipe in naipes:
            for valor in valores:
                nome_carta = f'{valor} de {naipe}'
                valor_carta = valores[valor]
                carta = Carta(nome_carta, valor_carta, naipe)
                self.cartas.append(carta)

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_cartas(self, quantidade):
        if len(self.cartas) < 1:
            print("O baralho está vazio.")
            return None
        elif len(self.cartas) < quantidade:
            print("Não há cartas suficientes no baralho.")
            return None
        else:
            cartas_distribuidas = []
            for i in range(quantidade):
                cartas_distribuidas.append(self.cartas.pop(0))
            return cartas_distribuidas