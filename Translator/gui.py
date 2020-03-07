import tkinter as tk
from googletrans import Translator
win = tk.Tk()
win.title("TRANSLATOR")
win.geometry("200x100")
def trans():
    word = entry.get()
    trans = Translator(service_urls=["translate.google.com"])
    translation = trans.translate(word,dest="en")
    label2 = tk.Label(win, text=f'Translated word : {translation.text}')
    label2.grid(row=2,column=0)
label = tk.Label(win, text="Enter Text:")
label.grid(row=0,column=0)
entry=tk.Entry(win)
entry.grid(row=1,column=0)
button=tk.Button(win,text='GO',command=trans)
button.grid(row=1,column=1)
win.mainloop()