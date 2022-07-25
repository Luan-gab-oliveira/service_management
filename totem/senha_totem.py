import pymysql.cursors
from contextlib import contextmanager

opc = 0
atendimento = 0

@contextmanager #gerenciador de contexto
def startserver(): # função conectar banco
    conexao = pymysql.connect(
        # host='127.0.0.1',
        host='192.168.2.106',
        #host='localhost',
        user='root',
        password='',
        db='database_att',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try: #Tratamento de exeções
        yield conexao 
    finally: #Executa independente da exeção 
        conexao.close() #Finaliza conexão

tabela = 'fila_espera'

# Acumuladores
next_service = 0

# Lista de opções
while opc != 6: # Executa laço enquanto o input for diferente de 6. [sair]
    while atendimento < 1 or atendimento > 2: #Executa laço até que o input seja igual a 1.[Preferencial] ou  2.[Convencional]

            atendimento = int(atendimento)
    opc = int(opc)
    if opc > 0 and opc <=5 : 
        if opc == 1:
            senha = 'TFD' #22
            opc = 'TFD'
        elif opc == 2:
            senha = 'PRE' #3
            opc = 'PREMIR'
        elif opc == 3:
            senha = 'FAE'
            opc = 'FARM.E'
        elif opc == 4:
            senha = 'FAA' #4
            opc = 'FARM.A'
        elif opc == 5:
            senha = 'AUT' #21
            opc = 'AUT.EXAMES'
        
        data = '02/05/2022'

        if atendimento == 1:
            senha = 'P' + senha
            atendimento = 'preferencial'
        else:
            atendimento = 'convencional'

        with startserver() as conexao: #chama a função para conectar ao banco mysql
            with conexao.cursor() as cursor:
                #caso exista uma sequencia para a opção selecionada na consulta, gera uma senha sequencial.
                if  cursor.execute(f'SELECT senha FROM {tabela} WHERE opcao = "{opc}" AND id IN (SELECT MAX(id) FROM {tabela} WHERE atendimento = "{atendimento}");')>0: #realiza consulta em banco
                    resultado = str(cursor.fetchone()['senha']) #retorna resultado da consulta

                    if atendimento == 'preferencial': #Preferencial
                        resultado = int(resultado[4:])+1 #converte o resutado, fatiando apenas os valores
                    else: # Convencional
                        resultado = int(resultado[3:])+1 #converte o resutado, fatiando apenas os valores

                    resultado = str(resultado).rjust(3,'0') # adiciona 3 digitos ao resultado
                    senha = senha + str(resultado) #seta senha
                    sql = f"INSERT INTO {tabela} (opcao, atendimento, senha, dataAtual) VALUES ('{opc}','{atendimento}','{senha}','{data}')" #seta intrução sql
                
                else: #caso não exista uma sequencia para a opção selecionada na consulta, gera uma nova senha no bloco else. 
                    senha = senha + str('001') #seta senha
                    sql = f"INSERT INTO {tabela} (opcao, atendimento, senha, dataAtual) VALUES ('{opc}','{atendimento}','{senha}','{data}')" #seta intrução sql

                cursor.execute(sql) #executa instrução sql
                conexao.commit() #commit para o interprertador entender que deve executar a instrução
                print(f'Sua senha: {senha}') # imprime senha

print('Encerrando ...')