"the ide file for gameScript"
#include<asmp>
#cas asmp.s.define
#.Bs bds
from tempfile import tempdir
import tkinter,time,os,sys
from tkinter import font
import tkinter.filedialog
import tkinter.messagebox
import tkinter.scrolledtext
import mingw
import io
from colorama import init,Back,Style
init(autoreset=True)
print(Back.RED+"start!")
print(Style.BRIGHT+Back.LIGHTBLACK_EX+"init...")
time.sleep(2)
root=tkinter.Tk()
m=tkinter.Menu(root)
f:io.TextIOWrapper
code=tkinter.scrolledtext.ScrolledText(root,undo=True)
code.pack()
class menu:
    class file:
        def new():
            temp=tkinter.filedialog.asksaveasfilename(filetypes=[("GameScript","*.gs"),("config file","*.config")])
            open(temp,mode="w").close()
            root.title("GameScript IDE:[file]",temp)
        def opena():
            global f
            temp=tkinter.filedialog.askopenfilename(filetypes=[("GameScript file","*.gs"),("Config file","*.ini")])
            root.title("GameScript IDE:[file]",temp)
            try:
                f=open(temp,mode="r+")
            except (IOError,BufferError,UnicodeEncodeError):
                f=None
                try:
                    f=open(temp,mode="r+",encoding="utf-8")
                except:
                    tkinter.messagebox.showerror("msg","can't open this file")
        def exitf():pass
def main():
    global root,m
    root.title("GameScripts IDE")
    root.geometry("900x700")
    root.minsize(900,700)
    root.maxsize(900,700)
    
if __name__=="__main__":
    main()