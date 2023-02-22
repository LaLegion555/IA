#hecho por LaLegion555
import speech_recognition as sr
import pyttsx3
import pywhatkit

name='ana'
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say ("Hola Soy "+ name +" tu asistente virtual, en que puedo ayudarte?")
engine.runAndWait()
def talk(text):
    engine.say (text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source :
            print ("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
            #else:
            #    talk('Por favor di mi nombre, si no dices mi nombre no podré ayudarte, por si olvidaste mi nombre te lo recordaré, me llamo '+name)
    except:
        pass
    return rec

def run():
    rec=listen()
    def buscar():
        q = rec.replace('busca', '')
        talk('estos son los resultados que encontré')
        pywhatkit.search(q)
    def music():#'reproduce' in rec
        music = rec.replace('reproduce', '')
        talk('Disfruta de esta canción '+ music)
        pywhatkit.playonyt(music)
    def inter():
        #bienvenido
        if 'como estas' in rec or 'como esta' in rec or 'como estais' in rec:
            talk('estoy muy bien y usted?, como esta?')
            listen()
            if 'bien' in rec:
                talk('Me alegro de que esté bien, puedo ayudarte en algo más?')
            elif 'mal' in rec:
                talk('no estés triste, las cosas pasan por algo')
            elif '' in rec:
                talk('al parecer no quiere conversar conmigo, en ese caso me retiro por el momento, adios')
            else:
                talk('no logro entenderte')
        elif 'girlfriend' in rec or 'enamorada' in rec or 'boyfriend' in rec or 'enamorado' in rec or 'flaca' in rec or 'flaco' in rec:
            talk('pero si la semana pasada te engaño, aun asi quierez realizar la operación?')
            listen()
    if 'reproduce' in rec or 'play' in rec:
        music()
    elif 'como estas' in rec or 'como esta' in rec or 'como estais' in rec or 'girlfriend' in rec or 'enamorada' in rec or 'boyfriend' in rec or 'enamorado' in rec:
        inter()
    elif 'busca' in rec:
        buscar()
    else:
        talk('no puedo entenderte, por favor intenta de nuevo')
        listen()
        if 'reproduce' in rec or 'play' in rec:
            music()
        elif 'como estas' in rec or 'como esta' in rec or 'como estais' in rec or 'girlfriend' in rec or 'enamorada' in rec or 'boyfriend' in rec or 'enamorado' in rec:
            inter()
        elif 'busca' in rec:
            buscar()
        else:
            talk('no pude entenderte')
            print(rec)


run()

#hecho por LaLegion555
