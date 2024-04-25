from tkinter import *
from PIL import Image,ImageTk, ImageSequence # type: ignore
import time
import pygame
from pygame import mixer # type: ignore
mixer.init()

root=Tk()
root.geometry("1800x900")

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img= Image.open("ironmanSnap.gif")
    lbl= Label(root)
    lbl.place(x=0, y=0)
    i=0
    mixer.music.load("Voicy_Avengers Assemble.mp3")
    mixer.music.play()


    for img in ImageSequence.Iterator(img):
        img =img.resize((1800,900))
        img= ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.09)
    root.destroy()

play_gif()
root.mainloop()
