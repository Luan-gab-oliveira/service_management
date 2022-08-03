from app_modules import *
from app_client import *

get_dir = os.path.dirname(__file__)
icon = fr'{get_dir}\images\sfs.ico'
settings = f'{get_dir}\images\settings.png'
fonts = ['Helvetica','Arial']
coolors = [
    '#000000', #0 - Black
    '#E7E7E7', #1 - Platinum
    '#ffffff', #2 - White
    '#686963', #3 - dim gray
    '#004568', #4 - Indigo Dye
    '#477C93', #5 - teal blue
    '#618DA0', #6 - light slate gray
    '#7B9EB3', #7 - air superiority
    '#FCA311'  #8 - Orange Web
    ]

senha, senha_anterior,senha_default, atendimento, prioritario = (0,0,0,0,0)
config = ConfigParser()
config.read('app.ini')
server_config = dict(config['server'])
opcao = server_config['setor']

class Functions():
    #função para chamar senhas na tabela fila_espera
    def chamar_proxima(self):
        global data, opcao,senha_anterior,senha_default, senha, atendimento, prioritario
        senha_anterior = senha_default
        
        sql = f'SELECT senha FROM fila_espera WHERE opcao = "{opcao}" AND status = "ESPERA";'
        resultado = consulta_database(sql)
        if resultado != None:
            if prioritario < 2:
                atendimento = 'preferencial'
                prioritario += 1
            elif prioritario ==2:
                # a cada duas preferencial chama uma convencional
                atendimento = 'convencional'
                prioritario = 0

            sql = f'SELECT senha FROM fila_espera WHERE id IN (SELECT MIN(id) FROM fila_espera WHERE opcao = "{opcao}" AND atendimento = "{atendimento}" AND status = "ESPERA");'
            
            senha = consulta_database(sql)
            if senha == None:
                self.chamar_proxima()
            else:
                for i in senha:
                    senha = i['senha']

                sql = f'UPDATE fila_espera SET status = "CHAMADA" WHERE senha = "{senha}"'
                update_databe(sql)
                data = [senha,opcao]
                chamar_senha(data)
                # display = senha
                self.display_senha.config(text=str(senha))
                senha_default = senha

        else:
            messagebox.showinfo('Atenção!','Não há senhas para chamar')

    # função para chamar senha anterior
    def chamar_anterior(self):
        global senha_anterior
        data = [senha_anterior,opcao]
        chamar_senha(data)
        self.display_senha.config(text=str(senha_anterior))
    
    #função para chamar novamente senha atual
    def chamar_novamente(self):
        global data
        chamar_senha(data)

    # atualização da barra de status
    def update_statubar(self):
        global opcao
        sql = f'SELECT COUNT(senha) FROM fila_espera WHERE opcao="{opcao}" AND status = "ESPERA";'
        consulta = consulta_database(sql)
        if consulta != None:
            for i in consulta:
                espera = i['COUNT(senha)']
            self.display_espera.config(text=espera)
            self.display_espera.after(200, self.update_statubar)
        


class ChamarSenhaGUI(Functions):
    def __init__(self):
        global senha, data, local
        self.root = tk.Tk()
        self.make_root()
        self.make_frame()
        self.make_widgets()
        self.update_statubar()
        self.root.mainloop()

    def make_root(self):
        width_root = 800
        height_root = 500
        width_screnn = self.root.winfo_screenwidth()
        height_screnn = self.root.winfo_screenheight()
        pos_x = width_screnn/2 - width_root/2
        pos_y = height_screnn/2 - height_root/2
        geometry_root = '%dx%d+%d+%d' % (width_root,height_root,pos_x,pos_y)
        self.root.title('Chamar senha - Gerenciador de filas')
        self.root.iconbitmap(default=icon)
        self.root.geometry(geometry_root)
        self.root.maxsize(width=width_screnn, height=height_screnn)
        # self.root.minsize(width=800, height=600)
        self.root.resizable(False, False)
        self.root.config(background=coolors[1])
        # self.root.overrideredirect(True)
    
    def make_frame(self):
        # frame 1
        self.frame_1 = Frame(self.root)
        self.frame_1.config(background=coolors[2])
        self.frame_1.place(rely=0, relx=0,relwidth=0.5, relheight=0.9)

        # frame2
        self.frame_2 = Frame(self.root)
        self.frame_2.config(background=coolors[2])
        self.frame_2.place(rely=0, relx=0.5,relwidth=0.5, relheight=0.9)

        self.frame3 = Frame(self.root)
        self.frame3.config(background=coolors[4])
        self.frame3.place(rely=0.9, relx=0,relwidth=1, relheight=0.1)


    def make_widgets(self):
        ## whidgets frame_1
        self.label1 = Label(self.frame_1, text='Senha atual')
        self.label1.config(
            font=(fonts[0],32, 'bold'), foreground=coolors[4], background=coolors[2], justify='center')
        self.label1.place(relwidth=1,relheight=0.25)

        self.display_senha = Label(self.frame_1, text='0000')
        self.display_senha.config(
            font=(fonts[0],60, 'bold'), foreground=coolors[4],background=coolors[2], justify='center')
        self.display_senha.place(rely=0.25 ,relwidth=1,relheight=0.5)

        ## whidgets frame_2

        self.btn_proxima = Button(self.frame_2, text='Próxima senha')
        self.btn_proxima.config(
            font=(fonts[0], 14), justify='center',
            background=coolors[4], bd=0, foreground=coolors[2],
            cursor='hand2',
            highlightbackground=coolors[1], highlightcolor=coolors[1], activebackground=coolors[1], 
            highlightthickness=0,
            command=self.chamar_proxima
        )
        self.btn_proxima.place(rely=0.225, relx=0.15, relheight=0.15, relwidth=0.75)


        self.btn_anterior = Button(self.frame_2, text='Senha anterior')
        self.btn_anterior.config(
            font=(fonts[0], 14), justify='center',
            background=coolors[4], bd=0, foreground=coolors[2],
            cursor='hand2',
            highlightbackground=coolors[1], highlightcolor=coolors[1], activebackground=coolors[1], 
            highlightthickness=0,
            command=self.chamar_anterior
        )
        self.btn_anterior.place(rely=0.425, relx=0.15, relheight=0.15, relwidth=0.75)

        self.btn_novamente = Button(self.frame_2, text='Chamar novamente')
        self.btn_novamente.config(
            font=(fonts[0], 14), justify='center',
            background=coolors[5], bd=0, foreground=coolors[2],
            cursor='hand2',
            highlightbackground=coolors[1], highlightcolor=coolors[1], activebackground=coolors[1], 
            highlightthickness=0,
            command= self.chamar_novamente
        )
        self.btn_novamente.place(rely=0.625, relx=0.15, relheight=0.15, relwidth=0.75)

        self.label = Label(self.frame3, text=f'Fila de espera {opcao}:')
        self.label.config(
            font=(fonts[0],12, 'normal'),foreground=coolors[2], background=coolors[4], anchor='w')
        self.label.place(relx=0.02 ,relwidth=0.25 ,relheight=1)

        self.display_espera = Label(self.frame3, text='0')
        self.display_espera.config(
            font=(fonts[0],12, 'normal'),foreground=coolors[2], background=coolors[4], anchor='w')
        self.display_espera.place(relx=0.25 ,relwidth=0.1,relheight=1)



ChamarSenhaGUI()