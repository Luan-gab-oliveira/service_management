from modules import *

def voice(senha):
   data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
   try:
      file_voice = f'Media\\Voices\\{senha}.mp3'
      texto = fr'Senha {senha}, favor dirigir-se ao local de atendimento!'
      tts = gtts.gTTS(texto, lang='pt-br')
      tts.save(file_voice)
   except:
      i += 1
      file_voice = f'Media\\Voices\\{senha}{data}.mp3'
      texto = fr'Senha {senha}, favor dirigir-se ao local de atendimento!'
      tts = gtts.gTTS(texto, lang='pt-br')
      tts.save(file_voice)
   
   playsound(file_voice)  
   os.remove(file_voice)

voice('P.FAE008')