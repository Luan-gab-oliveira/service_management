from util.gerar_senha import *
from util.espera import *

 ###Classe para Funções###
class func(espera):
    global opcao, setor, atendimento, opc, ref, set

    ###Função para aviso de HORARIO EXCEDENTE
    def horario_ex(self):
        global opcao, setor, atendimento, tela, opc, ref
        if hora_atual >= horario[0]:
            self.root_horario = tk.Toplevel() #Variavel para atribuir tela principal
            self.root_horario.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuir titulo a tela
            self.root_horario.configure(background= cores[2]) #Cor de fundo
            self.root_horario.geometry("1000x700") #Dimensões do tamanho da tela cheia
            self.root_horario.attributes('-alpha', 0.0)
            self.root_horario.resizable(False, False) #Negar o redimensionamento da tela
            self.root_horario.minsize(width=800, height= 500) #Definir tamanho minimo da tela   
            self.frame_horario =Frame(self.root_horario, bg = cores[0]) #Definindo um Frame para a tela 
            self.frame_horario.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 

            self.photo_horarios = PhotoImage(file= fr"{get_dir}\Plano de Fundo\Plano de Fundo horarios.png")
            self.logo_horarios = Label(self.frame_horario, image= self.photo_horarios, background= cores[0])
            self.logo_horarios.place(anchor="center", relx=0.5, rely=0.5)

            self.aviso = Label(self.frame_horario, text="A fila de espera para \neste Atendimento \nEXCEDE \no horario de atendimento", background= cores[0], foreground= "red")
            self.aviso.configure(font= tkFont.Font(family="Arial", size=45, weight="bold"))
            self.aviso.place(anchor='center', relx= 0.5, rely= 0.5)

            self.aviso2 = Label(self.frame_horario, text="Horario Atual:", background= cores[0])
            self.aviso2.configure(font= tkFont.Font(family="Arial", size=25))
            self.aviso2.place(anchor='center', relx= 0.5, rely= 0.8)

            self.aviso3 = Label(self.frame_horario, text= hora_atual, background= cores[0])
            self.aviso3.configure(font= tkFont.Font(family="Arial", size=25))
            self.aviso3.place(anchor='center', relx= 0.5, rely= 0.86)

            ###Código para janela abrir no meio da tela###
            self.root_horario.update_idletasks()
            width = self.root_horario.winfo_width()
            frm_width = self.root_horario.winfo_rootx() - self.root_horario.winfo_x()
            win_width = width + 2 * frm_width

            height = self.root_horario.winfo_height()
            titlebar_height = self.root_horario.winfo_rooty() - self.root_horario.winfo_y()
            win_height = height + titlebar_height + frm_width

            x = self.root_horario.winfo_screenwidth() // 2 - win_width // 2
            y = self.root_horario.winfo_screenheight() // 2 - win_height // 2
            self.root_horario.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            self.root_horario.deiconify()
            
            self.root_horario.attributes('-alpha', 1.0)
            self.root_horario.overrideredirect(True)
            self.root_horario.after(8000,self.root_horario.destroy)

        elif ref == 3:
            self.cartao_sus()  

        elif ref == 4:
            self.tfd()
    ###Funções de Fechamento de cada tela###
    def fechar_conv(self): #Função fechamento de tela Conv. do TFD, AUT, FAA, FAB, FAE, PRE
        global opcao, opc, atendimento, tela, setor, set
        atendimento = atend[1]
        threading.Thread(target=self.abrir_janela_espera())
        threading.Thread(target=self.gerar_senha).start()
        if tela == 2:
            self.rootCSUS.destroy() #Destruir janela 21
        elif tela == 1:
            self.rootTFD.destroy() #Destruir janela 2

    def fechar_prefe(self): #Função fechamento de tela Pref. do TFD, AUT, FAA, FAB, FAE, PRE
        global opcao, opc, atendimento, tela, setor, set
        atendimento = atend[0]
        opcao = 'P' + opcao
        threading.Thread(target=self.gerar_senha).start()
        self.abrir_janela_espera()
        if tela == 7:
            self.rootCSUS.destroy() #Destruir janela 21
        elif tela == 8:
            self.rootTFD.destroy() #Destruir janela 2


    def gerar_senha(self):
        global opcao, opc, atendimento, setor, set
        with connect_server() as conexao: #chama a função para conectar ao banco mysql
            with conexao.cursor() as cursor:
                #caso exista uma sequencia para a opção selecionada na consulta, gera uma senha sequencial.
                if  cursor.execute(f'SELECT senha FROM {tabela} WHERE id IN (SELECT MAX(id) FROM {tabela} WHERE opcao = "{opcao}" AND atendimento = "{atendimento}");')>0: #realiza consulta em banco
                    resultado = str(cursor.fetchone()['senha']) #retorna resultado da consulta
                    if atendimento == "preferencial": #Preferencial
                        resultado = int(resultado[4:])+1 #converte o resutado, fatiando apenas os valores
                    else: # Convencional
                        resultado = int(resultado[3:])+1 #converte o resutado, fatiando apenas os valores

                    resultado = str(resultado).rjust(3,'0') # adiciona 3 digitos ao resultado
                    senha = opcao + str(resultado) #seta senha
                    sql = f"INSERT INTO {tabela} (setor, opcao, atendimento, senha, data, status) VALUES ('{setor}','{opcao}','{atendimento}','{senha}','{data}', 'ESPERA')"  #seta intrução sql
                
                else: #caso não exista uma sequencia para a opção selecionada na consulta, gera uma nova senha no bloco else. 
                    senha = opcao + str('001') #seta senha
                    sql = f"INSERT INTO {tabela} (setor, opcao, atendimento, senha, data, status) VALUES ('{setor}','{opcao}','{atendimento}','{senha}','{data}', 'ESPERA')"  #seta intrução sql

                cursor.execute(sql) #executa instrução sql
                conexao.commit() #commit para o interprertador entender que deve executar a instrução
                imprimir(senha, setor)
                print(senha)

    ###Função Escolha Preferencial ou Convencional TFD###
    def abrir_janela_TFD(self): 
        global ref
        ref = 4
        self.horario_ex()
        
    def tfd(self):
        self.rootTFD = tk.Toplevel() #Variavel para atribuir tela principal
        self.rootTFD.configure(background= cores[0]) #Cor de fundo
        self.rootTFD.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
        self.fullScreenState = False
        self.frameTFD =Frame(self.rootTFD, bg = cores[0]) #Definindo um Frame para a tela 
        self.frameTFD.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96)  #Localizando o Frame na tela 
        global opcao, opc, atendimento, tela, setor, set
        opcao = opc[0]
        setor = set[0] 
        tela = 1
        
        #Imagens na Tela 
        self.fundo_TFD = PhotoImage(file= planos[1]) #Plano de fundo principal
        figura_fundo_TFD = Label(self.frameTFD, image= self.fundo_TFD, bd= 0) #Chamando imagem 
        figura_fundo_TFD.place(anchor= 'center',relx=0.5, rely=0.4, width= 500, height= 500) #Localizando a imagem na tela

        self.bt_conv_tfd = PhotoImage(file= bt[3]) #Chamando imagem 
        self.figura_bt_conv_tfd = Button(self.frameTFD, image=self.bt_conv_tfd, relief=FLAT, bd = 0, command= self.fechar_conv) #Adicionando a imagem a um botão
        self.figura_bt_conv_tfd.place(anchor = "center", relx= 0.5, rely=0.5, width= 510, height= 150) #Localizando o botão na tela

        self.bt_prefe_tfd = PhotoImage(file= bt[2]) #Chamando imagem 
        self.figura_bt_prefe_tfd = Button(self.frameTFD, image=self.bt_prefe_tfd, relief=FLAT, bd = 0, command= self.fechar_prefe)
        self.figura_bt_prefe_tfd.place(anchor = "center", relx= 0.5, rely=0.75, width= 510, height= 150) #Localizando o botão na tela

        self.aviso = Label(self.frameTFD, bg= cores[0], text="*As pessoas portadoras de deficiência, os idosos com idade igualou superior a 60 (sessenta) anos, as gestantes, as lactantes e as pessoas\nacompanhadas por crianças de colo terão atendimento prioritário")
        self.aviso.configure(font=fontes[0])
        self.aviso.place(anchor='center', relx= 0.5, rely=0.95) #Localizando o botão na tela 

        self.bt_voltar_tfd = PhotoImage(file = bt[4]) #Chamando imagem 
        self.figura_bt_voltar_tfd = Button(self.frameTFD, image = self.bt_voltar_tfd, relief=FLAT, bd = 0, command= self.rootTFD.destroy) #Adicionando a imagem a um botão
        self.figura_bt_voltar_tfd.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela 
        
    ###Função Escolha Preferencial ou Convencional AUTORIZAÇÃO DE EXAMES###
    def abrir_janela_CSUS(self):
        global ref
        ref = 3
        self.horario_ex()
        
    def cartao_sus(self):
        self.rootCSUS = tk.Toplevel() #Variavel para atribuir tela principal
        self.rootCSUS.configure(background= cores[0]) #Cor de fundo
        self.rootCSUS.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
        self.fullScreenState = False
        self.frameCSUS =Frame(self.rootCSUS, bg = cores[0]) #Definindo um Frame para a tela 
        self.frameCSUS.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela
        global opcao, opc, atendimento, tela, setor, set
        opcao = opc[1]
        setor = set[1]
        tela = 2

        #Imagens na Tela 
        self.fundo_CSUS = PhotoImage(file= planos[1]) #Plano de fundo principal
        figura_fundo_CSUS = Label(self.frameCSUS, image= self.fundo_CSUS, bd= 0) #Chamando imagem 
        figura_fundo_CSUS.place(anchor= 'center',relx=0.5, rely=0.4, width= 500, height= 500) #Localizando a imagem na tela

        self.btconv_imgCSUS = PhotoImage(file= bt[3]) #Imagem Botão Convencional
        self.btconv_CSUS = Button(self.frameCSUS, image=self.btconv_imgCSUS, relief=FLAT, bd = 0, command= self.fechar_conv) #Adicionando a imagem a um botão
        self.btconv_CSUS.place(anchor = "center", relx= 0.5, rely=0.5, width= 510, height= 150) #Localizando o botão na tela

        self.btprefe_imgCSUS = PhotoImage(file= bt[2]) #Imagem Botão Preferencial
        self.btprefe_CSUS = Button(self.frameCSUS, image=self.btprefe_imgCSUS, relief=FLAT, bd = 0, command= self.fechar_prefe) #Adicionando a imagem a um botão
        self.btprefe_CSUS.place(anchor = "center", relx= 0.5, rely=0.75, width= 510, height= 150) #Localizando o botão na tela

        self.aviso = Label(self.frameCSUS, bg= cores[0], text="*As pessoas portadoras de deficiência, os idosos com idade igualou superior a 60 (sessenta) anos, as gestantes, as lactantes e as pessoas\nacompanhadas por crianças de colo terão atendimento prioritário")
        self.aviso.configure(font=fontes[0])
        self.aviso.place(anchor='center', relx= 0.5, rely=0.95) #Localizando o botão na tela 

        self.btvoltar_imgCSUS = PhotoImage(file = bt[4]) #Imagem Botão Voltar 
        self.btvoltar_CSUS = Button(self.frameCSUS, image = self.btvoltar_imgCSUS, relief=FLAT, bd = 0, command= self.rootCSUS.destroy) #Adicionando a imagem a um botão
        self.btvoltar_CSUS.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela 

