from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero
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

print(f'{novo_cpf}')