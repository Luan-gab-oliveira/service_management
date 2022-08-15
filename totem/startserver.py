from Modulos import *

@contextmanager #gerenciador de contexto
def startserver(): # função conectar banco
    conexao = pymysql.connect(
        host='192.168.2.8',
        user='sms',
        password='',
        db='database_att',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try: #Tratamento de exeções
        yield conexao 
    finally: #Executa independente da exeção 
        conexao.close() #Finaliza conexão
    