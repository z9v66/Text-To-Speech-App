
import pyttsx3
def speak_text(text,rate,volume):

    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine

