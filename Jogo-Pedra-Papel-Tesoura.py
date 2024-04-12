# Loop while infinito para o usuário repetir, caso desejar, o jogo novamente. Antes do break deste while, pergunto o
# jogador se desejar jogar novamente, se sim: repete o while, senão termino o while com break.

while True:

        # while infinito para receber as opções dos jogadores
    while True:

        # Recebo a valor do usuario1 e vejo se escolheu uma das 3 opções disponíveis, se caso digitar um valor
        # diferente, terá um aviso para escolher uma das 3 opções.

        usuario1 = str (input('Usuário 1 - Escolha pedra, papel ou tesoura: '))
        if usuario1 != "pedra" and usuario1 != "papel" and usuario1 != "tesoura":
            print("Escolha pedra, papel ou tesoura!")

        usuario2 = str (input('Usuário 2 - Escolha pedra, papel ou tesoura: '))

        # recebo o valor do usuario2

        while usuario1 == usuario2:
        # Crio um loop infinito para verificar se o valor do usuario1 é igual ao usuario2, se sim,
        # o jogo dá empate e pede novamente o valor dos usuários.

            if usuario2 != "pedra" or usuario2 != "papel" or usuario2 != "tesoura":
            # verifico se o usuario2 digitou um valor diferente das opções, se sim
            # irá parar este loop while, para pedir novamente o valor dos usuários
            # no trecho de código número 35.
                break
            print("Empate! Escolha novamente.")
            usuario1 = str(input('Usuário 1 - digite pedra, papel ou tesoura: '))
            usuario2 = str(input('Usuário 2 - digite pedra, papel ou tesoura: '))


        # caso o usuario 2 digitar um valor diferente das opções, o 2 loop while irá repetir.
        if usuario2 != "pedra" and usuario2 != "papel" and usuario2 != "tesoura":
            print("Escolha pedra, papel ou tesoura!")
            continue

        # caso o usuario1 digitar um valor diferente das opçoes, o loop while irá repetir.
        elif usuario1 != "pedra" and usuario1 != "papel" and usuario1 != "tesoura":
            print("Escolha pedra, papel ou tesoura")
            continue

        # se o valor do usuario1 e usuario2 for as opçoes (pedra,papel ou tesoura)
        # saímos deste while com o comando break
        # Para definir qual dos dois usuarios ganhou.
        else:
            break

    # Nesta etapa, sabemos que o usuario1 e usuario2 escolheram as 3 opções (pedra,papel e tesoura)
    # Agora, iremos definir o vencedor a partir do valor de ambos.
    if usuario1 == "pedra" and usuario2 == "papel":
        print('Usuário 2 ganhou o jogo!')

    elif usuario1 == "pedra" and usuario2 == "tesoura":
        print("Usuário 1 ganhou o jogo!")

    elif usuario1 == "papel" and usuario2 == "pedra":
        print('Usuário 1 ganhou o jogo!')

    elif usuario1 == "papel" and usuario2 == "tesoura":
        print('Usuário 2 ganhou o jogo!')

    elif usuario1 == "tesoura" and usuario2 == "pedra":
        print('Usuário 2 ganhou o jogo!')

    elif usuario1 == "tesoura" and usuario2 == "papel":
        print('Usuário 1 ganhou o jogo!')

    # Pergunto se deseja continuar com o game:
    continuar = str(input('Desejas continuar? (S/N): '))
    if continuar in "Ss":
        continue
    else:
        break