import random

def jogar():

    print("*" * 20)
    print("Jogo de adivinhação!")
    print("*" * 20)

    numero_secreto = random.randrange(1, 101)
    chances = 0
    pontos = 100
    #rodadas = 1

    print("Qual nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        chances = 20
    elif(nivel == 2):
        chances = 10
    else:
        chances = 5

    #while(rodadas <= chances):
    for rodadas in range(1, chances + 1):

        print(f"Tentativa {rodadas} de {chances}")

        chute = int(input("Digite um número entre 1 e 100: "))

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        elif(maior) :
            print("Você digitou um valor maior que o número alvo.")
        elif(menor):
            print("Você digitou um número menor que o número alvo.")
            pontos_perdidos = round(abs(numero_secreto - chute)/ 3) #abs() serve para modular o numero
            pontos = pontos - pontos_perdidos

        #rodadas = rodadas + 1

    print("Fim do jogo")

if(__name__ == "__main__"):          #serve para diferenciar a importação da execução
    jogar()
