<<<<<<< HEAD
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
=======
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
>>>>>>> c1c51330ed6477b7f729fd9e97ad68f3c53255be
    