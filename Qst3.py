def desconto():
    print('Desconto de 15% para menores de 21, e de 10% para maiores de 21')

    idadeDesc = int(input('\nInsira aqui a sua idade: '))

    if idadeDesc < 21:
        print('Desconto de 15%!')
    else:
        print('Desconto de 10%!')

desconto()
