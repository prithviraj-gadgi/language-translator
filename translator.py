import tkinter as tk
from tkinter import ttk
from methods import MyTranslator

app = tk.Tk()
app.geometry('350x510')
app.title('Language Translator')
app.resizable(0, 0)
app.config(bg='gray')

def get():
    s = srcLangs.get()
    d = destLangs.get()
    message = sourceText.get(1.0, tk.END)
    translator = MyTranslator()
    text = translator.run(txt=message, src=s, dest=d)
    destText.delete(1.0, tk.END)
    destText.insert(tk.END, text)

appName = tk.Label(app, text='My Translator', font=('arial', 20), bg='powderblue', fg='black', height=2)
appName.pack(side=tk.TOP, fill=tk.BOTH, pady=0)
tk.Label(app, text='Beta', bg='powderblue', fg='gray').place(x=250, y=45)

sourceText = tk.Text(app, font=('arial', 10), height=11, wrap=tk.WORD, bg='#FCF5D8')
sourceText.pack(side=tk.TOP, padx=5, pady=5)

transBtn = tk.Button(app, text='Translate', font=('arial', 10, 'bold'), fg='red', bg='white', activebackground='green', relief=tk.GROOVE, command=get)
transBtn.pack(side=tk.TOP, pady=15)

langs = MyTranslator().langs

srcLangs = ttk.Combobox(app, values=langs, width=10)
srcLangs.place(x=30, y=280)
srcLangs.set('english')

destLangs = ttk.Combobox(app, values=langs, width=10)
destLangs.place(x=240, y=280)
destLangs.set('hindi')

destText = tk.Text(app, font=('arial', 10), height=11, wrap=tk.WORD, bg='#FCF5D8')
destText.pack(side=tk.TOP, padx=5, pady=5)

app.mainloop()
