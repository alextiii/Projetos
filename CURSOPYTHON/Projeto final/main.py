#### importando bibliotecas
import pandas as pd
import re
import os
import smtplib
import openpyxl
import email
import pywhatkit as kit
import pyautogui
from time import sleep 
from email.message import EmailMessage


class To_do:

    def  inciar(self):
        self.listar_tarefas =[]
        self.email_destino()
        self.menu()
        self.criar_planilha()
        sleep(2)
        self.enviar_email()
        sleep(3)
        self.confirmar_por_whats()


    def email_destino(self):

        while True:
            self.email = str(input('Email de destino:')).lower()

            Padrao_email = re.search(
            '[a-z0-9._-]+@[a-z0-9]+.[a-z]?.[a-z]', self.email
            )
            
            if Padrao_email:
                print ('Email válido')
                break
            else:
                print('Email inválido')    

        
    def menu(self):
        while True:
            try:
                Menu = int(input('''
                MENU
                [1] CADASTRAR
                [2] VISUALIZAR
                [3] SAIR
                Opção: '''))

                match Menu:
                    case 1 : self.cadastrar_tarefas()
                    case 2 : self.visualizar_tarefa()
                    case 3 : break
                    case _: print('Opção inválida!')
            
            except ValueError:
                print('\033[41m\n Opção inválida, escolha um número de 1 a 3!\033[m')

    def cadastrar_tarefas(self):
        while True:
            self.tarefa=str(input('Tarefa ou [S] para sair: ')).capitalize()

            if self.tarefa =='S':
                break
            else:
                self.listar_tarefas.append(self.tarefa)
                try:
                    with open('.CURSOPYTHON\Projeto final\src\Tarefas.txt','a', encoding='utf8') as arquivo:
                        arquivo.write(f'{self.tarefa}\n')
                except FileNotFoundError as erro_no_arquivo:
                    print(f'Erro: {erro_no_arquivo}')        

    def visualizar_tarefa(self):
        try:
            with open('./CURSOPYTHON\Projeto final\src\Tarefas.txt','r', encoding='utf8') as arquivo_visual:
                print(arquivo_visual.read())
        except FileNotFoundError as erro_no_arquivo:
                    print(f'Erro: {erro_no_arquivo}') 

    def criar_planilha(self):
        if len(self.listar_tarefas)> 0:
            try:
                df = pd.DataFrame({'Tarefas': self.listar_tarefas})
                self.nome_arquivo = str(input('nome da planilha (Sem .XLSX): '))
                df.to_excel(f'.CURSOPYTHON\Projeto final\src\Tarefas/{self.nome_arquivo}.xlsx', index=False)

            except Exception as e:
                print(f'Erro:{e}')    

    def enviar_email(self):
        endereco = 'leleex.com.br@gmail.com'
        with open('./src/Senha/senha.txt') as arquivo:
            s= arquivo.readlines()
        senha=s[0]    

        msg = EmailMessage()
        msg['Subject'] = 'Planilha de tarefas...'
        msg['From'] = endereco
        msg['To'] = self.email

        msg.set_content('Oi zé, sua planilha de email,')

        arquivos = [f'.CURSOPYTHON\Projeto final\src\Tarefas{self.nome_arquivo}.xlsx']

        for item in arquivos:
            with open(item,'rb') as arq:
                dados = arq.read()
                nome_arquivo = arq.name

            msg.add_attachment(
                dados,
                maintype = 'application',
                subtype = 'octet-stream',
                filename = nome_arquivo
            )
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(endereco, senha, initial_response_ok= True)
        server. send_message(msg)
        print('Email enviado com sucesso!')

    def confirmar_por_whats(self):
        try:
            numero_telefone = '+5511958315173'

            mensagem = 'Falaaa ai mano, mandei o email lá!'
            sleep(3)
            kit.sendwhatmsg_instantly(numero_telefone,mensagem,wait_time=20)
            print('Mensagem enviada com sucesso.')
        except Exception as e:
            print(f'Erro:{e}')    









Start=To_do()
Start.inciar()       

