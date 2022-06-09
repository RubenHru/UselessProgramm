import tkinter as tk
import random as rng

window = tk.Tk()

windowHeight = 150
windowWidth = 100
screenHeight = window.winfo_screenheight()
screenWidth = window.winfo_screenmmwidth()

window.geometry("150x100")

greeting = tk.Label(text="Hallo Reinhard!")
greeting.pack()

def selectEvent():
    randomNumber = rng.randint(0,1)

def moveWindow():
    randomNumber = rng.randint(1,10)
    x = screenWidth/randomNumber
    y = screenHeight/randomNumber
    window.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight, x, y))

def maybeOk():
    randomNumber = rng.randint(1,50)
    for x in range(randomNumber):
        notOkWindow = tk.Tk()
        buttonNotOk = tk.Button(notOkWindow,text="Ok")
        buttonNotOk.pack()

buttonNotOk = tk.Button(text="Not OK", command=moveWindow)
buttonNotOk.pack()


window.mainloop()