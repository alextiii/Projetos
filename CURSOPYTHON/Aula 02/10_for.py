"""
For >>> Utilizada quando se sabe a quantidade de repetições,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe:
for item in iteravel:
    bloco que será executado

* Range -> inicio, fim, passo
* Enumerate -> Permite acesso ao índice
"""

# # sintaxe
# for contagem in range(0,10,1):
#     print(contagem, end=' ')











'''
Desafio de aula: Crie um sistema que receba 4 notas 
e calcule a média, ao fim apresente a média e situção
do aluno, sendo:
>7 aprovado, >5 em recuperação e <5 reprovado.
'''
# soma= 0
# for contagem in range(1,5):
#     print (f'soma: {soma}')
#     nota= float(input(f'Digita a {contagem}º nota:'))

#     # soma= soma+nota
#     soma+=nota  #forma mais utilizada

# print(f'\n  Média :{soma/contagem}')    

soma=0

for cont in range (1,4):
    nome= str(input('Digite seu nome:')).title()
    idade=int(input('Digite a sua idade:'))
    soma+=soma+idade
print(f'a soma é{soma}')    
print(f'\n média :{soma/idade}')   

    