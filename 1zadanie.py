from tkinter import *
from tkinter import messagebox

def show_message():
    messagebox.showinfo("GUI Python", chislo.get())

root = Tk()
root.title("Simple GUI")
root.geometry("500x500")
chislo = numberinv()
message = IntVar()
message_entry = Entry(textvariable=message)
val = message_entry.get()
int(val)
message_entry.place(relx=.5, rely=.1, anchor="c")
def numberinv():
    n=val.get()
    m = 0
    while n>0:
        m = m * 10 + n % 10
        n = n // 10 # делим нацело
        return m
    #print("Перевернутое число:",m)#добавил текст для понятности   



btn = Button(text="start", command=show_message)
btn.pack()


root.mainloop()
