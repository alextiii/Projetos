"""
IF, ELSE, ELIF
Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Sintaxe:

if (teste):
    Bloco que será executado se o teste retornar True
"""

# if 10<20:  usar : para criar um bloco ate acabar o codigo
#     print('Menor')

'''
Exemplo de aplicação: 
Inserindo uma nota e testando as seguintes condições.
Se a nota for maior ou igual a 7 >>> O aluno está APROVADO.
Se a nota for menor que 7 e maior ou igual a 5 >>> o aluno está em RECUPERAÇÃO.
Se a nota for menor que 5 >>> o aluno está REPROVADO.
'''

# Condição simples
# media = 7.0
# if media >= 7.0:
#     print('Aprovado')
# else:
#     print ('Reprovado!')

# Condição composta
# media= 5.4
# if media >= 7.0:
#     print('Aprovado!')
# elif media>= 5:
#     print('Em recuperação!')
# else:
#     print('Reprovado!')   
# #sempre colocar o and para ninguem colocar um -9999.10
#     media= 9
# if media >= 7.0:
#     print('Aprovado!')
# elif media>= 5:
#     print('Em recuperação!')
# else:
#     print('Reprovado!') 

#     # no caso de negativos, colcoar condições
# media2= -9
# if (media2 >=5) and (media2 <7):
#     print('Em recuperação')

# elif (media2 >=7) and (media2 <=10):
#     print ('Aprovado')

# elif (media2 >=0) and (media2 <5):
#     print('Reprovado')
# else:
#     print ('média inválida')

    

# Condição aninhada
''' Vamos criar um sistema para validadar se o cliente
pode ou não ter uma Habilitação de acordo com a idade 
que irá informar.
'''
# idade= int(input('Digite sua idade') )
# if (idade >= 18 ):
#     print('CNH OK')
# elif (idade >16 and idade <18):
#     print ('precisa de autorização')
# elif (idade <16 and idade>=0):
#     print ('não pode seguir')
# else:
#     print('idade invalida')

    ###################
idade2= int(input('Digite sua idade') )
if (idade2 >= 18 and idade2 <60 ):
    print('CNH OK')
elif (idade2 >= 16 and idade2 <18)or (idade2>60 and idade2 <120):
    resposta = str(input('tem autorização? [n / s]:')).lower()
    if resposta == 's':
        print('Podemos seguir')
    elif resposta == 'n': 
        print('não podemos seguir') 
    else:
        print('resposta invalida')     
elif (idade2 <16 and idade2>=0):
    print ('não pode seguir')
else:
    print('idade invalida')


# idade >18 -> cnh ok
# idade >16 -> precisa de autorização
# idade <16 -> não pode seguir

# Operadores unitários >>> Dependem de um único valor >>> not, is
# Operadores binários >>> Dependem de mais que 1 valor >>> and, or



