import os
import win32com.client as wc
speak = wc.Dispatch("SAPI.SpVOICE")

if __name__ == '__main__':
    x=input("text_to_speech: ")
    speak.Speak(x)




