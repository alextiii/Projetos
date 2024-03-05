# def entrada_dados():
#     nome= str(input('Digite seu nome:')).title()
#     idade=int(input(f'olá {nome} Digite sua idade :'))
#     peso=float(input('Digite seu peso:'))
#     altura=float(input( 'Digite sua altura:'))

#     return[nome,idade,peso,altura]
# def imc(dados):

#     imc =dados[2]/dados[3]**2 
#     return imc
# print(imc(entrada_dados()))
# como dic
def entrada_dados():
    nome= str(input('Digite seu nome:')).title()
    idade=int(input(f'Olá {nome} Digite sua idade :'))
    peso=float(input('Digite seu peso:'))
    altura=float(input( 'Digite sua altura:'))

    return dict(
        nome=nome,
        idade=idade,
        peso=peso,
        altura=altura
    )
def imc(dados):
    dados['imc'] = dados ['peso'] / dados['altura'] ** 2
    return dados

def imprimir_resultado(dados_completos):
    return f'Olá {dados_completos["nome"]},o seu imc resultou :{dados_completos["imc"]}'
    
  



# nome= str(input('Digite seu nome:')).title()
# idade=int(input(f'olá{nome} Digite sua idade :'))
# peso=float(input('Digite seu peso:'))
# altura=float(input( 'Digite sua altura:'))

# imc= peso/altura**2
# print (f'Olá {nome}, seu imc resultou:{imc}')
# print (f'Olá {nome}, seu imc resultou:{imc:.2f}')# formatação buscando apenas 2 casas decimais
# print (f'Olá {nome}, seu imc resultou:{round(imc, 2)}') # mesma coisa mas sem o :.
