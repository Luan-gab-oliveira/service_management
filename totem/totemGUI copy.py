from modules import *


root = tk.Tk() #Variavel Princiapal das telas 
w, h = root.winfo_screenwidth(), root.winfo_screenheight() #Variavel que pega as medidas da tela como referência
password = '' #Senha para fechamento do programa
atendimento = "" #Variavel para escolha do tipo de atendimento 
  
###Função para Coleta da Data atual para                                                                                                                                                                                                                                                                                                                                                                           senha###
data = datetime.now().strftime('%d/%m/%Y %H:%M')

tabela = 'fila_espera' #Atribuindo nome da tabela 
tela = 0 #Contagem do numero de telas 


###Definindo variaveis para Profissionais e especialidades###
prof= [
    "Dr. Caio",
    "Dr. Jocenyr",
    "Dra. Daffne",
    "Dr. Alcélio",
    "Dra. Lúcia",
    "Dr. Ademar"
    ]
esp = [
    "Clínico Geral",
    "Ginecologista",
    "Obstetrícia",
    "Pediatra",
    "Cardiologista",
    "Dermatologista",
    "Pequenas Cirurgias",
    "Ortopedista"
    ]
###Definindo variaveis para senha###
opcao = [
    "TFD", 
    "PREMIR",
    "F.ESTADO", 
    "F.AUTO C.", 
    "F.BASICA", 
    "AUT.EXA."
    ]
senhal = [
    "TFD", #TFD
    "PRE", #Premir  
    "FAE", #Farmacia Estada
    "FAA", #Farmacia Auto-custo
    "FAB", #Farmacia Atenção Básica
    "EXA"  #Autorização de Exames
    ]
###Definindo variaveis para tipo de atendimento###
atend = [
    "preferencial", 
    "convencional"
    ]

###Definindo variavel com o nome do local fonte dos arquivos###
get_dir = os.path.dirname(__file__)

###Definindo Variaveis para Botões e seus diretorios###

#Diretorios para os botões
btAUT = fr"{get_dir}\Botões\btAUT.png"
btF = fr"{get_dir}\Botões\btF.png"
btFA = fr"{get_dir}\Botões\btFA.png" 
btFAB = fr"{get_dir}\Botões\btFAB.png"
btFE = fr"{get_dir}\Botões\btFE.png"
btPREMIR = fr"{get_dir}\Botões\btPREMIR.png"
btTFD = fr"{get_dir}\Botões\btTFD.png"
btcon = fr"{get_dir}\Botões\btcon.png"
btconv = fr"{get_dir}\Botões\btconv.png"
btmult = fr"{get_dir}\Botões\btmult.png"
btpref = fr"{get_dir}\Botões\btpref.png"
btult = fr"{get_dir}\Botões\btult.png"
btvoltar = fr"{get_dir}\Botões\btvoltar.png"

#Atribuindo Lista de Botões 
bt = [ 
    btAUT,
    btF,
    btFA,
    btFAB,
    btFE,
    btPREMIR,
    btTFD,
    btcon,
    btconv,
    btmult,
    btpref,
    btult,
    btvoltar
    ]

###Definindo variaveis para os blocos e seus diretorios###
bloco_grande = fr"{get_dir}\Blocos\Bloco cinza.png"
bloco_medio = fr"{get_dir}\Blocos\Bloco cinza2.png"

bloco = [
    bloco_grande, 
    bloco_medio
    ]

###Definindo variavel para GIF e seu diretorio###
gif_carregamento = fr"{get_dir}\Gif\Icone carregamento.gif"

gif = [
    gif_carregamento
    ]

###Definindo variaveis para Icones e seu diretorio###
icone_borda = fr"{get_dir}\Icones\loader blue.png"

icone = [
    icone_borda
    ]

###Definindo variavel para Plano de Fundo e seus diretorios###
plano_principal = fr"{get_dir}\Plano de fundo\Plano de Fundo principal.png"
plano_final = fr"{get_dir}\Plano de fundo\Plano de Fundo final.png"
plano_aviso = fr"{get_dir}\Plano de fundo\Plano de Fundo de aviso.png"

planos = [
    plano_principal,
    plano_final,
    plano_aviso
    ]

###Definindo variavel para cores###
cores = [
    'white',
    "blue",
    '#125dab',
    '#f0f0f0',
    '#c7d0d8',
    ]

