from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("1000x800")
root.minsize(600,700)
root.maxsize(1200,900)
root.title("MyCal")
root.configure(background='red')


root.wm_iconbitmap("th.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="georgia 40 bold")
screen.pack(fill=X, ipadx=8, pady=7, padx=10)

f = Frame(root, bg="blue")
b = Button(f, text="(", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=")", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root, bg="blue")
b = Button(f, text="9", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="blue")
b = Button(f, text="6", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)


f.pack()


f = Frame(root, bg="blue")
b = Button(f, text="3", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)


f.pack()


f = Frame(root, bg="blue")
b = Button(f, text="C", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=15, pady=8, font="georgia 35 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)


f.pack()


