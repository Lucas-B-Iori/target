n1 = 0
n2 = 1
n3 = n1 + n2
num_digitado = int(input("Digite um numero inteiro: "))
fazParte = False
if num_digitado == n1 or num_digitado == n2:
    fazParte = True

while n3 <= num_digitado:
    aux = n3
    n1 = n2
    n3 += n2
    n2 = aux
    if num_digitado == n3:
        fazParte = True
        break

if fazParte:
    print(f"O numero {num_digitado} faz parte da sequencia")
else:
    print(f"O numero {num_digitado} não faz parte da sequencia")
