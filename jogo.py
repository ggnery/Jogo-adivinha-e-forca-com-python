print("*********************")
print("***ESCOLHA UM JOGO***")
print("*********************")
import jogo_adivinhacao
import forca

def iniciar_jogos():
    jogo_escolhido = int(input("(1) Jogo da adivinhação (2) Forca: "))

    if(jogo_escolhido == 1):
        jogo_adivinhacao.iniciar_adivinhacao()
    if(jogo_escolhido == 2):
        forca.iniciar_forca()

if(__name__=="__main__"):
    iniciar_jogos()

