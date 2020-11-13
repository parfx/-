<<<<<<< HEAD
from tkinter import *
 
clicks = 0
 
 
def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
 
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
 
btn = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()
 
root.mainloop()
=======
n = int(input("Введите число"))
m = 0
while n>0:
    m = m * 10 + n % 10
    n = n // 10 # делим нацело
print("Перевернутое число:",m)#добавил текст для понятности
>>>>>>> 1df61eda8338a2f156b7762928651772761723fc
