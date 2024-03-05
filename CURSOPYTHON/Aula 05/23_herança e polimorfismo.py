"""  
HERANÇA é um tipo de relacionamento entre classes 
que significa que uma classe é outra.

POLIMORFISMO é a capacidade que uma subclasse tem de 
ter métodos com o mesmo nome de sua superclasse, e o 
programa saber qual método deve ser invocado, 
especificamente (da super ou sub). 
"""

"""
Uma classe é um modelo ou blueprint que descreve os atributos (variáveis) 
e comportamentos (métodos) comuns a um grupo de objetos relacionados. 

No contexto da orientação a objetos, uma classe funciona como uma base 
para criar instâncias, chamadas de objetos. Cada objeto criado a partir 
de uma classe possui os atributos e métodos definidos pela classe, 
mas com valores e estados específicos. 
"""
#herança
class Pessoa:
    def __init__(self,nome,email,cpf,idade):
        self._nome = nome
        self._email=email
        self._cpf=cpf
        self._idade=idade
    def getAll(self):
        return[self._nome,self._email,self._idade]
    

# Criar uma classe cliente   
class Cliente(Pessoa):
    def __init__(self,nome,email,cpf,idade,rg):
        super().__init__(nome,email,cpf,idade)
        self._rg=rg

    
class FUNCIONARIO(Pessoa):
    def __init__(self,nome,email,cpf,idade,matricula):
        super().__init__(nome,email,cpf,idade)
        self ._matricula=matricula
    def getAll(self):
        return[self._nome,self._email,self._matricula] # metodo polimorfismo retorno o que eu quero
        #até mesmo uma mensagem assim :return'ola mundo'#

client1= Cliente('Leonardo','leo@email.com',133,586059064,22)       
FUNC1= FUNCIONARIO('ALEX','LELEEX.COM.BR@GMAIL.COM',51543445888,22,150)
print(f'{client1.getAll()}\n {FUNC1.getAll()}') 
     

