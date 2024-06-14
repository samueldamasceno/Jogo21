# jogo de 21 no terminal em python
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

def calcular_total(cartas):
    total = 0
    for carta in cartas:
        total += carta.valor
    return total

def exibir_cartas(cartas):
    for carta in cartas:
        print(f"- {carta.nome}")
    total = calcular_total(cartas)
    print(f"Total: {total}")
    print()

def calcular_resultado(cartas_jogador, cartas_oponente):
    total_jogador = calcular_total(cartas_jogador)
    total_oponente = calcular_total(cartas_oponente)
    if total_jogador > 21:
        derrota()
        return
    elif total_oponente > 21:
        vitoria()
        return
    elif total_jogador > total_oponente:
        vitoria()
        return
    elif total_jogador < total_oponente:
        derrota()
        return
    elif total_jogador == total_oponente:
        empate()
        return
    
def derrota():
    print()
    print("Você perdeu!")
    print()

def vitoria():
    print()
    print("Você ganhou!")
    print()

def empate():
    print()
    print("Empate!")
    print()

def iniciar_jogo():
    bem_vindo()
    baralho = Baralho()
    baralho.embaralhar()

    cartas_jogador = baralho.distribuir_cartas(2)
    cartas_oponente = baralho.distribuir_cartas(2)

    print()
    print("Suas cartas:")
    exibir_cartas(cartas_jogador)
    print("As cartas do oponente estão viradas por enquanto")
    print()

    while True:
        opcao = input("""Deseja comprar mais uma carta?
                      1. Sim
                      2. Não
                      Digite a opção desejada: """)
        
        if opcao == "1":
            carta_nova = baralho.distribuir_cartas(1)[0]
            cartas_jogador.append(carta_nova)
            print(f"Você comprou: {carta_nova.nome}")
            print("Suas cartas agora:")
            exibir_cartas(cartas_jogador)
            if calcular_total(cartas_jogador) > 21:
                print("Você passou de 21!")
                break
        elif opcao == "2":
            print()
            print("Vamos calcular os pontos finais...")
            break
        else:
            print("Opção inválida!")

    print()
    print("As cartas do oponente:")
    exibir_cartas(cartas_oponente)
    
    calcular_resultado(cartas_jogador, cartas_oponente)

while True:
    iniciar_jogo()
    print()
    print("""Deseja jogar novamente?
          1. Sim
          2. Não""")
    opcao = input()
    if opcao == "1":
        print()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif opcao == "2":
        print()
        print("Até a próxima!")
        break

