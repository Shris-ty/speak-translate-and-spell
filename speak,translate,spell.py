import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
from textblob import TextBlob
from deep_translator import GoogleTranslator

root = tk.Tk()
root.geometry("600x600")
root.resizable(False, False)

img = Image.open(r"C:\\Users\\Lenovo\\OneDrive\\Pictures\\Saved Pictures\\IMG1.PNG").resize((600, 600))
final_img = ImageTk.PhotoImage(img)

labelx = tk.Label(root, image=final_img, bg="black")
labelx.place(x=20, y=20)

def speak():
    text = e1.get()
    if text.strip() != "":
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        listbox.insert(tk.END, f"Spoken: {text}")

def spelling():
    text = e1.get()
    if text.strip() != "":
        try:
            blob = TextBlob(text)
            corrected = blob.correct()
            corrected_text = str(corrected)

    
            e1.delete(0, tk.END)
            e1.insert(0, corrected_text)

            
            listbox.insert(tk.END, f"Original: {text}")
            listbox.insert(tk.END, f"Corrected: {corrected_text}")
        except Exception as e:
            listbox.insert(tk.END, f"Error: {e}")


def clear():
    e1.delete(0, tk.END)

def history(entry):
    listbox.insert(tk.END, entry)

def clr_history():
    listbox.delete(0, tk.END)


LANGUAGES = {
    "HINDI": "hi",
    "ENGLISH": "en",
    "FRENCH": "fr",
    "SPANISH": "es",
    "CHINESE": "zh-CN",
    "GERMAN": "de"
}

selected_lang = tk.StringVar()
selected_lang.set("HINDI")  


lang_menu = tk.OptionMenu(root, selected_lang, *LANGUAGES.keys())
lang_menu.config(font=("arial", 10), bg="white", fg="black")
lang_menu.place(x=400, y=120)

def translate():
    text = e1.get()
    if text.strip() != "":
        lang_code = LANGUAGES[selected_lang.get()]
        translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
        listbox.insert(tk.END, f"Translated to {selected_lang.get()}: {translated}")

root.title("speak,spell check,history")

l1 = tk.Label(root, text="text", bg="white", fg="black", font="arial 25 bold")
l1.place(x=50, y=90)

e1 = tk.Entry(root, width=40, font="arial 10 bold")
e1.place(x=150, y=90)

b1 = tk.Button(root, text="SPEAK", font="arial 13 bold", bg="sky blue", fg="black", cursor="hand2", command=speak)
b1.place(x=100, y=160)

b2 = tk.Button(root, text="CLEAR", bg="red", fg="black", font="arial 13 bold", command=clear, cursor="hand2")
b2.place(x=200, y=160)

b3 = tk.Button(root, text="SPELLING", bg="purple", fg="white", font="arial 13 bold", command=spelling, cursor="hand2")
b3.place(x=290, y=160)

b4 = tk.Button(root, text="CLEAR", font="arial 16 bold", bg="green", fg="white", command=clr_history, cursor="hand2")
b4.place(x=230, y=530)

l2 = tk.Label(root, text="HISTORY", font="arial 16 bold", bg="white", fg="black")
l2.place(x=230, y=230)

listbox = tk.Listbox(root, width=45, height=10, font="arial 15")
listbox.place(x=50, y=280)


b5 = tk.Button(root, text="TRANSLATOR", bg="light green", fg="black", font="arial 13 bold", cursor="hand2", command=translate)
b5.place(x=400, y=160)

root.mainloop()
