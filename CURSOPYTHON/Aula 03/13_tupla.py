"""
Tuplas >>> Tuple

Tuplas não são mutáveis, uma vez criada, permanecerá tal qual durante do o código.
- Aceita assim como as listas, quaisquer tipos de dados.

Sintaxe's
variável = ()
variável = tuple()

Tuplas são definidas por , e não por uso de parenteses.

Métodos de adição, remoção, alteração, ordenação em tuplas não existem.

Utilizamos em coleções que não sofrem alterações.
"""

# Criando uma tupla
# tupla1=()
# tupla2=tuple() # PARA USAR RANGE, LEMBRANDO QUE NAO TEM COMO MODIFICAR

# dias_semana= ('Segunda','terça','quarta','quinta','sexta','sabado','domingo')
# print(dias_semana[1])

# for batata in dias_semana:
#     print(f'DIA-> {batata}')

numeros= tuple(range(11))

print(numeros)
print(max(numeros))
print(min(numeros))
print(len(numeros))
print(sum(numeros))
print(sum(numeros)/ len(numeros))

