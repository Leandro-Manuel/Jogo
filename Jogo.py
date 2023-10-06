usuario1 = str(input('Usuário 1, digite pedra, papel ou tesoura: '))
usuario2 = str(input('Usuário 2, digite pedra, papel ou tesoura: '))

while usuario1 == usuario2:
    usuario1 = str(input('Usuário 1, digite pedra, papel ou tesoura: '))
    usuario2 = str(input('Usuário 2, digite pedra, papel ou tesoura: '))

if usuario1 == "pedra" and usuario2 == "papel":
    print('Usuário 2 ganhou o jogo!')

elif usuario1 == "pedra" and usuario2 == "tesoura":
    print('Usuário 1 ganhou o jogo!')

elif usuario1 == "papel" and usuario2 == "pedra":
    print('Usuário 1 ganhou o jogo!')

elif usuario1 == "papel" and usuario2 == "tesoura":
    print('Usuário 2 ganhou o jogo!')

elif usuario1 == "tesoura" and usuario2 == "pedra":
    print('Usuário 2 ganhou o jogo!')

elif usuario1 == "tesoura" and usuario2 == "papel":
    print('Usuário 1 ganhou o jogo!')
