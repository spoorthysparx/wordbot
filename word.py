import PySimpleGUI as sg
from utils import get_meaning, get_synonyms, get_antonyms 
greeting="Hello! I am a word bot, how can i help you\n"

layout=[
    [sg.Multiline(greeting, font=("Arial",14),size=(60,10),key="output")],
    [sg.InputText("", font=("Arial",14),size=(20,1),key="input",enable_events=True)],
    [sg.Button("Meaning", font=("Arial",14),bind_return_key=True,key="meaning"),sg.Button("synonyms", font=("Arial",14),bind_return_key=True,key="synonym"),
    sg.Button("antonyms",font=("Arial",14),bind_return_key=True,key="antonym"),sg.Button("clear",font=("Arial",14),bind_return_key=True,key="clear")]
]

def display_meaning(word):
    meaning=get_meaning(word)
    window["output"].print("WORD:",word)
    if meaning:
        window["output"].print("MEANING:",meaning)
    else:
        display_error("word in not found in corpus")

def display_synonym(word):
    synonym=get_synonyms(word)
    window["output"].print("WORD:",word)
    if synonym:
        window["output"].print("SYNONYM:",synonym)
    else:
        display_error("synonym is not found ")

def display_antonym(word):
    antonym=get_antonyms(word)
    window["output"].print("WORD:",word)
    if antonym:
        window["output"].print("ANTONYM:",antonym)
    else:
        display_error("antonym is not found ")


def display_error(message):
    window["output"].print("ERROR:"+ message, text_color="red")
    

if __name__ == "__main__":
    window=sg.Window("WORDNET",layout)
    while True:
        event,values=window.Read()
        if event== sg.WINDOW_CLOSED:
            break
        elif event=="meaning":
            display_meaning(values["input"])
        elif event=="synonym":
            display_synonym(values["input"])
        elif event=="antonym":
            display_antonym(values["input"])
        elif event=="clear":
            window.FindElement("output").update(greeting)
window.Close()