"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:
______________________________________________
| Menor que 18.5      | Abaixo do peso       |
| Entre 18.5 - 24.9   | Peso Normal          |
| Entre 25.0 - 29.9   | Excesso de peso      |
| Entre 30.0 - 34.9   | Obesidade classe I   |
| Entre 35.0 - 39.9   | Obesidade classe II  |
| Maior ou igual 40.0 | Obesidade classe III |
----------------------------------------------

Mostre também a data deste resultado.
"""

nome= str(input('Digite seu nome:\n')).title()
idade=int(input(f'Olá {nome} Digite sua idade :\n'))
peso=float(input('Digite seu peso com ate duas casas decimais, exemplo 70.00:   \n '))
altura=float(input( 'Digite sua altura com ate duas casas decimais, exemplo 1.70:  \n  '))

imc= peso/altura**2


if (imc <= 18.5):
    Resultado= 'Abaixo do peso'

elif imc >= 18.5 and imc< 25:
    Resultado= 'Peso normal'

elif (imc>= 25.0) and ( imc < 30):
    Resultado= 'Excesso de peso'

elif (imc>= 30.0) and (imc<35):
    Resultado='Obesidade 1'

elif (imc>= 35.0) and (imc<40):
    Resultado='Obesidade 2'

elif (imc>= 40.0): Resultado='Obesidade 3'   
else:
     Resultado='valores de altura ou peso inválidos'

print(f'\n {nome} Seu Imc é:{imc}\n De acordo com seu Imc você está com: {Resultado}')
print(str(1.94).replace('.',','))



