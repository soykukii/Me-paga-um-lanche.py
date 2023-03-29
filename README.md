# Me-paga-um-lanche.py
import tkinter as Lanche
import random

root = Lanche.Tk()
root.geometry('200x200')

def hover(event):
    x = random.randint(20, 180)
    y = random.randint(20, 180)
    nao.place(x=x, y=y)

    def msg():
        message = Lanche.Label(root, text = 'Obrigado!')
        message.place(x=70, y=120, relx=0, rely=0)

a = Lanche.Label(root, text='Me paga um lanche?')
a.pack(anchor='n', pady=20)

nao = Lanche.Button(root, text='Não')
nao.place(x=140, y=80)
nao.bind('<Enter>', hover)

sim = Lanche.Button(root, text='Sim', command='msg')
sim.place(x=25, y=80, relx=0, rely=0)

root.mainloop()
