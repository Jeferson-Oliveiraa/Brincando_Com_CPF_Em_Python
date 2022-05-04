#Validador
while True:
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for x in range(19):
        if x > 8:
            x -= 9

        total += int(novo_cpf[x]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not sequencia:
        print(f'O CPF {novo_cpf} é válido')
    else:
        print(f'O CPF {novo_cpf} é inválido')