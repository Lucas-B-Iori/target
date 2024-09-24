frase = input("Digite uma frase: ")
qtdA = 0

frase = frase.lower()

for i in range(len(frase)):
    if frase[i] == 'a':
        qtdA += 1

print(f"Quantidade de vezes que a letra 'a' aparece na frase digitada: {qtdA}")