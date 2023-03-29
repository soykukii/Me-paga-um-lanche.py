import tkinter as tk
import random

root = tk.Tk()
root.geometry('200x200')

def hover(event):
    x = random.randint(20, 180)
    y = random.randint(20, 180)
    nao.place(x=x, y=y)

    def msg():
        message = tk.Label(root, text = 'Obrigado!')
        message.place(x=70, y=120, relx=0, rely=0)

a = tk.Label(root, text='Me paga um lanche?')
a.pack(anchor='n', pady=20)

nao = tk.Button(root, text='Não')
nao.place(x=140, y=80)
nao.bind('<Enter>', hover)

sim = tk.Button(root, text='Sim', command='msg')
sim.place(x=25, y=80, relx=0, rely=0)

root.mainloop()

# Código muito legal e funcional feito por mim...
# Não precisa baixar a biblioteca 'tkinter' e nem a 'random', elas já são nativas do Python!
