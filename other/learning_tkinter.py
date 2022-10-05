from tkinter import *

def clicked():
    lbl.configure(text='ПОЕХАЛИ!')

window = Tk()
window.geometry('350x350')
window.title('Добро пожаловать в игру "Крестики-нолики"!')
lbl = Label(window, text = 'Hello', font=('Times New Roman', 20))
lbl.grid(column = 0, row = 0)
strt_btn = Button(window, text='Начать игру!', bg ='light blue', command=clicked)
strt_btn.grid(column=1, row=0)
window.mainloop()


