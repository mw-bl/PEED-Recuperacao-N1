import random

def numAleatorio():
    print('Adivinhe o número entre 1 e 50.')
    n = random.randint(1, 50)

    while True:
        palpite = int(input('\nDigite seu palpite aqui: '))
        if palpite < n:
            print('Quase! Tente um número maior.')
        elif palpite > n:
            print('Quase! Tente um número menor.')
        else:
            print('Muito bem, você acertou o número!')
            break

numAleatorio()
