"""
Vamos iniciar um programa que receba:
 nome
 idade
 peso
 altura
 

Retorne o IMC do usuário.

IMC =   Peso
      --------
       Altura²
"""


nome= str(input('Digite seu nome:')).title()
idade=int(input(f'olá{nome} Digite sua idade :'))
peso=float(input('Digite seu peso:'))
altura=float(input( 'Digite sua altura:'))

imc= peso/altura**2
print (f'Olá {nome}, seu imc resultou:{imc}')
print (f'Olá {nome}, seu imc resultou:{imc:.2f}')# formatação buscando apenas 2 casas decimais

print (f'Olá {nome}, seu imc resultou:{round(imc, 2)}') # mesma coisa mas sem o :.



