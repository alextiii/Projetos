"""
Variáveis:
Espaço na memória reservado para armazenar dados.
Não pode ser uma palavra reservada da linguagem.
Não pode conter espaço, para separa usamos _
Poder ser usado padrão CamelCase

Escopo:
Caso não seja declarada como global, a variável fica
disponível apenas dentro do escopo no qual foi criada.
"""

# correto
nome = 'Alex'
Idade= 22
Profissão= 'tecnologia'
print (nome,Idade,Profissão,'Seja Bem vindo ao seu curso de python')
intituição = input('Diga o nome da instituição')
nomecompleto= input('Digite seu nome completo')
print(nomecompleto,'seja Bem vindo a instituição',intituição)

#if e else teste alex#
if Idade>22 :
    print('Não achamos sua idade em nosso banco') 
else : Idade = 22
print :('Bem vindo',nome, 'sua idade esta correta')






