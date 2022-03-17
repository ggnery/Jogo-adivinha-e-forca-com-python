def verifica_entrada_usuario(chute):
    if (chute < 1 or chute > 100):
        print("voce escolheu um numero fora do intervalo e perdeu uma tentativa \n")
        return True

def iniciar_adivinhacao():

    import random
    numero_sorteado = round(random.randrange(1, 101))
    numero_tentativas = 0
    nivel = 0
    pontos = 1000

    print("JOGO DA ADIVINHAÇAO")
    print("********************")

    while (nivel != 1 and nivel != 2 and nivel != 3):
        nivel = int(input("escolha um nivel: (1)facil (2)medio (3)dificil: "))
        if (nivel == 1):
            numero_tentativas = 20
        elif (nivel == 2):
            numero_tentativas = 10
        elif (nivel == 3):
            numero_tentativas = 5
        else:
            print("Voce digitou um valor invalido\n")

    for rodada in range(1, numero_tentativas + 1):

        print("Voce tem {} tentativas de {}".format(rodada, numero_tentativas))
        chute_str = input("digite um numero entre 1 e 100: ")
        chute = int(chute_str)

        acertou = chute == numero_sorteado
        menor = chute < numero_sorteado
        maior = chute > numero_sorteado

        if (acertou):
            print("Voce acertou! parabens \n")
            break
        else:
            pontos_perdidos = abs(numero_sorteado - chute)
            pontos = pontos - pontos_perdidos
            if (menor):
                print("Voce errou! O numero chutado é menor que o numero sorteado \n")
            elif (maior):
                print("Voce errou! O numero chutado é maior que o numero sorteado \n")

            if (numero_tentativas == rodada):
                print("o numero secreto era {}".format(numero_sorteado))


        rodada = rodada + 1

    print("Voce fez", pontos, "pontos \n")
    print("Fim")

if(__name__=="__main__"):
    iniciar_adivinhacao()




