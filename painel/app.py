'''
versão playsound==1.2.2
'''
from modules import *

get_dir = os.path.dirname(__file__)
logs_errors = 'logs.txt'
fonts = ['Helvetica','Arial']
coolors = [
    '#000000', #0 - Black
    '#E7E7E7', #1 - Platinum
    '#ffffff', #2 - White
    '#686963', #3 ~ dim gray
    '#004568', #4 ~ Indigo Dye
    '#477C93', #5 ~ teal blue
    '#618DA0', #6 ~ light slate gray
    '#7B9EB3', #7 ~ air superiority
    '#FCA311'  #8 - Orange Web
    ]

@contextmanager
def connect_server():
    config = ConfigParser()
    get_dir = os.path.dirname(__file__)
    config.read('app.ini')
    server_config = dict(config['server'])
    conexao = pymysql.connect(
        host=server_config['host'],
        user=server_config['user'],
        password=server_config['password'],
        db=server_config['db'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try: #Tratamento de exeções
        yield conexao 
    finally: #Executa independente da exeção 
        conexao.close() #Finaliza conexão


class Functions():

    def validar_mac(self):
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        ip = socket.gethostbyname(socket.gethostname())

        with connect_server() as conexao:
            with conexao.cursor() as cursor:
                if cursor.execute(f'SELECT * FROM panels WHERE mac = "{mac_address}";')>0:
                    resultado = cursor.fetchall()
                    cursor.execute(f'UPDATE panels SET host = "{ip}" WHERE mac = "{mac_address}";')
                    conexao.commit()
                else:
                    cursor.execute(f'INSERT INTO panels (host, port, mac) VALUES ("{ip}", "50000", "{mac_address}");')
                    conexao.commit()

    def tread_start_server(self):
        t1 = threading.Thread(target=self.start_conect)
        t1.daemon = TRUE
        t1.start()


    def start_conect(self):
        config = ConfigParser()
        config_file = 'app.ini'
        try:
            with open(config_file, 'r') as file:
                file.close
        except IOError:
            config['config'] = {
                'local': 'local',
                'port': '50000'
                }
            with open(config_file, 'w', encoding='UTF-8') as file:
                config.write(file)
        
        config.read(config_file)
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = int(config['config']['port'])
        setor = str(config['config']['local'])

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            senha_atual = ''
            chamada0 = ''
            chamada1 = ''
            chamada2 = ''
            chamada3 = ''
            while True:
                try:
                    conn, addr = s.accept()
                    data = conn.recv(1024)    
                    if not data:
                        data = 0
                    else:
                        data = eval(data.decode())
                        senha = str(data[0])
                        senha_local = str(data[1])
                        if senha_local == setor:
                            
                            try: 
                                playsound(r'Media\\toque.wav',0)
                            except Exception as e:
                                data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                                try:
                                    with open(logs_errors, 'a') as file:
                                        file.write(f'{data}: {e}\n')
                                except IOError:
                                    with open(logs_errors, 'w') as file:
                                        file.write(f'{data}: {e}\n')

                            self.display_senha1.config(text=senha)
                            self.display_local.config(text=senha_local)

                        if senha != senha_atual:    
                            senha_atual = senha                            
                            chamada3 = chamada2
                            chamada2 = chamada1
                            chamada1 = chamada0
                            chamada0 = f'{senha} - {senha_local}'

                            self.display_senha2.config(text=senha)
                            self.display_local2.config(text=senha_local)
                            self.display_senha3.config(text=chamada1)
                            self.display_senha4.config(text=chamada2)
                            self.display_senha5.config(text=chamada3)
                        
                        if senha_local == setor:
                            self.voice(senha)
                        
                except Exception as e:
                    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    
                    try:
                        with open(logs_errors, 'a') as file:
                            file.write(f'{data}: {e}\n')
                    except IOError:
                        with open(logs_errors, 'w') as file:
                            file.write(f'{data}: {e}\n')
                    
                    

    def voice(self,senha):
        data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        try:
            file_voice = f'Media\\Voices\\{senha}.mp3'
            texto = fr'Senha {senha}, favor dirigir-se ao local de atendiemento!'
            tts = gtts.gTTS(texto, lang='pt-br')
            tts.save(file_voice)
        except:
            i += 1
            file_voice = f'Media\\Voices\\{senha}{data}.mp3'
            texto = fr'Senha {senha}, favor dirigir-se ao local de atendiemento!'
            tts = gtts.gTTS(texto, lang='pt-br')
            tts.save(file_voice)
        
        playsound(file_voice)  
        os.remove(file_voice)
        
    def relogio(self):
        self.data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.label_data.after(200, self.relogio)
        self.label_data.config(text=str(F'São Francisco do Sul - SC    {self.data_atual}'))


class PainelGUI(Functions):
    def __init__(self):
        self.root = tk.Tk()
        self.width_screnn = self.root.winfo_screenwidth()
        self.height_screnn = self.root.winfo_screenheight()   
        self.root.bind("<F11>", self.toggleFullScreen)
        self.root.bind("<Escape>", self.quitFullScreen)
        self.make_root()
        self.make_frame()
        self.widgets_frame1()
        self.widgets_frame2()
        self.widgets_frame3()
        self.widgets_frame4()
        self.validar_mac()
        self.tread_start_server()
        self.relogio()
        self.root.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.root.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.root.attributes("-fullscreen", self.fullScreenState)

    def make_root(self):
        width_root = 1280
        height_root = 700
        pos_x = self.width_screnn/2 - width_root/2
        pos_y = self.height_screnn/2 - height_root/2
        geometry_root = '%dx%d+%d+%d' % (width_root,height_root,pos_x,pos_y)
        icon = fr'{get_dir}\images\sfs.ico'
        self.root.title('Painel de senhas')
        self.root.iconbitmap(default=icon)
        self.root.geometry(geometry_root)
        self.root.maxsize(width=self.width_screnn, height=self.height_screnn)
        self.root.minsize(width=800, height=600)
        self.root.resizable(True, True)
        self.root.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.root.config(background=coolors[1])

    def make_frame(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.config(background=coolors[1])
        self.frame_1.place(rely=0.0, relwidth=1, relheight=0.15)

        self.frame_2 = Frame(self.root)
        self.frame_2.config(background=coolors[1])
        # self.frame_2.place(rely=0.16, relwidth=0.68, relx=0.01, relheight=0.73)
        self.frame_2.place(rely=0.15, relwidth=0.7, relheight=0.75)

        self.frame_3 = Frame(self.root)
        self.frame_3.config(background=coolors[1])
        self.frame_3.place(relx=0.7, rely=0.15 ,relwidth=0.3, relheight=0.85)

        self.frame_4 = Frame(self.root)
        self.frame_4.config(background=coolors[0])
        self.frame_4.place(rely=0.90, relwidth=1, relheight=0.1)

    def widgets_frame1(self):
        self.label = Label(self.frame_1, text='SECRETARIA MUNICIPAL DE SAÚDE')
        self.label.config(
            font=(fonts[0],40, 'bold'), foreground=coolors[2],
            background=coolors[4], justify='center'
        )
        self.label.place(relwidth=1,relheight=1)

        self.img_sfs = PhotoImage(file=f'{get_dir}\images\sfs.png')
        self.img = Label(self.frame_1, image=self.img_sfs, bd=0)
        self.img.config(background=coolors[4])
        self.img.place(relx=0.01, rely=0.2)

        self.img_sus = PhotoImage(file=f'{get_dir}\images\sus.png')
        self.img = Label(self.frame_1, image=self.img_sus, bd=0)
        self.img.config(background=coolors[4])
        self.img.place(relx=0.88, rely=0.2)

    def widgets_frame2(self):
        self.label = Label(self.frame_2, text='Senha')
        self.label.config(
            font=(fonts[0],50,'bold'), foreground=coolors[5],
            background=coolors[1], justify='center', anchor='s'
        )
        self.label.place(rely=0.10,relwidth=1,relheight=0.10)
        
        # display senha chamada/atualizar
        self.display_senha1 = Label(self.frame_2, text='0000')
        self.display_senha1.config(
            font=(fonts[0],100,'bold'), foreground=coolors[4],
            background=coolors[1], justify='center', anchor='n'
        )
        self.display_senha1.place(rely=0.2,relwidth=1,relheight=0.3)

        self.label = Label(self.frame_2, text='Local')
        self.label.config(
            font=(fonts[0],50,'bold'), foreground=coolors[5],
            background=coolors[1], justify='center', anchor='s'
        )
        self.label.place(rely=0.5,relwidth=1,relheight=0.10)

        self.display_local = Label(self.frame_2, text='-')
        self.display_local.config(
            font=(fonts[0],100,'bold'), foreground=coolors[4],
            background=coolors[1], justify='center', anchor='n'
        )
        self.display_local.place(rely=0.6,relwidth=1,relheight=0.3)

        self.label = Label(self.frame_2, text='Favor dirigir-se ao local de atendiemento!')
        self.label.config(
            font=(fonts[0],30), foreground=coolors[0],
            background=coolors[1], justify='center'
        )
        self.label.place(rely=0.9,relwidth=1,relheight=0.10)
    
    def widgets_frame3(self):
        self.label = Label(self.frame_3, text='Senha chamada')
        self.label.config(
            font=(fonts[0],22), foreground=coolors[2],
            background=coolors[0], justify='center'
        )
        self.label.place(rely=0 ,relwidth=1, relheight=0.05)

         # label, senha chamada
        self.label = Label(self.frame_3, text='Senha')
        self.label.config(
            font=(fonts[0],32), foreground=coolors[1],
            background=coolors[4], justify='center', anchor='s'
        )
        self.label.place(rely=0.05, relwidth=1,relheight=0.11)

        # dislpay, senha chamada
        self.display_senha2 = Label(self.frame_3, text='0000')
        self.display_senha2.config(
            font=(fonts[0],55,'bold'), foreground=coolors[2],
            background=coolors[4], justify='center', anchor='n'
        )
        self.display_senha2.place(rely=0.16, relwidth=1,relheight=0.12)

        # label, local/balcão
        self.label = Label(self.frame_3, text='Local')
        self.label.config(
            font=(fonts[0],32), foreground=coolors[1],
            background=coolors[4], justify='center', anchor='s'
        )
        self.label.place(rely=0.28, relwidth=1,relheight=0.06)

        # dislpay, local/balcão
        self.display_local2 = Label(self.frame_3, text='-')
        self.display_local2.config(
            font=(fonts[0],55,'bold'), foreground=coolors[2],
            background=coolors[4], justify='center', anchor='n'
        )
        self.display_local2.place(rely=0.34, relwidth=1,relheight=0.15)

        # label ultimas chamadas
        self.label = Label(self.frame_3, text='últimas chamadas')
        self.label.config(
            font=(fonts[0],22), foreground=coolors[2],
            background=coolors[0], justify='center'
        )
        self.label.place(rely=0.49, relwidth=1,relheight=0.05)

        # display senha 1
        self.display_senha3 = Label(self.frame_3, text='0000')
        self.display_senha3.config(
            font=(fonts[0],40,'bold'), foreground=coolors[0],
            background=coolors[5], justify='center'
        )
        self.display_senha3.place(rely=0.54 ,relwidth=1,relheight=0.12)

        # diplay chamada 3
        self.display_senha4 = Label(self.frame_3, text='0000')
        self.display_senha4.config(
            font=(fonts[0],40,'bold'), foreground=coolors[0],
            background=coolors[6], justify='center'
        )
        self.display_senha4.place(rely=0.66,relwidth=1,relheight=0.12)    

        # diplay chamada 3
        self.display_senha5 = Label(self.frame_3, text='0000')
        self.display_senha5.config(
            font=(fonts[0],40,'bold'), foreground=coolors[0],
            background=coolors[7], justify='center'
        )
        self.display_senha5.place(rely=0.78 , relwidth=1,relheight=0.12)
    
    def widgets_frame4(self):
        self.label_data = Label(self.frame_4, text='São Francisco do Sul - SC')
        self.label_data.config(
            font=(fonts[0],22), foreground=coolors[1],
            background=coolors[0], justify='center'
        )
        self.label_data.place(relwidth=1,relheight=1)

PainelGUI()