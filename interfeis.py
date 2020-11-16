from tkinter import *
from tkinter import messagebox

def remove():
    number = n.get()
    x = int(number)
    m = int(0)
    while x>0:
        m = m*10 + x%10
        x = x//10
    messagebox.showinfo("GUI Python", m)

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
 
n = IntVar()

message_entry = Entry(textvariable=n)
message_entry.place(relx=.5, rely=.1, anchor="c")
 
message_button = Button(text="Click Me", command=remove)
message_button.place(relx=.5, rely=.5, anchor="c")
 
root.mainloop()