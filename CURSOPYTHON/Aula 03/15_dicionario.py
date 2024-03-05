# """
# Dicionários - Em outras linguagens, conhecido como MAPA.

# Sintaxe
# exemplo1 = {}
# exemplo2 = dict()

# Aceita qualquer tipo de dado.
# As chaves não podem ser repetidas.
# """
# dicionario1={}
# dicionario2= dict()

# dicionario3= {'chave ': 'valor'}
# dicionario4= dict(batata='frita')

# paises = dict (
#     br='brasil',
#     us='eua',
#     py= 'paraguai'
# )

# paises['ar'] = 'Argentina'  # Alter o brasil para argentina

# print(paises)
# # print(paises.keys())  #so chave
# # print(paises.values()) # so valores

# # print(paises['br'])

# # print(paises['br'])

# # for c,v in paises.items():
# #     print(f'chave: {c} / valor: {v}')

usuarios=[]

for cont in range(3):
    user=dict(
        nome=str(input('nome:')),
        email =str(input('email:'))
    )

    usuarios.append(user)
for u in usuarios:  
    for chave,valor in u.items():
        print(f'{chave} --->{valor}')  




