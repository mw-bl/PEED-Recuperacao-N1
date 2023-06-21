def cMedia():
    print('Calculadora de Média.\n')

    tNotas = 0

    for i in range(10):
        nota = float(input(f'Insira a nota {i+1}: '))
        tNotas += nota

    media = tNotas / 10
    print('Média:', media)

cMedia()
