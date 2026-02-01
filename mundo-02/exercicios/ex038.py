"""
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:

> O primeiro valor é MAIOR
> O segundo valor é MAIOR
> Não existe valor maior, os dois são iguais
"""

valor1 = int(input('Digie um valor: '))
valor2 = int(input('Digite outro valor: '))

maior = valor1
if maior > valor2:
    print('O primeiro valor é MAIOR')
elif valor2 > maior:
    print('O segundo valor é MAIOR')
else:
    print('Não existe valor MAIOR, os dois são iguais!')
print('Fim do programa')
