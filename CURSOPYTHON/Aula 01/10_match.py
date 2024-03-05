menu= int(input('[1]somar \n[2] subtrair\n opção: '))
match menu:
    case 1:
        print(10+10)

    case 2:
        print(89-36)
    
    case _ :
        print('Opção inválida!')