from tkinter import *
expr = ""

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="white")
    root.title("Simple Calculator")
    root.geometry('300x350')

    display = StringVar()
    entry = Entry(root, textvariable=display, font=('Arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4,
                  relief='ridge', justify='right')
    entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=10)

    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=20, ipadx=150)


    btn1 = Button(root, text='1', fg='black', bg='white',font=('Arial',9), command=lambda: press(1), height=2, width=8)
    btn1.grid(row=2, column=0)
    btn2 = Button(root, text='2', fg='black', bg='white',font=('Arial',9), command=lambda: press(2), height=2, width=8)
    btn2.grid(row=2, column=1)
    btn3 = Button(root, text='3', fg='black', bg='white', font=('Arial',9),command=lambda: press(3), height=2, width=8)
    btn3.grid(row=2, column=2)
    btn4 = Button(root, text='4', fg='black', bg='white', font=('Arial',9),command=lambda: press(4), height=2, width=8)
    btn4.grid(row=3, column=0)
    btn5 = Button(root, text='5', fg='black', bg='white',font=('Arial',9),command=lambda: press(5), height=2, width=8)
    btn5.grid(row=3, column=1)
    btn6 = Button(root, text='6', fg='black', bg='white',font=('Arial',9),command=lambda: press(6), height=2, width=8)
    btn6.grid(row=3, column=2)
    btn7 = Button(root, text='7', fg='black', bg='white',font=('Arial',9),command=lambda: press(7), height=2, width=8)
    btn7.grid(row=4, column=0)
    btn8 = Button(root, text='8', fg='black', bg='white',font=('Arial',9),command=lambda: press(8), height=2, width=8)
    btn8.grid(row=4, column=1)
    btn9 = Button(root, text='9', fg='black', bg='white', font=('Arial',9),command=lambda: press(9), height=2, width=8)
    btn9.grid(row=4, column=2)
    btn0 = Button(root, text='0', fg='black', bg='white',font=('Arial',9),command=lambda: press(0), height=2, width=8)
    btn0.grid(row=5, column=0)

    plus = Button(root, text='+', fg='black', bg='white',font=('Arial',9),command=lambda: press('+'), height=2, width=8)
    plus.grid(row=2, column=3)
    minus = Button(root, text='-', fg='black', bg='white',font=('Arial',9),command=lambda: press('-'), height=2, width=8)
    minus.grid(row=3, column=3)
    multply = Button(root, text='*', fg='black', bg='white', font=('Arial',9),command=lambda: press('*'), height=2, width=8)
    multply.grid(row=4, column=3)
    division = Button(root, text='/', fg='black', bg='white',font=('Arial',9),command=lambda: press('/'), height=2, width=8)
    division.grid(row=5, column=3)


    eq = Button(root, text='=', fg='black', bg='white',font=('Arial',9),command=equal, height=2, width=8)
    eq.grid(row=5, column=2)
    dot = Button(root, text='.', fg='black', bg='white', font=('Arial',9),command=clear, height=2, width=8)
    dot.grid(row=5, column=1)
    bracket = Button(root, text='(', fg='black', bg='white', font=('Arial',9),command=lambda: press('.'), height=2, width=8)
    bracket.grid(row=6, column=0)
    bracket = Button(root, text=')', fg='black', bg='white', font=('Arial',9),command=lambda: press('.'), height=2, width=8)
    bracket.grid(row=6, column=1)
    persent = Button(root, text='%', fg='black', bg='white', font=('Arial',9),command=lambda: press('.'), height=2, width=8)
    persent.grid(row=6, column=2)
    clr = Button(root, text='c', fg='black', bg='white', font=('Arial',9),command=lambda: press('.'), height=2, width=8)
    clr.grid(row=6, column=3)


    root.mainloop()

