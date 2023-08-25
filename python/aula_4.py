idade = int(input('Digite sua idade: '))

if idade >= 18 and idade <= 50:
    print(f'Você pode entrar, você tem {idade}')
elif idade >= 50:
    print('Você está entrando na melhor idade, não posso deixar entrar!')
elif idade <= 17:
    print('Você não pode entrar!')