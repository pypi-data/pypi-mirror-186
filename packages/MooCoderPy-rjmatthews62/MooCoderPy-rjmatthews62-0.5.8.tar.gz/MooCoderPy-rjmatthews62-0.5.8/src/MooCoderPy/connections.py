from configparser import ConfigParser
import os,sys
from tkinter import *
from tkinter import font,simpledialog
import SettingsDialog

class Connections(Toplevel):
    inifile:ConfigParser
    list:Listbox
    connectionList=[]
    currentConnection:StringVar
    currentLogin:StringVar
    currentIndex:int=-1

    def __init__(self,*args, **kwargs):
        y:int=0
        super().__init__(*args, **kwargs)
        self.option_add('*Font', ("Arial",10,font.BOLD))
        self.grab_set()
        f0=Frame(self)
        f0.pack(side=LEFT,fill=Y)
        lb0=Label(f0,text="Connections")
        lb0.pack(side=TOP)
        self.list=Listbox(f0,exportselection=False)
        self.list.pack(fill=Y)
        self.list.bind("<<ListboxSelect>>",self.onSelected)
        f2=Frame(f0)
        Button(f2,text="Add",command=self.addConnection).grid(column=0,row=0)
        Button(f2,text="Delete").grid(column=1,row=0)
        Button(f2,text="Rename").grid(column=2,row=0)
        f2.pack(side=BOTTOM,pady=4)
    
        f1=Frame(self)
        f1.pack(side=LEFT,fill=BOTH, expand=True)

        def addrow(caption:str, edit:Widget):
            nonlocal y
            lbl=Label(f1,text=caption)
            lbl.grid(row=y,column=0,sticky=W,padx=(8,0))
            edit.grid(row=y,column=1,sticky=W, padx=8)
            y+=1
        
        self.currentConnection=StringVar(self,value="srtmoo:8492")
        self.currentLogin=StringVar(self,value="connect robbie SRTDumpling")
        self.currentName=StringVar(self,value="Default")
        addrow("Name",Label(f1,textvariable=self.currentName))
        addrow("Address",Entry(f1,width=60,textvariable=self.currentConnection))
        addrow("Login",Entry(f1,width=60,textvariable=self.currentLogin))
        self.title("Settings")
        self.loadSettings()
    
    def addConnection(self):
        result=simpledialog.askstring("Connections","New connection name")
        if not(result):
            return
        self.addList(result,"server:port","login goes here")
        self.list.select_set(len(self.connectionList)-1)
        self.onSelected(None)

    def loadSettings(self):
        self.inifile=SettingsDialog.getConfig()
        settings=self.inifile["settings"]
        address=settings.get("Server","example.server.net:8922")
        login=settings.get("Connect","login command here")

        self.addList("Default",address,login)
        self.addList("Testing 1","testing.com:8339","connect as me")
        self.addList("SRTMoo","strmoo.net:8492","connect robbie SRTDumpling")
        self.addList("Local server","localhost:8492","connect wizard")
        self.list.select_set(0)
    
    def addList(self,name,address,login):
        self.connectionList.append((name,address,login))
        self.refreshList()
    
    def refreshList(self):
        self.list.delete(0,END)
        for x in self.connectionList:
            self.list.insert(END,x[0])

    def onSelected(self,e:Event):
        i=self.list.curselection()[0]
        if self.currentIndex>=0:
            row=self.connectionList[self.currentIndex]
            self.connectionList[self.currentIndex]=(row[0],self.currentConnection.get(),self.currentLogin.get())
        con=self.connectionList[i]
        self.currentName.set(con[0])
        self.currentConnection.set(con[1])
        self.currentLogin.set(con[2])
        self.currentIndex=i

if __name__=="__main__":
    root=Tk()
    root.title("Root")
    root.after(50,lambda: Connections(root))
    root.mainloop()