try:
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
    ###Classe para Funções###
    
    class func():
        global senha, opc, atendimento, senhal
        ###Funções de Fechamento de cada tela###
        def fechar22(self): #Função fechamento de tela Conv. do TFD, AUT, FAA, FAB, FAE, PRE
            global senha, opc, atendimento, tela
            atendimento = atend[1]
            self.gerar_senha()
            self.abrir_janela5()
            if tela == 1:
                self.root3.destroy()
                self.root2Mult.destroy() #Destruir janela 2 Mult
            elif tela == 2:
                self.root3.destroy()
                self.root2Ultrassom.destroy() #Destruir janela 2 Ultrassom
            elif tela == 3:
                self.root3.destroy()
                self.root2Consultas.destroy() #Destruir janela 2 Consultas
            elif tela == 4:
                self.root4.destroy()
                self.root20.destroy() #Destruir janela 20
            elif tela == 5:
                self.root4.destroy()
                self.root200.destroy() #Destruir janela 200
            elif tela == 6:
                self.root4.destroy()
                self.root2000.destroy() #Destruir janela 2000
            elif tela == 7:
                self.root21.destroy() #Destruir janela 21
            elif tela == 8:
                self.root22.destroy() #Destruir janela 2

        def fechar229(self): #Função fechamento de tela Pref. do TFD, AUT, FAA, FAB, FAE, PRE
            global senha, opc, atendimento, tela, senhal
            atendimento = atend[0]
            senha = 'P' + senha
            self.gerar_senha()
            self.abrir_janela5()
            if tela == 1:
                self.root3.destroy()
                self.root2Mult.destroy() #Destruir janela 2 Mult
            elif tela == 2:
                self.root3.destroy()
                self.root2Ultrassom.destroy() #Destruir janela 2 Ultrassom
            elif tela == 3:
                self.root3.destroy()
                self.root2Consultas.destroy() #Destruir janela 2 Consultas
            elif tela == 4:
                self.root4.destroy()
                self.root20.destroy() #Destruir janela 20
            elif tela == 5:
                self.root4.destroy()
                self.root200.destroy() #Destruir janela 200
            elif tela == 6:
                self.root4.destroy()
                self.root2000.destroy() #Destruir janela 2000
            elif tela == 7:
                self.root21.destroy() #Destruir janela 21
            elif tela == 8:
                self.root22.destroy() #Destruir janela 2
                
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

                    cursor.execute(sql) #executa instrução sql
                    conexao.commit() #commit para o interprertador entender que deve executar a instrução
                    threading.Thread(target=imprimir(senha, opc)).start()
                    # imprimir(senha, opc)
                    print(senha)
        ###Função Escolha Preferencial ou Convencional PREMIR Multiprofissionais###
        def abrir_janela2Mult(self): 
            self.root2Mult = tk.Toplevel() #Variavel para atribuir tela principal
            self.root2Mult.title('Sistema de Senhas Secretaria Municipal de Saúde.')#Atribuir titulo a tela
            self.root2Mult.configure(background= cores[2]) #Cor de fundo
            self.root2Mult.geometry("1366x768") #Dimensões do tamanho da tela cheia
            self.root2Mult.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
            self.fullScreenState = False
            self.root2Mult.resizable(False, False) #Negar o redimensionamento da tela
            self.root2Mult.minsize(width=800, height= 500) #Definir tamanho minimo da tela 
            self.frame2Mult =Frame(self.root2Mult, bg = cores[0]) #Definindo um Frame para a tela 
            self.frame2Mult.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96)  #Localizando o Frame na tela 
            global senha, opc, atendimento, tela, senhal
            senha = senhal[1]
            opc = opcao[1] 
            tela = 1

            #Imagens na Tela 
            self.photo2Mult = PhotoImage(file= planos[1]) #Plano de fundo principal
            figura2Mult = Label(self.frame2Mult, image= self.photo2Mult, bd= 0) #Chamando imagem 
            figura2Mult.place(relx=0.125, rely=0) #Localizando a imagem na tela

            self.photo22Mult = PhotoImage(file= bt[8]) #Chamando imagem 
            self.btconvMult = Button(self.frame2Mult, image=self.photo22Mult, relief=FLAT, bd = 0, command= self.fechar22) #Adicionando a imagem a um botão
            self.btconvMult.place(relx= 0.31, rely=0.4, relwidth= 0.387, relheight= 0.18) #Localizando o botão na tela

            self.photo222Mult = PhotoImage(file= bt[10]) #Chamando imagem 
            self.btprefeMult = Button(self.frame2Mult, image=self.photo222Mult, relief=FLAT, bd = 0, command= self.fechar229)
            self.btprefeMult.place(relx= 0.31, rely=0.6, relwidth= 0.39, relheight= 0.2) #Localizando o botão na tela

            self.photo2222Mult = PhotoImage(file = bt[12]) #Chamando imagem 
            self.btvoltarMult = Button(self.frame2Mult, image = self.photo2222Mult, relief=FLAT, bd = 0, command= self.root2Mult.destroy) #Adicionando a imagem a um botão
            self.btvoltarMult.place(relx= 0.05, rely=0.05, relwidth= 0.173, relheight= 0.08) #Localizando o botão na tela
        ###Função Escolha Preferencial ou Convencional PREMIR Consultas###
        def abrir_janela2Consultas(self): 
            self.root2Consultas = tk.Toplevel() #Variavel para atribuir tela principal
            self.root2Consultas.title('Sistema de Senhas Secretaria Municipal de Saúde.')#Atribuir titulo a tela
            self.root2Consultas.configure(background= cores[2]) #Cor de fundo
            self.root2Consultas.geometry("1366x768") #Dimensões do tamanho da tela cheia
            self.root2Consultas.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
            self.fullScreenState = False
            self.root2Consultas.resizable(False, False) #Negar o redimensionamento da telato
            self.root2Consultas.minsize(width=800, height= 500) #Definir tamanho minimo da tela 
            self.frame2Consultas =Frame(self.root2Consultas, bg = cores[0]) #Definindo um Frame para a tela 
            self.frame2Consultas.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96)  #Localizando o Frame na tela 
            global senha, opc, atendimento, tela, senhal
            senha = senhal[1]
            opc = opcao[1] 
            tela = 3

            #Imagens na Tela 
            self.photo2Consultas = PhotoImage(file= planos[1]) #Plano de fundo principal
            figura2Consultas = Label(self.frame2Consultas, image= self.photo2Consultas, bd= 0) #Chamando imagem 
            figura2Consultas.place(relx=0.125, rely=0) #Localizando a imagem na tela

            self.photo22Consultas = PhotoImage(file= bt[8]) #Chamando imagem 
            self.btconvConsultas = Button(self.frame2Consultas, image=self.photo22Consultas, relief=FLAT, bd = 0, command= self.fechar22) #Adicionando a imagem a um botão
            self.btconvConsultas.place(relx= 0.31, rely=0.4, relwidth= 0.387, relheight= 0.18) #Localizando o botão na tela

            self.photo222Consultas = PhotoImage(file= bt[10]) #Chamando imagem 
            self.btprefeConsultas = Button(self.frame2Consultas, image=self.photo222Consultas, relief=FLAT, bd = 0, command= self.fechar229)
            self.btprefeConsultas.place(relx= 0.31, rely=0.6, relwidth= 0.39, relheight= 0.2) #Localizando o botão na tela

            self.photo2222Consultas = PhotoImage(file = bt[12]) #Chamando imagem 
            self.btvoltarConsultas = Button(self.frame2Consultas, image = self.photo2222Consultas, relief=FLAT, bd = 0, command= self.root2Consultas.destroy) #Adicionando a imagem a um botão
            self.btvoltarConsultas.place(relx= 0.05, rely=0.05, relwidth= 0.173, relheight= 0.08) #Localizando o botão na tela
        ###Função Escolha Preferencial ou Convencional PREMIR Ultrassom###
        def abrir_janela2Ultrassom(self): 
            self.root2Ultrassom = tk.Toplevel() #Variavel para atribuir tela principal
            self.root2Ultrassom.title('Sistema de Senhas Secretaria Municipal de Saúde.')#Atribuir titulo a tela
            self.root2Ultrassom.configure(background= cores[2]) #Cor de fundo
            self.root2Ultrassom.geometry("1366x768") #Dimensões do tamanho da tela cheia
            self.root2Ultrassom.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
            self.fullScreenState = False
            self.root2Ultrassom.resizable(False, False) #Negar o redimensionamento da tela
            self.root2Ultrassom.minsize(width=800, height= 500) #Definir tamanho minimo da tela 
            self.frame2Ultrassom =Frame(self.root2Ultrassom, bg = cores[0]) #Definindo um Frame para a tela 
            self.frame2Ultrassom.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96)  #Localizando o Frame na tela 
            global senha, opc, atendimento, tela, senhal
            senha = senhal[1]
            opc = opcao[1] 
            tela = 2

            #Imagens na Tela 
            self.photo2Ultrassom = PhotoImage(file= planos[1]) #Plano de fundo principal
            figura2Ultrassom = Label(self.frame2Ultrassom, image= self.photo2Ultrassom, bd= 0) #Chamando imagem 
            figura2Ultrassom.place(relx=0.125, rely=0) #Localizando a imagem na tela

            self.photo22Ultrassom = PhotoImage(file= bt[8]) #Chamando imagem 
            self.btconvUltrassom = Button(self.frame2Ultrassom, image=self.photo22Ultrassom, relief=FLAT, bd = 0, command= self.fechar22) #Adicionando a imagem a um botão
            self.btconvUltrassom.place(relx= 0.31, rely=0.4, relwidth= 0.387, relheight= 0.18) #Localizando o botão na tela

            self.photo222Ultrassom = PhotoImage(file= bt[10]) #Chamando imagem 
            self.btprefeUltrassom = Button(self.frame2Ultrassom, image=self.photo222Ultrassom, relief=FLAT, bd = 0, command= self.fechar229)
            self.btprefeUltrassom.place(relx= 0.31, rely=0.6, relwidth= 0.39, relheight= 0.2) #Localizando o botão na tela

            self.photo2222Ultrassom = PhotoImage(file = bt[12]) #Chamando imagem 
            self.btvoltarUltrassom = Button(self.frame2Ultrassom, image = self.photo2222Ultrassom, relief=FLAT, bd = 0, command= self.root2Ultrassom.destroy) #Adicionando a imagem a um botão
            self.btvoltarUltrassom.place(relx= 0.05, rely=0.05, relwidth= 0.173, relheight= 0.08) #Localizando o botão na tela
        ###Função Escolha Preferencial ou Convencional FARMACIA BASICA###
        def abrir_janela_AtencaoBasica(self): 
            self.root20 = tk.Toplevel() #Variavel para atribuir tela principal
            self.root20.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuir titulo a tela
            self.root20.configure(background= cores[2]) #Cor de fundo
            self.root20.geometry("1366x768") #Dimensões do tamanho da tela cheia
            self.root20.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
            self.fullScreenState = False
            self.root20.resizable(False, False) #Negar o redimensionamento da tela
            self.root20.minsize(width=800, height= 500) #Definir tamanho minimo da tela 
            self.frame20 =Frame(self.root20, bg = cores[0]) #Definindo um Frame para a tela 
            self.frame20.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 
            global senha, opc, atendimento, tela, senhal
            senha = senhal[4]
            opc = opcao[4] 
            tela = 4
            
            #Imagens na Tela 
            self.photo20 = PhotoImage(file= planos[1]) #Plano de fundo principal
            figura20 = Label(self.frame20, image= self.photo20, bd= 0) #Chamando imagem 
            figura20.place(relx=0.125, rely=0) #Localizando a imagem na tela

            self.photo220 = PhotoImage(file= bt[8]) #Imagem Botão Convencional
            self.btconv = Button(self.frame20, image=self.photo220, relief=FLAT, bd = 0, command= self.fechar22) #Adicionando a imagem a um botão
            self.btconv.place(relx= 0.31, rely=0.4, relwidth= 0.387, relheight= 0.18) #Localizando o botão na tela

            self.photo2220 = PhotoImage(file= bt[10]) #Imagem Botão Preferencial
            self.btprefe = Button(self.frame20, image=self.photo2220, relief=FLAT, bd = 0, command= self.fechar229) #Adicionando a imagem a um botão
            self.btprefe.place(relx= 0.31, rely=0.6, relwidth= 0.39, relheight= 0.2) #Localizando o botão na tela

            self.photo22220 = PhotoImage(file = bt[12]) #Imagem Botão Voltar 
            self.btvoltar = Button(self.frame20, image = self.photo22220, relief=FLAT, bd = 0, command= self.root20.destroy) #Adicionando a imagem a um botão
            self.btvoltar.place(relx= 0.05, rely=0.05, relwidth= 0.173, relheight= 0.08) #Localizando o botão na tela
        ###Função Escolha Preferencial ou Convencional FARMACIA ESTADO###
        def abrir_janela_Estado(self): 
            self.root200 = tk.Toplevel() #Variavel para atribuir tela principal
            self.root200.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuir titulo a tela
            self.root200.configure(background= cores[2]) #Cor de fundo
            self.root200.geometry("1366x768") #Dimensões do tamanho da tela cheia
            self.root200.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
            self.fullScreenState = False
            self.root200.resizable(False, False) #Negar o redimensionamento da tela
            self.root200.minsize(width=800, height= 500) #Definir tamanho minimo da tela 
            self.frame200 =Frame(self.root200, bg = cores[0]) #Definindo um Frame para a tela 
            self.frame200.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 
            global senha, opc, atendimento, tela, senhal
            senha = senhal[2]
            opc = opcao[2] 
            tela = 5
            
            #Imagens na Tela 
            self.photo200 = PhotoImage(file= planos[1]) #Plano de fundo principal
            figura200 = Label(self.frame200, image= self.photo200, bd= 0) #Chamando imagem 
            figura200.place(relx=0.125, rely=0) #Localizando a imagem na tela

            self.photo2200 = PhotoImage(file= bt[8]) #Imagem Botão Convencional
            self.btconv = Button(self.frame200, image=self.photo2200, relief=FLAT, bd = 0, command= self.fechar22) #Adicionando a imagem a um botão
            self.btconv.place(relx= 0.31, rely=0.4, relwidth= 0.387, relheight= 0.18) #Localizando o botão na tela

            self.photo22200 = PhotoImage(file= bt[10]) #Imagem Botão Preferencial
            self.btprefe = Button(self.frame200, image=self.photo22200, relief=FLAT, bd = 0, command= self.fechar229) #Adicionando a imagem a um botão
            self.btprefe.place(relx= 0.31, rely=0.6, relwidth= 0.39, relheight= 0.2) #Localizando o botão na tela

            self.photo222200 = PhotoImage(file = bt[12]) #Imagem Botão Voltar 
            self.btvoltar = Button(self.frame200, image = self.photo222200, relief=FLAT, bd = 0, command= self.root200.destroy) #Adicionando a imagem a um botão
            self.btvoltar.place(relx= 0.05, rely=0.05, relwidth= 0.173, relheight= 0.08) #Localizando o botão na tela
        ###Função Escolha Preferencial ou Convencional FARMACIA AUTO-CUSTO###
        def abrir_janela_AutoCusto(self): 
            self.root2000 = tk.Toplevel() #Variavel para atribuir tela principal
            self.root2000.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuir titulo a tela
            self.root2000.configure(background= cores[2]) #Cor de fundo
            self.root2000.geometry("1366x768") #Dimensões do tamanho da tela cheia
            self.root2000.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
            self.fullScreenState = False
            self.root2000.resizable(False, False) #Negar o redimensionamento da tela
            self.root2000.minsize(width=800, height= 500) #Definir tamanho minimo da tela 
            self.frame2000 =Frame(self.root2000, bg = cores[0]) #Definindo um Frame para a tela 
            self.frame2000.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 
            global senha, opc, atendimento, tela, senhal
            senha = senhal[3]
            opc = opcao[3] 
            tela = 6
            
            #Imagens na Tela 
            self.photo2000 = PhotoImage(file= planos[1]) #Plano de fundo principal
            figura2000 = Label(self.frame2000, image= self.photo2000, bd= 0) #Chamando imagem 
            figura2000.place(relx=0.125, rely=0) #Localizando a imagem na tela

            self.photo22000 = PhotoImage(file= bt[8]) #Imagem Botão Convencional
            self.btconv = Button(self.frame2000, image=self.photo22000, relief=FLAT, bd = 0, command= self.fechar22) #Adicionando a imagem a um botão
            self.btconv.place(relx= 0.31, rely=0.4, relwidth= 0.387, relheight= 0.18) #Localizando o botão na tela

            self.photo222000 = PhotoImage(file= bt[10]) #Imagem Botão Preferencial
            self.btprefe = Button(self.frame2000, image=self.photo222000, relief=FLAT, bd = 0, command= self.fechar229) #Adicionando a imagem a um botão
            self.btprefe.place(relx= 0.31, rely=0.6, relwidth= 0.39, relheight= 0.2) #Localizando o botão na tela

            self.photo2222000 = PhotoImage(file = bt[12]) #Imagem Botão Voltar 
            self.btvoltar = Button(self.frame2000, image = self.photo2222000, relief=FLAT, bd = 0, command= self.root2000.destroy) #Adicionando a imagem a um botão
            self.btvoltar.place(relx= 0.05, rely=0.05, relwidth= 0.173, relheight= 0.08) #Localizando o botão na tela    
        ###Função Escolha Preferencial ou Convencional AUTORIZAÇÃO DE EXAMES###
        def abrir_janela21(self): 
            self.root21 = tk.Toplevel() #Variavel para atribuir tela principal
            self.root21.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuir titulo a tela
            self.root21.configure(background= cores[2]) #Cor de fundo
            self.root21.geometry("1366x768") #Dimensões do tamanho da tela cheia
            self.root21.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
            self.fullScreenState = False
            self.root21.resizable(False, False) #Negar o redimensionamento da tela
            self.root21.minsize(width=800, height= 500) #Definir tamanho minimo da tela 
            self.frame21 =Frame(self.root21, bg = cores[0]) #Definindo um Frame para a tela 
            self.frame21.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 
            global senha, opc, atendimento, tela, senhal
            senha = senhal[5]
            opc = opcao[5]
            tela = 7

            #Imagens na Tela 
            self.photo21 = PhotoImage(file= planos[1]) #Plano de fundo principal
            figura21 = Label(self.frame21, image= self.photo21, bd= 0) #Chamando imagem 
            figura21.place(relx=0.125, rely=0) #Localizando a imagem na tela

            self.photo221 = PhotoImage(file= bt[8]) #Imagem Botão Convencional
            self.btconv = Button(self.frame21, image=self.photo221, relief=FLAT, bd = 0, command= self.fechar22) #Adicionando a imagem a um botão
            self.btconv.place(relx= 0.31, rely=0.4, relwidth= 0.387, relheight= 0.18) #Localizando o botão na tela

            self.photo2221 = PhotoImage(file= bt[10]) #Imagem Botão Preferencial
            self.btprefe = Button(self.frame21, image=self.photo2221, relief=FLAT, bd = 0, command= self.fechar229) #Adicionando a imagem a um botão
            self.btprefe.place(relx= 0.31, rely=0.6, relwidth= 0.39, relheight= 0.2) #Localizando o botão na tela

            self.photo22221 = PhotoImage(file = bt[12]) #Imagem Botão Voltar 
            self.btvoltar = Button(self.frame21, image = self.photo22221, relief=FLAT, bd = 0, command= self.root21.destroy) #Adicionando a imagem a um botão
            self.btvoltar.place(relx= 0.05, rely=0.05, relwidth= 0.173, relheight= 0.08) #Localizando o botão na tela   
        ###Função Escolha Preferencial ou Convencional TFD###
        def abrir_janela22(self):
            self.root22 = tk.Toplevel() #Variavel para atribuir tela principal
            self.root22.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuir titulo a tela
            self.root22.configure(background= cores[2]) #Cor de fundo
            self.root22.geometry("1366x768") #Dimensões do tamanho da tela cheia
            self.root22.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
            self.fullScreenState = False
            self.root22.resizable(False, False) #Negar o redimensionamento da tela
            self.root22.minsize(width=800, height= 500) #Definir tamanho minimo da tela 
            self.frame22 =Frame(self.root22, bg = cores[0]) #Definindo um Frame para a tela 
            self.frame22.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 
            global senha, opc, atendimento, tela, senhal
            senha = senhal[0]
            opc = opcao[0]
            tela = 8
            
            #Imagens na Tela 
            self.photo22 = PhotoImage(file= planos[1]) #Plano de fundo principal
            figura22 = Label(self.frame22, image= self.photo22, bd= 0) #Chamando imagem 
            figura22.place(relx=0.125, rely=0) #Localizando a imagem na tela

            self.photo222 = PhotoImage(file= bt[8]) #Imagem Botão Convencional
            self.btconv = Button(self.frame22, image=self.photo222, relief=FLAT, bd = 0, command= self.fechar22) #Adicionando a imagem a um botão
            self.btconv.place(relx= 0.31, rely=0.4, relwidth= 0.387, relheight= 0.18) #Localizando o botão na tela

            self.photo2222 = PhotoImage(file= bt[10]) #Imagem Botão Preferencial
            self.btprefe = Button(self.frame22, image=self.photo2222, relief=FLAT, bd = 0, command= self.fechar229) #Adicionando a imagem a um botão
            self.btprefe.place(relx= 0.31, rely=0.6, relwidth= 0.39, relheight= 0.2) #Localizando o botão na tela

            self.photo22222 = PhotoImage(file = bt[12]) #Imagem Botão Voltar 
            self.btvoltar = Button(self.frame22, image = self.photo22222, relief=FLAT, bd = 0, command= self.root22.destroy) #Adicionando a imagem a um botão
            self.btvoltar.place(relx= 0.05, rely=0.05, relwidth= 0.173, relheight= 0.08) #Localizando o botão na tela   
        ###Função para Tela Premir###
        def abrir_janela3(self):
            self.root3 = tk.Toplevel()#Abertura da Tela 4 de Opções do Premir
            self.root3.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuição do titulo
            self.root3.configure(background= cores[2]) #Cor do plano de fundo da tela 
            self.root3.geometry("1366x768") #Código que faz a tela abrir em modo tela cheia
            self.root3.attributes('-fullscreen', True) #Código que faz com que a tela fique em Fullscreen
            self.root3.resizable(False, False) #Permite que o tamanho da tela seja reajustado
            self.root3.minsize(width=800, height= 500) #Tamanhos minimos para diminuir a tela
            self.frame3 =Frame(self.root3, bd = 4, bg = cores[0]) #Frame definido para a tela 4 com fundo branco
            self.frame3.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96) #Definição do local do frame expresso em porcentagem de tela

            #Imagens na Tela 
            self.photo3 = PhotoImage(file= planos[0]) #Plano de fundo principal
            self.photo33 = PhotoImage(file= bloco[1]) #Blocos de Cores


            figura3 = Label(self.frame3, image= self.photo3, bd= 0) #Chamando imagem 
            figura3.place(relx=0.152, rely=0, relwidth= 0.7, relheight= 0.9) #Localizando a imagem na tela

            figura33 = Label(self.frame3, image= self.photo33, bd= 0) #Chamando imagem 
            figura33.place(relx=0.04, rely=0.334) #Localizando a imagem na tela

            figura333 = Label(self.frame3, image= self.photo33, bd= 0) #Chamando imagem 
            figura333.place(relx=0.355, rely=0.334) #Localizando a imagem na tela

            figura3333 = Label(self.frame3, image= self.photo33, bd= 0) #Chamando imagem
            figura3333.place(relx=0.67, rely=0.334) #Localizando a imagem na tela

            fontexemplo0 = tkFont.Font(family= 'Arial Black', size= 18) #Definindo Variavel para fonte padrão
            fontexemplo01 = tkFont.Font(family= 'Arial Black', size= 12) #Definindo Variavel para fonte padrão
            fontexemplo3 = tkFont.Font(family= 'Arial Black', size= 20) #Definindo Variavel para fonte padrão
            fontexemplo33 = tkFont.Font(family= 'Arial Black', size= 10) #Definindo Variavel para fonte padrão

            self.photo3333 = PhotoImage(file = bt[7]) #Imagem botão Consultas
            self.btPconsultas = Button(self.frame3, image= self.photo3333, relief=FLAT, bd= 0, command= self.abrir_janela2Consultas) #Adicionando a imagem a um botão
            self.btPconsultas.place(relx= 0.395, rely=0.4, relwidth= 0.21, relheight= 0.1) #Localizando o botão na tela

            self.photo33333 = PhotoImage(file= bt[11]) #Imagem botão Ultrassom
            self.btult = Button(self.frame3, image= self.photo33333, relief=FLAT, bd= 0, command= self.abrir_janela2Ultrassom) #Adicionando a imagem a um botão
            self.btult.place(relx= 0.713, rely=0.4, relwidth= 0.21, relheight= 0.1) #Localizando o botão na tela

            self.photo333333 = PhotoImage(file = bt[9]) #Imagem botão Multiprofissionais
            self.btmult = Button(self.frame3, image= self.photo333333, relief=FLAT, bd= 0, command= self.abrir_janela2Mult) #Adicionando a imagem a um botão
            self.btmult.place(relx= 0.080, rely=0.4, relwidth= 0.21, relheight= 0.1) #Localizando o botão na tela

            self.photo3333333 = PhotoImage(file = bt[12]) #Imagem botão Voltar
            self.btvoltar = Button(self.frame3, image = self.photo3333333, relief=FLAT, bd = 0, command= self.root3.destroy) #Adicionando a imagem a um botão
            self.btvoltar.place(relx= 0.05, rely=0.05, relwidth= 0.17, relheight= 0.08) #Localizando o botão na tela

            self.btconsultas2 = Button(self.frame3, text = f"•{esp[0]} \n•{esp[1]} \n•{esp[2]} \n•{esp[3]} \n•{esp[4]} \n•{esp[5]} \n•{esp[6]} \n•{esp[7]}", relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.abrir_janela2Consultas) #Adicionando texto a um botão
            self.btconsultas2.configure(font = fontexemplo0) #Configuração fonte padrão
            self.btconsultas2.place(relx= 0.398, rely=0.52, relwidth= 0.21, relheight= 0.4)  #Localizando o botão na tela
            
            self.btult2 = Button(self.frame3, text = "•Agendamento \n•Resultado de \nExames", relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.abrir_janela2Ultrassom) #Adicionando texto a um botão
            self.btult2.configure(font = fontexemplo0) #Configuração fonte padrão
            self.btult2.place(relx= 0.713, rely=0.5, relwidth= 0.21, relheight= 0.4)  #Localizando o botão na tela
            
            self.btmult2 = Button(self.frame3, text = "Multiprofissonais: \n\n•Psícologa \n•Terapia Ocupacional \n•Assistente Social \n •Fonoaudióloga", relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.abrir_janela2Mult) #Adicionando texto a um botão
            self.btmult2.configure(font = fontexemplo0) #Configuração fonte padrão
            self.btmult2.place(relx= 0.06, rely=0.51, relwidth= 0.25, relheight= 0.3)  #Localizando o botão na tela

            self.mult2 = Label(self.frame3, text= "*A senha Multiprofissionais atende \na todos os profissionais acima!", background= cores[4])
            self.mult2.configure(font = fontexemplo33)
            self.mult2.place(relx= 0.08, rely=0.85, relwidth= 0.21, relheight= 0.07)  #Localizando o botão na tela

        ###Função para Tela Farmacias###
        def abrir_janela4(self): 
            self.root4 = tk.Toplevel()#Abertura da Tela 4 de Opções do Premir
            self.root4.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuição do titulo
            self.root4.configure(background= cores[2]) #Cor do plano de fundo da tela 
            self.root4.geometry("1366x768") #Código que faz a tela abrir em modo tela cheia
            self.root4.attributes('-fullscreen', True) #Código que faz com que a tela fique em Fullscreen
            self.root4.resizable(False, False) #Permite que o tamanho da tela seja reajustado
            self.root4.minsize(width=800, height= 500) #Tamanhos minimos para diminuir a tela
            self.frame4 =Frame(self.root4, bd = 4, bg = cores[0]) #Frame definido para a tela 4 com fundo branco
            self.frame4.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96) #Definição do local do frame expresso em porcentagem de tela

            #Imagens na Tela 
            self.photo4 = PhotoImage(file= planos[0]) #Plano de fundo principal
            self.photo44 = PhotoImage(file= bloco[1]) #Blocos de Cores
            

            figura4 = Label(self.frame4, image= self.photo4, bd= 0) #Chamando imagem1
            figura4.place(relx=0.125, rely=0, relwidth= 0.75, relheight= 0.9) #Localizando a imagem na tela

            figura44 = Label(self.frame4, image= self.photo44, bd= 0) #Chamando imagem 
            figura44.place(relx=0.04, rely=0.334) #Localizando a imagem na tela

            figura444 = Label(self.frame4, image= self.photo44, bd= 0) #Chamando imagem 
            figura444.place(relx=0.355, rely=0.334) #Localizando a imagem na tela

            figura4444 = Label(self.frame4, image= self.photo44, bd= 0) #Chamando imagem
            figura4444.place(relx=0.67, rely=0.334) #Localizando a imagem na tela

            fontexemplo0 = tkFont.Font(family= 'Arial Black', size= 18) #Definindo Variavel para fonte padrão
            fontexemplo = tkFont.Font(family= 'Arial Black', size= 23) #Definindo Variavel para fonte padrão
            fontexemplo2 = tkFont.Font(family= 'Arial Black', size= 40) #Definindo Variavel para fonte padrão
            fontexemplo3 = tkFont.Font(family= 'Arial Black', size= 20) #Definindo Variavel para fonte padrão

            self.photo444= PhotoImage(file = bt[2]) #Imagem botão Farmacia Auto-custo
            self.btFA = Button(self.frame4, image= self.photo444, relief=FLAT, bd= 0, command= self.abrir_janela_AutoCusto) #Adicionando a imagem a um botão
            self.btFA.place(relx= 0.395, rely=0.4, relwidth= 0.21, relheight= 0.1) #Localizando o botão na tela
        
            self.photo4444 = PhotoImage(file= bt[3]) #Imagem botão Farmacia Atenção Básica
            self.btFAB = Button(self.frame4, image= self.photo4444, relief=FLAT, bd= 0, command= self.abrir_janela_AtencaoBasica) #Adicionando a imagem a um botão
            self.btFAB.place(relx= 0.08, rely=0.4, relwidth= 0.21, relheight= 0.1) #Localizando o botão na tela

            self.photo44444 = PhotoImage(file = bt[4]) #Imagem botão Farmacia Estado
            self.btFE = Button(self.frame4, image= self.photo44444, relief=FLAT, bd= 0, command= self.abrir_janela_Estado) #Adicionando a imagem a um botão
            self.btFE.place(relx= 0.713, rely=0.4, relwidth= 0.21, relheight= 0.1) #Localizando o botão na tela

            self.BtFAB = Button(self.frame4, text= 'CBAF \n\nMedicamentos \nfornecidos pelo \nMunicípio \n', relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.abrir_janela_AtencaoBasica)
            self.BtFAB.place(relx= 0.08, rely=0.5, relwidth= 0.21, relheight= 0.4) #Localizando o botão na tela
            self.BtFAB.configure(font= fontexemplo0)

            self.BtFE = Button(self.frame4, text= 'CEAF \n\nMedicamentos \nretirados apartir \ndo Estado ou \nJudicial', relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.abrir_janela_Estado)
            self.BtFE.place(relx= 0.713, rely=0.5, relwidth= 0.21, relheight= 0.4) #Localizando o botão na tela
            self.BtFE.configure(font= fontexemplo0)

            self.BtFA = Button(self.frame4, text= 'Convenio Municípal \n\nFarmâcias Externas \nconveniadas ao \nMunicípio \n', relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.abrir_janela_AutoCusto)
            self.BtFA.place(relx= 0.395, rely=0.5, relwidth= 0.21, relheight= 0.4) #Localizando o botão na tela
            self.BtFA.configure(font= fontexemplo0)
            
            self.photo444444 = PhotoImage(file = bt[12]) #Imagem botão Voltar 
            self.btvoltar = Button(self.frame4, image = self.photo444444, relief=FLAT, bd = 0, command= self.root4.destroy) #Adicionando a imagem a um botão
            self.btvoltar.place(relx= 0.05, rely=0.05, relwidth= 0.17, relheight= 0.08) #Localizando o botão na tela
        ###Função para tela de espera de senha###
        def abrir_janela5(self):
            self.root5 = tk.Toplevel()
            self.root5.title('') #Atribuição do titulo
            self.root5.configure(background= cores[2]) #Cor do plano de fundo da tela 
            self.root5.geometry('400x500') #Código que faz a tela abrir em modo tela cheia #Código que faz com que a tela fique em Fullscreen
            self.root5.attributes('-alpha', 0.0)
            self.root5.resizable(False, False) #Negar que o tamanho da tela seja reajustado
            self.frame5 =Frame(self.root5, bd = 5, highlightbackground= cores[2], highlightthickness= 10, bg = cores[3]) #Frame definido para a tela 4 com fundo branco
            self.frame5.place(relx= 0,rely= 0, relwidth= 1, relheight= 1)
            
            fontexemplo5 = tkFont.Font(family= 'Arial Black', size= 20)

            self.aguarde = Label(self.frame5, text= 'Aguarde um instante! \nGerando Senha...', background= cores[3], bd = 0)
            self.aguarde.configure(font= fontexemplo5)
            self.aguarde.place(relx= 0.05,rely= 0.01, relwidth= 0.9, relheight=0.5)

            ###Adicionando GIF de Carregamento###
            file= gif[0]
            info = Image.open(file)
            frames = info.n_frames  # gives total number of frames that gif contains
            # creating list of PhotoImage objects for each frames
            im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]
            count = 0
            anim = None
            def animation(count):
                global anim
                im2 = im[count]

                gif_label.configure(image=im2)
                count += 1
                if count == frames:
                    count = 0
                anim = self.root5.after(50,lambda :animation(count))

            gif_label = tk.Label(self.root5)
            gif_label.place(relx= 0.17,rely= 0.35)
            start = tk.Button(self.root5,command= animation(count))
            

            ###Código para janela abrir no meio da tela###
            self.root5.update_idletasks()
            width = self.root5.winfo_width()
            frm_width = self.root5.winfo_rootx() - self.root5.winfo_x()
            win_width = width + 2 * frm_width

            height = self.root5.winfo_height()
            titlebar_height = self.root5.winfo_rooty() - self.root5.winfo_y()
            win_height = height + titlebar_height + frm_width

            x = self.root5.winfo_screenwidth() // 2 - win_width // 2
            y = self.root5.winfo_screenheight() // 2 - win_height // 2
            self.root5.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            self.root5.deiconify()
            
            self.root5.attributes('-alpha', 1.0)
            self.root5.overrideredirect(True)
            self.root5.after(5000,self.root5.destroy)











    ###Tela Inicial###        
    class Application(func):
        def __init__(self): #Tela Incial Conv. e Pref.
            # try:
            self.root = root #Variavel para atribuir tela principal
            # self.root.bind('<F11>', self.toggleFullScreen) #Variavel para ligar e desligar o modo Fullscreen
            # self.root.bind('<Escape>', self.quitFullScreen) #Variavel para escapar do modo Fullscreen
            self.tela() #Variavel para atribuir Configurações da tela
            self.frames() #Variavel para atribuir a divisão dos frames
            self.widgets() #Variavel para atribuir botões na tela
            root.mainloop() #Variavel que faz com que a tela permaneça aberta enquanto em uso 
            # except:
            #     pass

        # def toggleFullScreen(self, event):
        #     self.fullScreenState = True
        #     self.root.attributes("-fullscreen", self.fullScreenState)

        # def quitFullScreen(self, event):
        #     self.fullScreenState = False
        #     self.root.attributes("-fullscreen", self.fullScreenState)

        def tela(self):
            self
            self.root.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuição do titulo
            self.root.configure(background= cores[2]) #Cor do plano de fundo da tela
            self.root.geometry("1366x768") #Código que faz a tela abrir em modo tela cheia
            self.root.attributes('-fullscreen', True) #Código que faz com que a tela fique em Fullscreen
            self.root.resizable(False, False) #Permite que o tamanho da tela seja reajustado
            self.root.minsize(width=800, height= 500) #Tamanhos minimos para diminuir a tela

        def frames(self):
            self.frame =Frame(self.root, bd = 4, bg = cores[0]) #Frame definido para a tela 4 com fundo branco
            self.frame.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.96) #Definição do local do frame expresso em porcentagem de tela
            
            ###Imagens na Tela### 
            self.photo_plano_de_fundo = PhotoImage(file= planos[0]) #Plano de fundo principal
            plano_de_fundo = Label(self.frame, image= self.photo_plano_de_fundo, bd= 0) #Chamando imagem 
            plano_de_fundo.place(relx=0.125, rely=0) #Localizando a imagem na tela      
        def widgets(self):
            # ###Botões###
            # self.photo_bt_TFD = PhotoImage(file = bt[6]) #Imagem botão TFD
            # self.bt_TFD = Button(self.frame, image= self.photo_bt_TFD, relief=FLAT, bd = 0, command= self.abrir_janela22) #Adicionando a imagem a um botão
            # self.bt_TFD.place(relx= 0.549, rely=0.7, relwidth= 0.39, relheight= 0.19) #Localizando o botão na tela

            # self.photo_bt_FARMARCIA = PhotoImage(file = bt[1]) #Imagem botão Farmacia
            # self.bt_F = Button(self.frame, image= self.photo_bt_FARMARCIA, relief=FLAT, bd= 0, command= self.abrir_janela4) #Adicionando a imagem a um botão
            # self.bt_F.place(relx= 0.07, rely=0.675, relwidth= 0.395, relheight= 0.22) #Localizando o botão na tela

            # self.photo_bt_PREMIR = PhotoImage(file = bt[5]) #Imagem botão PREMIR    
            # self.bt_premir = Button(self.frame, image = self.photo_bt_PREMIR, bd = 0, relief=FLAT, command= self.abrir_janela3) #Adicionando a imagem a um botão
            # self.bt_premir.place(relx= 0.547, rely=0.40, relwidth= 0.3965, relheight= 0.21) #Localizando o botão na tela
            
            # self.photo_BT_AUT_EXAMES = PhotoImage(file = bt[0]) #Imagem botão Autorização de Exames
            # self.bt_Aut = Button(self.frame, image = self.photo_BT_AUT_EXAMES, bd = 0, relief=FLAT, command= self.abrir_janela21) #Adicionando a imagem a um botão
            # self.bt_Aut.place(relx= 0.079, rely=0.41, relwidth= 0.389, relheight= 0.19) #Localizando o botão na tela


            ###Botões###
            self.photo_bt_FARMARCIA = PhotoImage(file = bt[1]) #Imagem botão Farmacia
            self.bt_F = Button(self.frame, image= self.photo_bt_FARMARCIA, relief=FLAT, bd= 0, command= self.abrir_janela4) #Adicionando a imagem a um botão
            self.bt_F.place(relx= 0.31, rely=0.675, relwidth= 0.395, relheight= 0.22) #Localizando o botão na tela

            self.photo_bt_PREMIR = PhotoImage(file = bt[5]) #Imagem botão PREMIR    
            self.bt_premir = Button(self.frame, image = self.photo_bt_PREMIR, bd = 0, relief=FLAT, command= self.abrir_janela3) #Adicionando a imagem a um botão
            self.bt_premir.place(relx= 0.547, rely=0.40, relwidth= 0.3965, relheight= 0.21) #Localizando o botão na tela
            
            self.photo_BT_AUT_EXAMES = PhotoImage(file = bt[0]) #Imagem botão Autorização de Exames
            self.bt_Aut = Button(self.frame, image = self.photo_BT_AUT_EXAMES, bd = 0, relief=FLAT, command= self.abrir_janela21) #Adicionando a imagem a um botão
            self.bt_Aut.place(relx= 0.079, rely=0.41, relwidth= 0.389, relheight= 0.19) #Localizando o botão na tela


except:
    pass

def on_closing():
    password_close = simpledialog.askstring(title='', prompt='Informe a senha',show= '*')
    if password_close == password:
        root.destroy() 

root.protocol('WM_DELETE_WINDOW', on_closing)   
if __name__ == '__main__':
    app = Application() 


    
Application()