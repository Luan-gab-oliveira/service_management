import os
from util.models import *
from util.modules import *

document = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []

get_dir = os.path.dirname(__file__)
count = 0

def consulta(mes, nome):
    global res, rel_att, setor, mes_nome, nome_func, soma
    mes_nome = mes
    nome_func = nome
    soma = 0
    config = ConfigParser()
    get_dir = os.path.dirname(__file__)
    config.read(fr'{get_dir}\settings.ini')
    server_config = dict(config['server'])
    setor = server_config['setor']
    
    if mes_nome == 'Janeiro':
        mes_num = "{0:02d}".format(1)
    elif mes_nome == 'Fevereiro':
        mes_num = "{0:02d}".format(2)   
    elif mes_nome == 'Março':
        mes_num = "{0:02d}".format(3)  
    elif mes_nome == 'Abril':
        mes_num = "{0:02d}".format(4)  
    elif mes_nome == 'Maio':
        mes_num = "{0:02d}".format(5)  
    elif mes_nome == 'Junho':
        mes_num = "{0:02d}".format(6)  
    elif mes_nome == 'Julho':
        mes_num = "{0:02d}".format(7)  
    elif mes_nome == 'Agosto':
        mes_num = "{0:02d}".format(8)  
    elif mes_nome == 'Setembro':
        mes_num = "{0:02d}".format(9)   
    elif mes_nome == 'Outubro':
        mes_num = 10        
    elif mes_nome == 'Novembro':
        mes_num = 11       
    elif mes_nome == 'Dezembro':
        mes_num = 12     
    try:
        sql = f"SELECT data, atendimentos FROM atendimentos WHERE setor='{setor}' AND data LIKE '%/{mes_num}/%';"
        res = consulta_database(sql)
        if res == None:
            messagebox.showwarning('Atenção!',f"O mês selecionado não possui registro de atendimentos!")
        else:
            rel_att=[]
            for i in res:
                data = i['data']
                att = i['atendimentos']
                rel_att.append(f'{data:115}{att:5}')
                soma += int(att)
    except:
        pass

def mm2p(milimetros): #converte milimetros em pontos
    return milimetros/0.352777

def doc():
    global count
    data_name = datetime.now().strftime('%d%m%Y%H%M')
    data_doc= datetime.now().strftime('%d/%m/%Y - %H:%M')
    font_style = 'Helvetica'
    eixo = 190
    # inicializa canvas
    cnv = canvas.Canvas(fr'{get_dir}\..\doc\{mes_nome}{data_name}_{count}.pdf')
    cnv.drawImage(fr'{get_dir}\smssfs.jpeg' ,mm2p(0),mm2p(260),mm2p(210),mm2p(28)) 
    cnv.setFont(font_style, 16)
    cnv.drawCentredString(mm2p(110),mm2p(240), "Relatório de Atendimento Mensal")
    cnv.setFont(font_style, 12)
    cnv.drawCentredString(mm2p(55),mm2p(220), f"Setor: {setor}")
    cnv.drawCentredString(mm2p(165),mm2p(220), f"Mês de Ref: {mes_nome}")
    cnv.drawCentredString(mm2p(55),mm2p(200), "Data")
    cnv.drawCentredString(mm2p(165),mm2p(200), "Qtde de Atendimentos")
    cnv.drawCentredString(mm2p(110),mm2p(20), f"Emitido por: {nome_func}")
    cnv.drawCentredString(mm2p(110),mm2p(10), f"{data_doc}")

    cnv.drawCentredString(mm2p(110),mm2p(60), "_________________________________________________")
    cnv.drawCentredString(mm2p(110),mm2p(50), f"Total de Atendimentos em {mes_nome}: {soma}")
    cnv.drawCentredString(mm2p(110),mm2p(45), "_________________________________________________")
    # Gerar pdf senha  
    #  
    i = int(0)
    try:
        for txt in range(len(rel_att)):
            cnv.setFont(font_style, 10)
            cnv.drawCentredString(mm2p(110),mm2p(eixo), rel_att[txt])
            cnv.drawCentredString(mm2p(110),mm2p(eixo), "_________________________________________________________________")
            eixo -= (5+i)

        count += 1
        cnv.save()  
        messagebox.showinfo("Concluído", "O arquivo foi salvo com sucesso!")
    except:
        messagebox.showerror("ERRO", "A criação do Relatório não pode ser concluida!")