from Modulos import *
from startserver import *
from parametros import *

###Função para conectar ao servidor###
def gerar_senha(self):
    global senha, opc, atendimento, senhal
    with startserver() as conexao: #chama a função para conectar ao banco mysql
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
            
            print(senha)