"""
Primeiro passo para leitura, é abrir o arquivo, para isto usamos
a função OPEN(nomeArquivo).
O parâmetro é o nome ou caminho do arquivo.

O arquivo deve existir, caso contrário retornará erro FileNotFound.

Open apenas abre o arquivo, para ler seu conteúdo é necessário usarmos
a função nomeArquivo.read()
Por padrão o Open abre com o parâmetro r(read)
"""

# criando um arquivo txt
# a -> adc w -> sub r -> leitura (pode ser suprimido)
# tratamento de erro

with open('teste.txt','w', encoding='utf8')as arquivo:
    arquivo.write('Só estou testando...\n')


try:
        with open('test.txt','r', encoding='utf8')as arquivo2:
            print(arquivo2.read())  

except FileNotFoundError:
      print('Arquivo não encontrado...')

finally:
      print('Volte sempre!')      


# Exercício de aula: criar um todo (lista de tarefas)

      
