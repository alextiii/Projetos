# Sets

# tupla= ()
# tupla 2 = tuple()

# lista1 =[]
# lista2=[]

# dicionario1={'chave':'valor'}
# discionario2= dict(chave='valor')

# conjunto1={}
# conjunto2= set()

# exemplo set
# numero= {1,2,3,4,5}


# exemplo dict

# numero{'valor':123}





# Analise cidades (cada pessoa que entrou colocou a cidade de nascimento)
cidade = ['Rio de Janeiro', 'São Paulo', 'Juiz de Fora', 'Petrolina',
          'Salvador','Juiz de Fora', 'Rio de Janeiro', 'Petrolina',
          'Salvador', 'São Paulo', 'São Paulo', 'São Paulo',  'Juiz de Fora',
          'Rio de Janeiro', 'Petrolina', 'Rio de Janeiro', 'Salvador',
          'Juiz de Fora',  'Petrolina', 'Salvador', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo',
          'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro',  'São Paulo', 'Rio de Janeiro',
          'São Paulo', 'Rio de Janeiro', 'São Paulo']

# total de pessoas que vieram hoje

# print(f'Total de visitantes: {len(cidade)}')

# #total de pessoas que vieram do Rj
# print(f'Total de pessoas do Rj:{cidade.count("Rio de Janeiro")}  ')

# #total de cidades que

# print(f'total de cidades: {len(set(cidade))}')

# d=dict(a=10)
# num={1,2,3}
# cidade.append('santos') #adiciona em lista
# num.add(6)              #adc em conjunto
# d['b']=20               #adc em dicionario
# d.update({'a':40, 'j':50}) # adc em dicionario porem podendo inserir 1 ou mais chaves e valores

# num.discard('batata') # ele removo e se caso nao tiver batata ele ignora e printa o que tem


Curso_Py= {'Léo A','Maria B','juca c','Beto B','Ana C'}
Curso_Bd= {'Joaquim M', 'Sandra S', 'Léo A', 'Ana C'}

#Total de alunos no curso de python
# print(f'Total de alunos em Python:{len(Curso_Py)}')

#Total de alunos no curso de Banco de dados
# print(f'Total de alunos em Python:{len(Curso_Bd)}')

# total de alunos na escola  UNIÃO -union
tot_alunos= Curso_Py.union(Curso_Bd) 
Tot_alunos2= Curso_Py| Curso_Bd    #### são iguais ( sempre serão removidos dados duplicados e unificar em um conjunto final)



## total de pessoas em ambos os cursos
ambos_cursos1=Curso_Py.intersection(Curso_Bd)
ambos_cursos2= Curso_Py& Curso_Bd


#### total de alunos em python que não estão fazendo banco de dados 
so_python= Curso_Py.difference(Curso_Bd)


### total de alunos apenas em Banco que não estao em python
So_bancodedados=Curso_Bd.difference(Curso_Py)
print(f'Total de alunos em Python:{len(Curso_Py)}')
print(f'Total de alunos em Python:{len(Curso_Py)}')
print(f'Total de alunos em Python:{len(Curso_Bd)}')
print(f'Total de alunos:{len(tot_alunos)}')
print(f'Total de alunos em ambos os cursos: {len(ambos_cursos1)}')
print(f'Total de alunos que estão em Python e não estã em Bd:{len(so_python)}')
print(f'Total de alunos que estão em Banco de dados e não estã em Python:{len(So_bancodedados)}')
