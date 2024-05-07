from random import randint
comp = randint(1, 100)
print("{:=^60}".format(" Bem vindo ao jogo da adivinhação "))
palpite = int(input("Digite seu palpite: "))

while comp != palpite: 
    
    if comp > palpite:
        print("Seu palpite é menor que o numero sorteado, tente novamente")
    elif comp < palpite:
        print("Seu palpite é maior que o numero sorteado, tente novamente ")
    elif comp == palpite:
        print("Parabens!!! vc acertou o palpite")
        break
    palpite = int(input("Digite seu palpite: "))

