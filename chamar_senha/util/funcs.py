from util.modules import *
from util.models import *

senha, senha_anterior,senha_default, atendimento, prioritario = (0,0,0,0,0)
config = ConfigParser()
get_dir = os.path.dirname(__file__)
config.read(fr'{get_dir}\settings.ini')
server_config = dict(config['server'])
setor = server_config['setor']

class Functions():
    #função para chamar senhas na tabela fila_espera
    def chamar_proxima(self,opc):
        global data, setor,senha_anterior,senha_default, senha, atendimento, prioritario
        senha_anterior = senha_default
        if setor == 'PREMIR':
            sql = f'SELECT senha FROM fila_espera WHERE setor = "{setor}" AND status = "ESPERA" AND opcao="{opc}";'
        else:
            sql = f'SELECT senha FROM fila_espera WHERE setor = "{setor}" AND status = "ESPERA";'
        
        resultado = consulta_database(sql)

        if resultado != None:
            if prioritario < 2:
                atendimento = 'preferencial'
                prioritario += 1
            elif prioritario ==2:
                # a cada duas preferencial chama uma convencional
                atendimento = 'convencional'
                prioritario = 0

            sql = f'SELECT senha FROM fila_espera WHERE id IN (SELECT MIN(id) FROM fila_espera WHERE setor = "{setor}" AND atendimento = "{atendimento}" AND status = "ESPERA");'
            
            senha = consulta_database(sql)
            if senha == None:
                self.chamar_proxima()
            else:
                for i in senha:
                    senha = i['senha']

                sql = f'UPDATE fila_espera SET status = "CHAMADA" WHERE senha = "{senha}"'
                update_databe(sql)
                data = [senha,setor]
                chamar_senha(data)
                # display = senha
                self.display_senha.config(text=str(senha))
                senha_default = senha

        else:
            messagebox.showinfo('Atenção!','Não há senhas para chamar')

    # função para chamar senha anterior
    def chamar_anterior(self):
        global senha_anterior
        data = [senha_anterior,setor]
        chamar_senha(data)
        self.display_senha.config(text=str(senha_anterior))
    
    #função para chamar novamente senha atual
    def chamar_novamente(self):
        senha = self.display_senha.cget('text')
        data = [senha,setor]
        chamar_senha(data)

    # atualização da barra de status
    def update_statubar(self):
        global setor
        
        if setor == 'PREMIR':  
            mul = consulta_fila(f'SELECT count(senha) as total FROM fila_espera WHERE setor="{setor}" AND status = "ESPERA" AND opcao = "mul";')
            con = consulta_fila(f'SELECT count(senha) as total FROM fila_espera WHERE setor="{setor}" AND status = "ESPERA" AND opcao = "con";')
            ult = consulta_fila(f'SELECT count(senha) as total FROM fila_espera WHERE setor="{setor}" AND status = "ESPERA" AND opcao = "ult";') 
            self.display_espera.config(text=f'Fila de espera - Multiprofissionais: {mul} / Consultas: {con} / Ultrassom: {ult}')
        else:
            con = consulta_fila(f'SELECT count(senha) as total FROM fila_espera WHERE setor="{setor}" AND status = "ESPERA";')
            self.display_espera.config(text=f'Fila de espera {setor}: {con}')
            
        self.display_espera.after(200, self.update_statubar)

