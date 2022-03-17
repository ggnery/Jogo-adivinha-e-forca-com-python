import random

def iniciar_forca():
    imprime_mensagem_abertura()

    lista_palavras = cria_lista_palavras()
    palavra_secreta = gera_palavra_secreta(lista_palavras)

    enforcou = False
    acertou = False
    erros = 0

    palavra = gera_lista_com_underline(palavra_secreta)
    print(palavra)

    while(not enforcou and not acertou):
        chute = pede_chute_usuario()
        index = 0

        palavra = substitui_underline_por_chute_usuario(index, chute,palavra_secreta, palavra)

        erros = verifica_se_usuario_errou_letra(erros, chute, palavra)

        desenha_forca(erros)

        print(palavra)

        acertou = verifica_se_usuario_acertou_palavra_secreta(palavra)
        enforcou = verifica_se_acabou_chances_usuario(erros)


    escreve_se_venceu_ou_perdeu(acertou, palavra_secreta)

def imprime_mensagem_abertura():
    print("\n*********************")
    print("****JOGO DA FORCA****")
    print("*********************")

def cria_lista_palavras():
    lista = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            lista.append(linha.strip())
        return lista

def gera_palavra_secreta(lista):
    numero_sorteado = random.randrange(0, len(lista))
    return lista[numero_sorteado].upper()

def gera_lista_com_underline(palavra_secreta):
    palavra = ["_" for letra in palavra_secreta]
    return palavra

def pede_chute_usuario():
    chute = input("Escolha uma letra: ")
    print("\n")
    chute = chute.strip()
    chute = chute.upper()
    return chute

def substitui_underline_por_chute_usuario(index, chute,palavra_secreta, palavra):
    for letra in palavra_secreta:
        if (chute == letra):
            palavra[index] = chute
        index += 1
    return palavra

def verifica_se_usuario_errou_letra(erros, chute, palavra):
    if (chute not in palavra):
        print("Voce errou! {} tentativas restantes".format(6 - erros))
        erros += 1
        return erros
    else:
        return erros

def verifica_se_usuario_acertou_palavra_secreta(palavra):
    return "_" not in palavra

def verifica_se_acabou_chances_usuario(erros):
    return erros == 7

def escreve_se_venceu_ou_perdeu(acertou, palavra_secreta):
    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__=="__main__"):
    iniciar_forca()