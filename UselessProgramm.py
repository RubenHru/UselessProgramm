import tkinter as tk
import random as rng
import sys

window = tk.Tk()
firstWindow = tk.Tk()
firstWindow.withdraw()
window.attributes("-fullscreen", True)

backGround = tk.PhotoImage(file = "Microsoft-Teams-stuck-on-loading.png")

label = tk.Label(window, image=backGround)
label.place(x=0, y=0)

screenHeight = window.winfo_screenheight()
screenWidth = window.winfo_screenmmwidth()

def Start(event):
    firstWindow.geometry("150x100")
    firstWindow.deiconify()
    greeting = tk.Label(firstWindow,text="Hallo Reinhard!")
    greeting.pack()
    buttonNotOk.pack()

def Close(event):
    window.destroy()


window.geometry("720x480")
window.bind("<Button-1>", Start)
window.bind("<Escape>", Close)



def SelectEvent():
    randomNumber = rng.randint(0, 2)
    if randomNumber == 0:
        MoveWindow()
    if randomNumber == 1:
        MaybeOk()
    if randomNumber == 2:
        MoveOk()

buttonNotOk = tk.Button(firstWindow, text="Not OK", command=SelectEvent)

def MoveWindow():
    windowHeight = 100
    windowWidth = 150
    randomNumber = rng.randint(2,50)
    x = screenWidth/randomNumber
    y = screenHeight/randomNumber
    firstWindow.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight, x, y))

def MaybeOk():
    randomNumber = rng.randint(1,25)
    for x in range(randomNumber):
        notOkWindow = tk.Tk()
        notOkWindow.geometry("150x100")
        buttonNotOk = tk.Button(notOkWindow,text="Not OK", command=notOkWindow.destroy)
        buttonNotOk.pack()

def MoveOk():
    randomNumber = rng.randint(1,10)
    x = 150/randomNumber
    y = 100/randomNumber
    buttonNotOk.place(x=x, y=y)


window.mainloop()