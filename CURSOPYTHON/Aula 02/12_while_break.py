"""
While com Break
while True: >>> este laço será executado enquanto 
não encontrar o Break pelo caminho.
Break >>> Condição de parada de um loop. (FLAG)
"""
# sintaxe
# Validando tipo de dado com break
while True:
    menu = str(input("\n[1]SOMAR,\n[2]SUBTRAIR, \n[3]Multiplicar, \n[4]Dividir, \n[s]sair \n opção:"))
    if menu.lower() == 's':
        menu= 5
    elif menu not in '1234':
        print('DADO INVÁLIDO')
    
    else:
        menu=int(menu)

        n1= int(input('Digite um número: '))
        n2= int(input('Digite um número: '))
    match menu:
       
        case 1:
            print(f'Somando valores, temos:{n1+n2}')        
        
        case 2:
            print(f'Subtraindo valores, temos : {n1-n2}')

        case 3:
            print(f'multiplicando valores, temos:{n1*n2}')  

        case 4:
            print(f'Dividindo valores, temos:{n1/n2}')      

        case 5:
            break

           