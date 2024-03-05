"""
Uma classe é um modelo ou blueprint que descreve os atributos (variáveis) 
e comportamentos (métodos) comuns a um grupo de objetos relacionados. 

No contexto da orientação a objetos, uma classe funciona como uma base 
para criar instâncias, chamadas de objetos. Cada objeto criado a partir 
de uma classe possui os atributos e métodos definidos pela classe, 
mas com valores e estados específicos. 
"""

# Criar uma classe cliente   
class Cliente:
    def __init__(self,nome,email,cpf,rg,idade):
        self._nome = nome
        self._email=email
        self._cpf=cpf
        self._rg=rg
        self._idade=idade

    def getEmail(self):
        return[self._nome,self._email]    
client1= Cliente('Leonardo','leo@email.com',133,586059064,22)
c=client1.getEmail()
print(c)



class FUNCIONARIO:
    def __init__(self,nome2,email2,cpf2,idade2,matricula2):
        self ._nome2=nome2
        self ._email2=email2
        self ._cpf2=cpf2
        self ._idade2=idade2
        self ._matricula2=matricula2

    def get(self):
        return[self._nome2,self._email2,self._idade2]
FUNC1= FUNCIONARIO('ALEX','LELEEX.COM.BR@GMAIL.COM',51543445888,22,150)
exibir=FUNC1.get() 
print(exibir) 
    