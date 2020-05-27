from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import Back as bk

def callBackOne():
    imageOne = str(fd.askopenfile())
    imList1= imageOne.split("'")
    global imOnePosition
    imOnePosition = imList1[1]
    print(imOnePosition)
    global imageOneSelected
    imageOneSelected = True

def callBackTwo():
    imageTwo= str(fd.askopenfile())
    imList2 = imageTwo.split("'")
    global imTwoPosition
    imTwoPosition = imList2[1]
    print(imTwoPosition)

def displayLabel():
    if imageOneSelected == True:
        text1 = Label(root, text=str(bk.comparator(imOnePosition, imTwoPosition, 4)))
        text1.pack(side=RIGHT)
    else:
        print("Image one not selected")

root = Tk()
root.geometry("600x600")
root.title("CompEnv")
'''root.attributes('-fullscreen', True)
root.bind("<F11>",lambda event:root.attributes("-fullscreen",not root.attributes("-fullscreen")))
root.bind("<Escape>",lambda event: root.attributes("-fullscreen",False))'''

errmsg = 'Error!'
button1 = Button(root,text='Click to Open Image One', command=callBackOne).pack(side=LEFT)
button2 = Button(root,text='Click to Open Image Two', command=lambda:[callBackTwo(),displayLabel()]).pack(side=LEFT)
tk.mainloop()