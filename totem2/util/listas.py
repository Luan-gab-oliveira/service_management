import os
from util.modulos import *

###Definição de Horarios###
horario = [
    "13:40",
    "13:30",
    "08:00",
    "07:40"
]
###Definindo variaveis para senha###
set = [
    "TFD",
    "Cartão SUS"
    ]
opc = [
    "TFD", #TFD
    "SUS"  #Cartão SUS
    ]
###Definindo variaveis para tipo de atendimento###
atend = [
    "preferencial", 
    "convencional"
    ]

###Definindo variavel com o nome do local fonte dos arquivos###
get_dir = os.getcwd()+ r'\imagens'

###Definindo Variaveis para Botões e seus diretorios###

#Diretorios para os botões
btCSUS = fr"{get_dir}\Botões\btCSUS.png"
btTFD = fr"{get_dir}\Botões\btTFD.png"
btconv = fr"{get_dir}\Botões\btconv.png"
btpref = fr"{get_dir}\Botões\btpref.png"
btvoltar = fr"{get_dir}\Botões\btvoltar.png"

#Atribuindo Lista de Botões 
bt = [ 
    btCSUS,
    btTFD,
    btpref,
    btconv,
    btvoltar
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

###Definindo variaveis para fontes
fonte0 = tkFont.Font(family= "Arial", size= 16, weight= "bold")

fontes = [
    fonte0
]