# jogo de 21 no terminal em python

import random
import os

from baralho import Baralho

def bem_vindo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bem-vindo ao jogo de 21!")
    print()
    while True:
        print("""Você conhece as regras?
              1. Sim
              2. Não""")
        resposta = input("Digite a opção que deseja: ")
        if resposta == "1":
            print()
            print("Ótimo! Então vamos começar!")
            print()
            break
        elif resposta == "2":
            regras()
        else:
            print()
            print("Opção inválida!")
            print()

def regras():
    print()
    print("Regras do jogo:")
    print()
    print("""
        1. O objetivo é obter uma mão com um valor total mais próximo de 21 do que o oponente, sem ultrapassar.
        2. Ás vale 1 ponto. As cartas de 2 a 10 valem seu valor normal. J, Q e K valem 10 pontos cada.
        3. Em cada rodada, você tem a opção de comprar uma carta ou parar de comprar.
        4. Se você comprar uma carta, ela será adicionada à sua mão.
        5. Se você parar de comprar, sua mão será comparada com a mão do oponente.
        6. Se a sua mão for maior que 21, você perde.
        7. Se a sua mão for menor que a do oponente, você ganha.
        8. Se as duas mãos forem iguais, você perde.""")
    print()
    print("Boa sorte!")
    print()

def iniciar_jogo():
    bem_vindo()
    baralho = Baralho()
    baralho.embaralhar()

    cartas_jogador = baralho.distribuir_cartas(2)
    cartas_oponente = baralho.distribuir_cartas(2)

iniciar_jogo()
