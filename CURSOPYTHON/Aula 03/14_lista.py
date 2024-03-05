"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

* SORT >>> Ordena os dados de uma lista.
* REVERSE >>> Inverte a lista.
* APPENDD >>> Atribui a lista, um elemento por vez. Podendo ser inclusive outra lista...
* INSERT >>> Atribui vários elementos, integrando à lista original.
* POP >>> Remove um valor da lista por índice.
* REMOVE >>> Remove um valor da lista por valor.
* ENUMERATE >>> Acesso à chave e valor.
* SHALLOW COPY
* CLEAR >>> Limpa a lista.
"""
# # print(numeros)
# # print(max(numeros))
# # print(min(numeros))
# # print(len(numeros))
# # print(sum(numeros))
# # print(sum(numeros)/ len(numeros))

# numeros.sort()
# print(numeros)
# numeros.reverse()
# print(numeros)
# nomes=[]
# for cont in range(3):
#     nome=str(input(f'{cont+1}nome:')).title()

#     nomes.append(nome) # append seria um insert na variavel nomes porem so pode adicionar um de cada vez e sem posição
# print(nomes)    

# num=[9,7,1,4,3]
# num.append(10)
# num.insert(1,'leo')
# num.pop()# remove a ultima posição
# num.pop(1)# remove a posição 1
# num.remove('leo')# removo como um filtro
# num.clear# limpar a lista
# print(num)
#################################################################################
# for indice,numero in enumerate(num):
#     if indice >=2:
#         print(f'posição: {indice} / Elemento: {numero}')




a=[1,2,3]
b = a  # recebe a  e os dois ficam conectadas para sempre
b=a [:]  # recebe a conteudo mas nao fica conectada
b.append(100)
print(f'lista A: {a}')
print(f' lista B: {b}')