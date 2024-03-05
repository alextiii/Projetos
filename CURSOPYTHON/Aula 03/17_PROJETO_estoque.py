"""
Cadastre 3 produtos no estoque, cada produto precisa ter:
- nome
- preço
- data e hora que foi cadastrado
- Nome do Funcionário

Em seguida, permita que os produtos sejam visualizados.
"""
estoque=[]
from datetime import datetime
while True:
    menu = int(input("\n[1]CADASTRAR,\n[2]VISUALIZAR, \n[3]SAIR\n Opção:\n"))
    match menu:
       
        case 1:
            produto=dict(
                nome=str(input('Digite seu nome: ')).title(),
                preco=float(input('Digite o preço: ')),
                dt_cadastro= datetime.now().strftime("%d . %m . %Y | %H:%M"),
                funcionario=str(input('Digite o nome do funcionário: ')).title())    
            estoque.append(produto)

        case 2:
            
            for produto in estoque:
                for chave,valor in produto.items():
                    print(f'{chave} → {valor}')
                    print()

        case 3:
            break
        case _:
            print('\n invalido')           

            

        


          
    
        