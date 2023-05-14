#Alan de Jesus Fabian Garcia 
import speech_recognition as sr

# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

# Definir el archivo de audio a reconocer
archivo_audio = "ruta/al/archivo/de/audio.wav"

# Cargar el archivo de audio
with sr.AudioFile(archivo_audio) as source:
    # Leer el audio desde el archivo
    audio = r.record(source)

    try:
        # Utilizar el reconocimiento de voz de Google Speech-to-Text
        texto = r.recognize_google(audio, language="es-ES")

        # Imprimir el texto reconocido
        print("Texto reconocido:")
        print(texto)

    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")

    except sr.RequestError as e:
        print("Error en la solicitud al servicio de reconocimiento de voz de Google; {0}".format(e))
