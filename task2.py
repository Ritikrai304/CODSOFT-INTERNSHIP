from tkinter import *
root = Tk()
root.geometry("644x600")
root.title("Calculator by ritik")
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

            scvalue.set(value)
            screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10,padx=10)

frame = Frame(root, bg="grey")
button = Button(frame, text="9", font="bold", padx=26, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="8", font="bold", padx=26, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="7", font="bold", padx=26, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="C", font="bold", padx=26, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
frame.pack()

frame = Frame(root, bg="grey")
button = Button(frame, text="6", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="5", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="4", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="/", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
frame.pack()

frame = Frame(root, bg="grey")
button = Button(frame, text="3", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="2", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="1", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="*", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
frame.pack()

frame = Frame(root, bg="grey")
button = Button(frame, text="0", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="-", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="+", font="bold", padx=27, pady=18)
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
button = Button(frame, text="=", font="bold", padx=27, pady=18, bg="orange")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)
frame.pack()
root.mainloop()
