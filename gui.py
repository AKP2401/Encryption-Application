import tkinter as tk
import tkinter.font as tkFont
from Encrypt import Encryption
import pyperclip as pc

class App:
    def __init__(self, root):
        self.EN = Encryption()
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.inPut=tk.Entry(root)
        self.inPut["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.inPut["font"] = ft
        self.inPut["fg"] = "#333333"
        self.inPut["justify"] = "center"
        self.inPut["text"] = ""
        self.inPut.place(x=60,y=40,width=481,height=130)

        self.encodeBt=tk.Button(root)
        self.encodeBt["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.encodeBt["font"] = ft
        self.encodeBt["fg"] = "#000000"
        self.encodeBt["justify"] = "center"
        self.encodeBt["text"] = "Encode"
        self.encodeBt["relief"] = "raised"
        self.encodeBt.place(x=115,y=220,width=88,height=41)
        self.encodeBt["command"] = self.encode

        self.decodeBt=tk.Button(root)
        self.decodeBt["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.decodeBt["font"] = ft
        self.decodeBt["fg"] = "#000000"
        self.decodeBt["justify"] = "center"
        self.decodeBt["text"] = "Decode"
        self.decodeBt["relief"] = "raised"
        self.decodeBt.place(x=255,y=220,width=88,height=41)
        self.decodeBt["command"] = self.decode

        self.pastClip=tk.Button(root)
        self.pastClip["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.pastClip["font"] = ft
        self.pastClip["fg"] = "#000000"
        self.pastClip["justify"] = "center"
        self.pastClip["text"] = "Paste from Clipboard"
        self.pastClip["relief"] = "raised"
        self.pastClip.place(x=395,y=220,width=145,height=41)
        self.pastClip["command"] = self.paste

        self.outPut=tk.Label(root, wraplength=450)
        ft = tkFont.Font(family='Times',size=10)
        self.outPut["font"] = ft
        self.outPut["fg"] = "#333333"
        self.outPut["justify"] = "center"
        self.outPut["text"] = ""
        self.outPut.place(x=60,y=290,width=484,height=115)

        self.copyClip=tk.Button(root)
        self.copyClip["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        self.copyClip["font"] = ft
        self.copyClip["fg"] = "#000000"
        self.copyClip["justify"] = "center"
        self.copyClip["text"] = "Copy \nto \nClipboard"
        self.copyClip.place(x=250,y=430,width=110,height=50)
        self.copyClip["command"] = self.copy

    def encode(self):
        inp = self.inPut.get()
        self.outPut.config(text=self.EN.Encrypt(inp))
        
    def decode(self):
        inp = self.inPut.get()
        self.outPut.config(text=self.EN.Decrypt(inp))

    def copy(self):
        pc.copy(self.outPut.cget("text"))

    def paste(self):
        inp = pc.paste()
        self.inPut.delete(0, "end")
        self.inPut.insert(0, inp)
    

def run():
    root = tk.Tk()
    app = App(root)
    root.mainloop()