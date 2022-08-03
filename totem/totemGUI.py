from modules import *
from config import *

###Tela Inicial###        
class Application():
    def __init__(self):
        self.root = tk.Tk() #Variavel para atribuir tela principal
        self.width_screnn = self.root.winfo_screenwidth()
        self.height_screnn = self.root.winfo_screenheight()   
        self.tela() #Variavel para atribuir Configurações da tela
        self.frames() #Variavel para atribuir a divisão dos frames
        self.widgets() #Variavel para atribuir botões na tela
        self.root.mainloop() #Variavel que faz com que a tela permaneça aberta enquanto em uso


    def tela(self):
        width_root = 1366
        height_root = 768
        pos_x = self.width_screnn/2 - width_root/2
        pos_y = self.height_screnn/2 - height_root/2
        geometry_root = '%dx%d+%d+%d' % (width_root,height_root,pos_x,pos_y)
        self.root.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuição do titulo
        self.root.configure(background= cores[2]) #Cor do plano de fundo da tela
        self.root.geometry(geometry_root) #Código que faz a tela abrir em modo tela cheia
        # self.root.attributes('-fullscreen', True) #Código que faz com que a tela fique em Fullscreen
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
        # self.bt_TFD = Button(self.frame, image= self.photo_bt_TFD, relief=FLAT, bd = 0) #Adicionando a imagem a um botão
        # # self.bt_TFD.config(command= self.abrir_janela22) #Adicionando a imagem a um botão
        # self.bt_TFD.place(relx= 0.549, rely=0.7, relwidth= 0.39, relheight= 0.19) #Localizando o botão na tela

        self.photo_bt_FARMARCIA = PhotoImage(file = bt[1]) #Imagem botão Farmacia
        self.bt_F = Button(self.frame, image= self.photo_bt_FARMARCIA, relief=FLAT, bd= 0) #Adicionando a imagem a um botão
        # self.bt_F.config(command = self.abrir_janela4)
        self.bt_F.place(relx= 0.07, rely=0.675, relwidth= 0.395, relheight= 0.22) #Localizando o botão na tela

        self.photo_bt_PREMIR = PhotoImage(file = bt[5]) #Imagem botão PREMIR    
        self.bt_premir = Button(self.frame, image = self.photo_bt_PREMIR, bd = 0, relief=FLAT) #Adicionando a imagem a um botão
        # self.bt_premir.config(command= self.abrir_janela3) #Adicionando a imagem a um botão
        self.bt_premir.place(relx= 0.547, rely=0.40, relwidth= 0.3965, relheight= 0.21) #Localizando o botão na tela
        
        self.photo_BT_AUT_EXAMES = PhotoImage(file = bt[0]) #Imagem botão Autorização de Exames
        self.bt_Aut = Button(self.frame, image = self.photo_BT_AUT_EXAMES, bd = 0, relief=FLAT) #Adicionando a imagem a um botão
        # self.bt_Aut.config(command= self.abrir_janela21) #Adicionando a imagem a um botão
        self.bt_Aut.place(relx= 0.079, rely=0.41, relwidth= 0.389, relheight= 0.19) #Localizando o botão na tela


        ###Botões###
        self.photo_bt_FARMARCIA = PhotoImage(file = bt[1]) #Imagem botão Farmacia
        self.bt_F = Button(self.frame, image= self.photo_bt_FARMARCIA, relief=FLAT, bd= 0) #Adicionando a imagem a um botão
        # self.bt_F.config(command= self.abrir_janela4) #Adicionando a imagem a um botão
        self.bt_F.place(relx= 0.31, rely=0.675, relwidth= 0.395, relheight= 0.22) #Localizando o botão na tela

        self.photo_bt_PREMIR = PhotoImage(file = bt[5]) #Imagem botão PREMIR    
        self.bt_premir = Button(self.frame, image = self.photo_bt_PREMIR, bd = 0, relief=FLAT) #Adicionando a imagem a um botão
        # self.bt_premir.config(command= self.abrir_janela3) #Adicionando a imagem a um botão
        self.bt_premir.place(relx= 0.547, rely=0.40, relwidth= 0.3965, relheight= 0.21) #Localizando o botão na tela
        
        self.photo_BT_AUT_EXAMES = PhotoImage(file = bt[0]) #Imagem botão Autorização de Exames
        self.bt_Aut = Button(self.frame, image = self.photo_BT_AUT_EXAMES, bd = 0, relief=FLAT) #Adicionando a imagem a um botão
        # self.bt_Aut.config(command= self.abrir_janela21) #Adicionando a imagem a um botão
        self.bt_Aut.place(relx= 0.079, rely=0.41, relwidth= 0.389, relheight= 0.19) #Localizando o botão na tela


Application()