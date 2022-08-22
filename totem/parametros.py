<<<<<<< HEAD
from Modulos import *

root = tk.Tk()                                              #Variavel Princiapal das telas 
w, h = root.winfo_screenwidth(), root.winfo_screenheight()  #Variavel que pega as medidas da tela como referência
password = ''                                               #Senha para fechamento do programa
atendimento = ""                                            #Variavel para escolha do tipo de atendimento                                                                                                                                                                                                                                                                                                                                                 senha###
data = datetime.now().strftime('%H:%M')                     #Função para Coleta da Hora atual
tabela = 'fila_espera'                                      #Atribuindo nome da tabela 
tela = 0                                                    #Contagem do numero de telas 
# imprimir pdf
# impressora = "ZDesigner GC420d"
impressora = "Informatica_Samsung"
win32print.SetDefaultPrinter(impressora)
=======
from Modulos import *

root = tk.Tk()                                              #Variavel Princiapal das telas 
w, h = root.winfo_screenwidth(), root.winfo_screenheight()  #Variavel que pega as medidas da tela como referência
password = ''                                               #Senha para fechamento do programa
atendimento = ""                                            #Variavel para escolha do tipo de atendimento                                                                                                                                                                                                                                                                                                                                                 senha###
data = datetime.now().strftime('%H:%M')                     #Função para Coleta da Hora atual
tabela = 'fila_espera'                                      #Atribuindo nome da tabela 
tela = 0                                                    #Contagem do numero de telas 
# imprimir pdf
# impressora = "ZDesigner GC420d"
impressora = "Informatica_Samsung"
win32print.SetDefaultPrinter(impressora)
>>>>>>> c1c51330ed6477b7f729fd9e97ad68f3c53255be
