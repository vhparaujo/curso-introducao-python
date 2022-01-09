print("*" * 20)
print("Jogo de adivinhação!")
print("*" * 20)

numero_secreto = 7
chute = int(input("Digite seu numero: "))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Você acertou!!!")
elif(maior) :
    print("Você digitou um valor maior.")
elif(menor):
    print("Você digitou um número menor.")

print("Fim do jogo")
