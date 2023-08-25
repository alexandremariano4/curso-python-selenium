def somarNumero(num1,num2):
    return num1 + num2


if __name__ == '__main__':

    numero1 = int(input('Digite o numero 1: '))
    numero2 = int(input('Digite o numero 2: '))


    if somarNumero(numero1,numero2) > 10:
        print('Número maior que 10')
    else:
        print('Número menor que 10')

