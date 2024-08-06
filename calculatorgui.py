from tkinter import Tk, Entry, Button, END

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=20, fg="blue")
e.grid(row=0, column=0, columnspan=20, padx=20, pady=30)

# declaring functions
def buttonclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def button_add():
    firstnum = e.get()
    global fnum
    global math
    math = "add"
    fnum = float(firstnum)
    e.delete(0, END)

def equal():
    secondnum = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, fnum + float(secondnum))
    elif math == "sub":
        e.insert(0, fnum - float(secondnum))
    elif math == "mul":
        e.insert(0, fnum * float(secondnum))
    elif math == "div":
        e.insert(0, fnum / float(secondnum))  
    elif math == "pow":
        e.insert(0, fnum ** float(secondnum))

# functions that calculate
def sub():
    firstnum = e.get()
    global fnum
    global math 
    math = "sub"
    fnum = float(firstnum)
    e.delete(0, END)
    return   

def mul():
    firstnum = e.get()
    global fnum
    global math
    math = "mul"
    fnum = float(firstnum)
    e.delete(0, END)
    return

def div():
    firstnum = e.get()
    global fnum
    global math
    math = "div"
    fnum = float(firstnum)
    e.delete(0, END)
    return

def pow():
    firstnum = e.get()
    global fnum
    global math
    math = "pow"
    fnum = float(firstnum)
    e.delete(0, END)
    return

# creation of the buttons
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonclick(1)) 
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonclick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonclick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonclick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonclick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonclick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonclick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonclick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonclick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonclick(0))
button_dot = Button(root, text=".", padx=40, pady=20, command=lambda: buttonclick("."))

# operations
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=40, pady=20, command=sub)
button_mul = Button(root, text="*", padx=40, pady=20, command=mul)
button_div = Button(root, text="/", padx=40, pady=20, command=div)
button_equal = Button(root, text="=", padx=40, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=40, pady=20, command=clear)
button_pow = Button(root, text="pow", padx=40, pady=20, command=pow)
button_quit = Button(root, text="Exit", padx=40, pady=20, command=root.quit)

# put buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)

button_add.grid(row=4, column=2)
button_sub.grid(row=5, column=0)
button_mul.grid(row=5, column=1)
button_div.grid(row=5, column=2)
button_clear.grid(row=6, column=0)
button_equal.grid(row=6, column=1)
button_pow.grid(row=6, column=2)
button_quit.grid(row=6, column=3)

root.mainloop()