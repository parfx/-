from tkinter import *
from tkinter import messagebox

def show_message():
    messagebox.showinfo("GUI Python", message.get())
root = Tk()
root.title("SIMPLE GUI")
root.geometry("500x500")
message = IntVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="Click me", command=show_message)

def number(n):
    m = 0
    while n > 0:
        m = m * 10 + n % 10
        n = m // 10 # делим нацело

        


btn = Button(text="Start", command=show_message)
btn.pack()


root.mainloop()