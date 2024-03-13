#Desafio Estágio Ribeirão Preto
#1)
indice = 13
k = 0
soma = 0

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)

#2)
number = int(input("insira o numero que deseja saber se pertence a sequencia fibonacci: "))

a = 0
b = 1
fibo = [a, b]

while a < number:
    c = a + b
    a = b
    b = c
    fibo.append(c)

print(fibo)
if number in fibo:
    print(f"{number} é um numero da sequencia fibonacci")
else:
    print(f"{number} não é um numero da sequencia fibonacci")

#5)

palavra = input("insira a palavra que deseja inverter: ")

lista_palavra = list(palavra)
x = len(lista_palavra)
palavra_invertida = []

for i in range(x):
    a = (i + 1) * - 1
    letra = lista_palavra[a]
    palavra_invertida.append(letra)


print(palavra_invertida)
palavra = "".join(palavra_invertida)
print(palavra)

