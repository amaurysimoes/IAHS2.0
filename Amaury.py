#Caso apresente agum problema com o interpretador, instalar o 3.6.2 64bits
#O interpretador em uso é o 3.11.2
import pyttsx3 #Biblioteca gratuita "Zira"
import datetime
#Para utilizar este reconhecimento de fala, vai precisar sempre de uma conexão de internet
import speech_recognition as sr #Responsável pelo reconhecimento de fala só trabalha on-line

texto_fala = pyttsx3.init()

# Definição para criar função em python = def
def falar(audio):
    rete = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate", 180)#Velocidade da fala
    voices = texto_fala.getProperty('voices')
    #Quando abre chaves [] , faz-se atribuição de lista em qualquer linguagem
    texto_fala.setProperty('voice', voices[2].id)#variar de ids: [0] [1] [2] mudar vozes
    #Ao pressionar o Tab e colocar o texto no recuo, tudo vai para dentro da função.
    texto_fala.say(audio)
    texto_fala.runAndWait()
#falar("Teste de fala") - Exemplo anterior

def tempo():
    Tempo = datetime.datetime.now().strftime("%I:%M")
    #Tempo = datetime.datetime.now().strftime("%I:%M:%S") - hora, minutor e segundo
    falar("A hora atual é:")
    falar(Tempo)
#tempo() - Exemplo anterior

def data():
    ano  = str(datetime.datetime.now().year)
    mes = str(datetime.datetime.now().month)
    dia = str(datetime.datetime.now().day)
    falar("Data atual é:")
    falar(dia)
    falar("de" + mes)
    falar("de" + ano)
#tempo()
#data() - Exemplo anterior

def bem_vindo():
    falar("Oi Amaury.")
    tempo()
    data()

    hora = datetime.datetime.now().hour

    if hora >= 6 and hora < 12:
        falar("bom dia")
    elif hora >= 12 and hora < 18:
        falar("boa tarde")
    elif hora >= 18 and hora <= 24:
        falar("boa noite")
    else:
        falar("boa madrugada")
    falar("Alguma solicitação?")
#bem_vindo() - Exemplo anterior


#instalar o: #pip install pyaudio
def microne():
    # r = Tipo de dados que já vem na biblioteca speech
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Reconhecendo...")
        comando = r.recognize_google(audio,language='pt-br')
        print(comando)

    except Exception as e:
        print(e)
        falar("Repita a informação")

        return "None"
    
    return comando

#microne() - Exemplo anterior

if __name__== "__main__":
    bem_vindo()

    while True:
        print("Escutando..")
        comando = microne().lower()

        if 'Como você está' in comando:
            falar("Estou bem")
            falar("Como posso ajudar?")

        if 'hora' in comando:
            tempo()

        elif 'data' in comando:
            data()

#Procurar o restante das aulas