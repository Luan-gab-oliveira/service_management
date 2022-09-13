from util.models import *
from util.parametros import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
import win32print, win32api, os, threading

def mm2p(milimetros): #converte milimetros em pontos
    return milimetros/0.352777

def imprimir(senha, local): 
    try:
        txt_senha = senha
        txt_local = local   
        data = datetime.now().strftime('%d/%m/%Y %H:%M')
        texto_pdf = ['Atendimento','SENHA', txt_senha, 'LOCAL', txt_local, f'São francisco do Sul, {data}']
        font_style = 'Helvetica'
        font_size = [50,40,110,40,110,30]
        eixo = 210

        dir_app = os.getcwd()+ r'\totem\util\impressao'
        # dir_app = str(os.path.dirname(__file__))

        print(dir_app)

        senha_pdf = 'senha.pdf'
        # inicializa canvas
        cnv = canvas.Canvas(f'{dir_app}\{senha_pdf}', pagesize=A4)

        # carrega imagem de cabeçalho
        cnv.drawImage(f'{dir_app}\smssfs.jpeg' ,mm2p(0),mm2p(260),mm2p(210),mm2p(28)) 
        # Gerar pdf senha
        i = int(0)
        for txt in texto_pdf:
            cnv.setFont(font_style,font_size[i])
            cnv.drawCentredString(mm2p(110),mm2p(eixo), txt)
            eixo -= (35+i)
            i += 1
            
        threading.Thread(target= cnv.save()).start
        impressora = "ZDesigner_GC420d"
        win32print.SetDefaultPrinter(impressora)
        win32api.ShellExecute(0,"print",senha_pdf,None, dir_app,0)
    except:
        pass


###Função para conectar ao servidor###
def gerar_senha(self):
    global senha, opc, atendimento, senhal
    with connect_server() as conexao: #chama a função para conectar ao banco mysql
        with conexao.cursor() as cursor:
            #caso exista uma sequencia para a opção selecionada na consulta, gera uma senha sequencial.
            if  cursor.execute(f'SELECT senha FROM {tabela} WHERE id IN (SELECT MAX(id) FROM {tabela} WHERE opcao = "{opc}" AND atendimento = "{atendimento}");')>0: #realiza consulta em banco
                resultado = str(cursor.fetchone()['senha']) #retorna resultado da consulta
                if atendimento == "preferencial": #Preferencial
                    resultado = int(resultado[4:])+1 #converte o resutado, fatiando apenas os valores
                else: # Convencional
                    resultado = int(resultado[3:])+1 #converte o resutado, fatiando apenas os valores

                resultado = str(resultado).rjust(3,'0') # adiciona 3 digitos ao resultado
                senha = senha + str(resultado) #seta senha
                sql = f"INSERT INTO {tabela} (opcao, atendimento, senha, data, status) VALUES ('{opc}','{atendimento}','{senha}','{data}', 'ESPERA')"  #seta intrução sql
            
            else: #caso não exista uma sequencia para a opção selecionada na consulta, gera uma nova senha no bloco else. 
                senha = senha + str('001') #seta senha
                sql = f"INSERT INTO {tabela} (opcao, atendimento, senha, data, status) VALUES ('{opc}','{atendimento}','{senha}','{data}', 'ESPERA')"  #seta intrução sql
            
            threading.Thread(target= imprimir, args= (senha, opc)).start
            cursor.execute(sql) #executa instrução sql
            conexao.commit() #commit para o interprertador entender que deve executar a instrução

