"""
While >>> Utilizada quando se sabe a quantidade de repetições e
quando não se sabe.
* Necessário atentar para o critério de parada.

Sintaxe >>>  while expressão_bool:
                    Execução.

Expressão será executada enquanto for verdadeira.
Expressão Booleana >>> Toda expressão onde o resultado
for Verdadeiro ou Falso.

Ex.
resposta = ''
    while resposta != 'SIM':
            resposta = 'input'
"""








# # repetindo um texto 5 vezes com for
# for cont in range(5):
#     print(f'{cont}->batata')
# # repetindo um texto 5 vezes com while
# print()
# numero=0
# while numero<5:
#     print(f'{numero}->frita')
#     numero= numero + 1
# validando uma senha de forma simples
senha_cadastrada = str(input('cadastre uma senha:'))
senha_entrada=''


while senha_entrada != senha_cadastrada:
    senha_entrada = str(input('Digite sua senha:'))

print('\n Acesso permitido...')   

