"""
Parâmetros X Argumentos
"""




# def dizer_Oi():
#     return('Oi')

# # Função canta parabéns
# def dizer_parabens(nome_aniversariante):
#     return f'{nome_aniversariante},Parabéns para você'.title()
   
# # Função soma 2 valores
# def somar2valores():
#     valor1=int(input(f'Digite um valor:'))
#     valor2=int(input(f'Digite o segundo valor:'))
#     return((valor1)+(valor2))


# nome=str(input('nome:')).title()
# print(dizer_parabens(nome))

# def somardoisvalores(valor1,valor2):
#     return f'soma dos valores são: {valor1+valor2}'

# valor1=int(input(f'Digite um valor:'))
# valor2=int(input(f'Digite o segundo valor:'))
# print(somardoisvalores(valor1,valor2))


def recebe_valores():
    numeros=[]
    while True:
        menu = int(input('[1Mais [2]Sair | Opção:'))
        if menu ==1:
            numeros.append(int(input('números:')))
        elif menu ==2:
            break
        else:
            print('Opc inválida...')
    return numeros
def somar(lista_numeros):
    return sum(lista_numeros)

print(somar(recebe_valores()))            