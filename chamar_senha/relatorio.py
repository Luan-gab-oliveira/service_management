from util.modules import *
from util.gerar_doc import *

root = tk.Tk()
dir_app = os.path.dirname(__file__)
root.iconbitmap(fr"{dir_app}\sfs.ico")


fonte1 = tkFont.Font(family="Arial", size=16)                       #Definindo padrão de fonte
fonte2 = tkFont.Font(family="Arial", size=35, weight="bold")        #Definindo padrão de fonte
fonte3 = tkFont.Font(family="Arial", size=16, weight="bold")        #Definindo padrão de fonte
fonte4 = tkFont.Font(family="Arial", size=12, weight="bold")        #Definindo padrão de fonte
fonte5 = tkFont.Font(family="Arial", size=10)                       #Definindo padrão de fonte

fontes = [
    fonte1,     #fontes[0]
    fonte2,     #fontes[1]
    fonte3,     #fontes[2]
    fonte4,     #fontes[3]
    fonte5,     #fontes[4]
]

def center(win):
    win.update_idletasks()

    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    win.deiconify()

class Relatorio():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.labels()
        self.entries()
        self.widget()
        self.root.mainloop()
        pass
    def tela(self):
        self.root.title("Gerar Relatório")
        self.root.geometry("500x300")
        self.root.configure(background= "#A9A9A9")
        self.root.resizable(False,False)
        center(self.root)
    def frames(self):
        self.frame = Frame(self.root, bd=4, bg = "#ffffff")
        self.frame.place(anchor= 'center', relx= 0.5, rely=0.5, relwidth= 0.98, relheight= 0.98)
    def labels(self):
        global data
        data = datetime.now().strftime("%H:%M - %d/%m/%Y")
        self.label_title = Label(self.frame, bd = 0, text="Gerador de Relatorio de Atendimentos Mensal", background= "#ffffff")
        self.label_title.configure(font=fontes[2])
        self.label_title.place(anchor='center', relx= 0.5, rely= 0.2)

        self.mes = Label(self.frame, bd = 0, text="Escolha o mês: ", background= "#ffffff")
        self.mes.configure(font=fontes[0])
        self.mes.place(anchor='center', relx= 0.5, rely= 0.32)

        self.nome = Label(self.frame, bd = 0, text="Gerado por: ", background= "#ffffff")
        self.nome.configure(font=fontes[0])
        self.nome.place(anchor='center', relx= 0.5, rely= 0.53)

        self.data = Label(self.frame, bd= 0, bg= "#ffffff", text=f"Data e hora Atual: {data}")
        self.data.configure(font=fontes[4])
        self.data.place(anchor='center', relx= 0.5, rely= 0.9)
    def entries(self):
        self.mes_entrie = ttk.Combobox(state="readonly", values=("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"), justify="center")
        self.mes_entrie.configure(font= fontes[3])
        self.mes_entrie.place(anchor='center', relx= 0.5, rely= 0.43, relwidth=0.4, relheight= 0.08) 
        
        self.nome_entrie = Entry(self.frame, bd = 1, bg= "#ffffff", justify= "center")
        self.nome_entrie.configure(font= fontes[3])
        self.nome_entrie.place(anchor='center', relx= 0.5, rely= 0.63, relwidth=0.4, relheight= 0.08)           
    def widget(self):
        self.bt_gerar = Button(self.frame, text= "Gerar", command= self.gerar)
        self.bt_gerar.place(anchor='center', relx= 0.5, rely= 0.75, relwidth=0.2, relheight= 0.08)

    def gerar(self):
        consulta(self.mes_entrie.get(), self.nome_entrie.get())
        doc()

Relatorio()