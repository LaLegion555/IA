import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import os

horas_invertidas = 20

name = 'noni'

listener = sr.Recognizer()#captura de microfono

engine = pyttsx3.init()#captura la voz de google
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say ("Hola Soy "+ name +" tu asistente virtual, en que puedo ayudarte?")
engine.runAndWait()

def talk(text):#Noni habla
    engine.say(text)
    engine.runAndWait()

def listen(texto):#Entiende lo que dices
    try:
        with sr.Microphone() as source:
            print(texto)
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,'')
                print("Usted dijo: " + rec)                                                
    except:
        pass

    return rec

#Funciones de noni(lo que noni puede hacer)
def run():
    rec = listen('Esperando ordenes...')

    # Música y Videos en YT
    if 'reproduce' in rec or 'reproduzca' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)

    # su nombre
    elif 'nombre' in rec:
        talk('Mi nombre es: '+name)
        talk("puedo hacer algo más por ti?")
        sh = listen('Esperando ordenes...')
        if 'gracias' in sh or 'eso es todo' in sh or 'adios' in sh:
            talk('en ese caso me retiro por el momento, nos vemos')
        else:
            run()

    # Hora
    elif 'hora actual' in rec or 'que hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
        talk("puedo hacer algo más por ti?")
        sh = listen('Esperando ordenes...')
        if 'gracias' in sh or 'eso es todo' in sh or 'adios' in sh:
            talk('en ese caso me retiro por el momento, nos vemos')
        else:
            run()

    # Fecha
    elif 'fecha actual' in rec or 'día' in rec:
        fecha = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Hoy es " + fecha)
        talk("puedo hacer algo más por ti?")
        sh = listen('Esperando ordenes...')
        if 'gracias' in sh or 'eso es todo' in sh or 'adios' in sh:
            talk('en ese caso me retiro por el momento, nos vemos')
        else:
            run()

    # Buscador
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        talk('Buscando ' + order)
        pywhatkit.search(order)

    # Chistes
    elif 'dime algo gracioso' in rec or 'chiste' in rec:
        talk(pyjokes.get_joke('es'))
        talk('fue gracioso verdad?')
        talk("en fin, puedo hacer algo más por ti?")
        sh = listen('Esperando ordenes...')
        if 'gracias' in sh or 'eso es todo' in sh or 'adios' in sh:
            talk('en ese caso me retiro por el momento, nos vemos')
        else:
            run()

    # Ejecución de aplicaciones.exe
    elif 'ejecuta' in rec:
        order = rec.replace('ejecuta', '')
        talk('Abriendo ' + order)
        app = order+'.exe'
        os.system(app)

    # interactúa con el usuario
    elif 'cómo estás' in rec or 'cómo está' in rec or 'como estais' in rec or 'como estas' in rec or 'como esta' in rec:
        talk('estoy muy bien y usted?, como está?')
        sh = listen('Esperando ordenes...')
        if 'bien' in sh:
            talk('Me alegro de que esté bien, puedo ayudarte en algo más?')
            run()
        elif 'mal' in sh:
            talk('no estés triste, las cosas pasan por algo, para que te animes te contaré un chiste')
            talk(pyjokes.get_joke('es'))
            talk('fue gracioso verdad?')
            talk("en fin, puedo hacer algo más por ti?")
            sh = listen('Esperando ordenes...')
            if 'gracias' in sh or 'eso es todo' in sh or 'adios' in sh:
                talk('en ese caso me retiro por el momento, nos vemos')
            else:
                run()
        elif '' in sh:
            talk('al parecer no quiere conversar conmigo, en ese caso me retiro por el momento, adios')
        else:
            talk('no logro entenderte')
            run()
    elif 'girlfriend' in rec or 'enamorada' in rec or 'boyfriend' in rec or 'enamorado' in rec or 'flaca' in rec or 'flaco' in rec:
        talk('pero si la semana pasada te engañó, aun asi quiere realizar la operación?')
        sh = listen('Esperando ordenes...')
        if 'si' in sh:
            talk('Lo siento no puedo realizar la operación')
            talk('Espero que entienda que es por su bien')
            talk('para que no me vuelva a solicitar cosas que no debe me retiraré por el momento, si necesitas algo mucho más importante vuelve a llamarme')
        elif 'no' in sh:
            talk('me alegro de que haya cambiado de opinión')
            talk("en fin, puedo hacer algo más por ti?")
            sh = listen('Esperando ordenes...')
            if 'gracias' in sh or 'eso es todo' in sh or 'adios' in sh:
                talk('en ese caso me retiro por el momento, nos vemos')
            else:
                run()
        else:
            talk("No pude entender su petición, por favor realice nuevamente su pregunta")
            run()

    elif 'gracias' in rec or 'eso es todo' in rec or 'adios' in rec:
        talk('en ese caso me retiro por el momento, nos vemos')

    else:
        talk("No pude entender su petición, por favor realice nuevamente su pregunta")
        run()
    
# Iniciador
if __name__ == "__main__":
    run()