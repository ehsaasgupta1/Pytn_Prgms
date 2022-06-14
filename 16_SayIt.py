# First you gotta download the module so called "pyttsx3" using pip.
import pyttsx3
engine = pyttsx3.init()
engine.say("If you don't know now you know")
engine.runAndWait()