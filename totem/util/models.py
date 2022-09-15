from contextlib import contextmanager
import pymysql.cursors
from datetime import date, datetime, timedelta     
#Importanto funções para trabalha em banco de dados 
#pip install pymysql

@contextmanager #gerenciador de contexto
def connect_server(): # função conectar banco
    conexao = pymysql.connect(
        host='192.168.2.8',
        user='totem',
        password='fundosaude@2021',
        db='database_att',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try: #Tratamento de exeções
        yield conexao 
    finally: #Executa independente da exeção 
        conexao.close() #Finaliza conexão

def verificar_filaEspera():
    data = date.today()
    tabela = 'fila_espera'
    with connect_server() as conn:
        with conn.cursor() as cursor:
            if  cursor.execute(f'SELECT data FROM {tabela} WHERE id IN (SELECT MAX(id) FROM {tabela});')>0:
                last_date = datetime.strptime(str(cursor.fetchone()['data']), '%d/%m/%Y').date()
                print(f'{data}\n{last_date}')
                if last_date < data:
                    cursor.execute(f'TRUNCATE TABLE {tabela};')
                    conn.commit()