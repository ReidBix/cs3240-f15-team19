__author__ = 'Reid'

import os
import sys
from tkinter import *


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

from media.documents import *

import os

from Project.SecureWitness.models import Document
from django.contrib.auth.models import User


from datetime import datetime
from django.utils import timezone

import django
django.setup()

import tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        u = "NotAUser"
        self.frames ={}
        for F in (StartPage, ):
            frame = F(self, container, self, u)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self,c):
        self.frames[c].tkraise()
        print(self.frames)

    """
    def __init__(self):
        tk.Tk.__init__(self)
        userIn = "NotAUser"
        self.title("Title")
        self.create_widgets(userIn)
        self.resizable(0,0)
    """

    def create_frame(self, c, u):
        t = tk.Toplevel(self)
        container = tk.Frame(self)
        frame = c(t, container, self, u)
        self.frames[c] = frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(c)

        """
        container = tk.Frame(self)
        frame = c(self, container, self, u)
        self.frames[c] = frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(c)
        """

    """
    def create_widgets(self, userIn):
        self.container = tk.Frame(self)
        self.container.grid(row=0,column=0,sticky=tk.W+tk.E)

        self.frames = {}
        for f in (StartPage, ):
            frame = f(self, self.container, self, userIn)
            frame.grid(row=2, column=2, stick= tk.NW+tk.SE)
            self.frames[f] = frame
        self.show_frame(StartPage)
    """


class BaseFrame(tk.Frame):
    def __init__(self, window, parent, controller, userIn):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        raise NotImplementedError

"""

class ExecuteFrame(BaseFrame):
    def create_widgets(self):
        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(StartPage),
                                    padx=5,
                                    pady=5,
                                    text="Home")
        self.new_button.grid(padx=5,pady=5,sticky=tk.W+tk.E)

class HomeFrame(BaseFrame):
    def create_widgets(self):
        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(ExecuteFrame),
                                    padx=5,
                                    pady=5,
                                    text="Execute")
        self.new_button.grid(padx=5,pady=5,sticky=tk.W+tk.E)
"""

class StartPage(BaseFrame):
    def create_widgets(self):
        N = 0
        label = tk.Label(self, text ="This is the start page")
        label.grid(row=0)

        """
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame(PageOne))
        N+=1
        button1.grid(row=N)
        """

        e1 = Entry(self)
        e2 = Entry(self)
        e3 = Entry(self)

        N+=1
        tk.Label(self, text="Username").grid(row=N)
        e1.grid(row=N, column=1)

        N+=1
        tk.Label(self, text="Email Address").grid(row=N)
        e2.grid(row=N, column=1)

        N+=1
        tk.Label(self, text="Password").grid(row=N)
        e3.grid(row=N, column=1)

        def login():
            uTry = e1.get()
            eTry = e2.get()
            pTry = e3.get()
            userList = User.objects.all()
            for u in userList:
                if (uTry == u.username):
                    print("Username is valid")
                    if(eTry == u.email):
                        print("Email is valid")
                        if(u.check_password(pTry)):
                            print("Password is valid")
                            userIn = uTry
                            self.controller.create_frame(PageOne, userIn)
                            break
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)


        N+=1
        tk.Button(self, text='Quit', command=self.quit).grid(row=N, column=0,
                                                             sticky=W, pady=4)
        tk.Button(self, text='Login', command=login).grid(row=N, column=1,
                                                        sticky=W, pady=4)


class PageOne(BaseFrame):
    def __init__(self, window, parent, controller, userIn):
        tk.Frame.__init__(self,parent)
        #label = tk.Label(window, text = "Page 1")
        #label.pack(side="top",fill="x",pady=10)
        #button = tk.Button(window,text = "Go to start page",
        #                   command=lambda: controller.show_frame(StartPage))
        #button.pack()

        print(userIn)
        var = StringVar()

        if(userIn == "NotAUser"):
            d = Document.objects.all()
        else:
            print("hi")
            d = Document.objects.filter(user=userIn)
        dList = []
        num = 1
        for name in d:
            dObject = (name, num)
            dList.append(dObject)
            num += 1
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        def getDocfile():
            dLink = var.get().replace('/', '\\')
            address = BASE_DIR + '\\media\\' + dLink
            print("Opening file at " + address)
            os.system("start " + address)

        label2 = tk.Label(window,
              text="""Choose a file:""",
              justify=LEFT,
              padx=20).grid()

        for name, val in dList:
            tk.Radiobutton(window,
                        justify = CENTER,
                        text=name,
                        indicatoron=0,
                        width=20,
                        padx=50,
                        variable=var,
                        command=getDocfile,
                        value=name.docfile).grid()


def startApp():
    root = Tk()

    w = Label(root, text="Hello!")
    w.pack()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logo = PhotoImage(file=BASE_DIR+"/static/meme_small.gif")
    w1 = Label(root, image=logo).pack(side="right")
    explanation = """at present, only
    GIF and PPM/PGM
    formats are supported,
    but an interface
    exists to allow
    additional image file
    formats to be added
    easily."""

    w2 = Label(root,justify=LEFT,
             padx = 0,
                pady = 0,
             text=explanation).pack(side="left")


    #compound = image drawn corresponding to text (BOTTOM, LEFT, RIGHT, TOP, CENTER)
    #justify = justify a text on the LEFT, RIGHT, or CENTER
    #padx = add additional horizontal padding around a text label
    #pady = add additional vertical padding around a text label


    Label(root,
                justify=CENTER,
                padx = 100,
                text = "Red Text in Times Font",
                fg = "red",
                font = "Times").pack()

    Label(root,
                text = "Green Text in Helvetica Font",
                fg = "light green",
                bg = "dark green",
                font = "Helvetica 16 bold italic").pack()

    Label(root,
                text = "Blue Text in Verdana bold",
                fg = "blue",
                bg = "yellow",
                font = "Verdana 10 bold").pack()



    quote = "This is a quote, and it's going to be misquoted for the rest of eternity. \n(Reid Bixler)"
    msg = Message(root, text = quote)
    msg.config(bg='lightgreen', font=('times',24,'italic'))
    msg.pack()


    class Appp:
        def __init__(self, root):
            frame = Frame(root)
            frame.pack()
            self.button = Button(frame,
                                 text="QUIT",fg="red",
                                 command=frame.quit)
            self.button.pack(side=LEFT)
            self.slogan = Button(frame,
                                 text="Hello",
                                 command=self.write_slogan)
            self.slogan.pack(side=LEFT)
        def write_slogan(self):
            print("Hello you idiot!")

    app = Appp(root)


    f1 = Frame(root)

    v = IntVar()
    v.set(0)

    languages = [
        ("Python",1),
        ("Perl",2),
        ("Java",3),
        ("C++",4),
        ("C",5)
    ]

    var = StringVar()

    d = Document.objects.all()
    dList = []
    num = 1
    for name in d:
        dObject = (name, num)
        dList.append(dObject)
        num+=1

    def getDocfile():
        dLink = var.get().replace('/','\\')
        address = BASE_DIR + '\\media\\' + dLink
        print("Opening file at " + address)
        os.system("start "+address)

    Label(root,
          text="""Choose a file:""",
          justify = LEFT,
          padx = 20).pack()

    for name,val in dList:
        Radiobutton(root,
                    text=name,
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=var,
                    command=getDocfile,
                    value=name.docfile).pack(anchor=W)


    frame = Frame(root)
    frame.pack()

    bottomFrame = Frame(root)
    bottomFrame.pack(side = BOTTOM)

    frame2 = Frame(root)
    frame2.pack(side = RIGHT)

    redButton = Button(frame, text="Red", fg="red")
    redButton.pack(side = LEFT)

    greenButton = Button(frame, text="Brown", fg="brown")
    greenButton.pack(side = LEFT)

    blueButton = Button(frame2, text="Blue", fg="blue")
    blueButton.pack(side = LEFT)

    blackButton = Button(bottomFrame, text="Black", fg="black")
    blackButton.pack(side =BOTTOM)

    #root.geometry("600x400+200+200")
    root.title("StandAloneApp Test")

    t = datetime.now()
    print(t)
    y = t.strftime("%Y")
    m = t.strftime("%m")
    d = t.strftime("%d")
    dfile = 'documents/' + str(y) + '/' + str(m) + '/' + str(d) + '/'

    d = Document(title="testdocument.txt", description="Test document for StandAloneApp",
                 detailed_description="", encrypted=True, private=True,
                 docfile=dfile,timestamp=t,
                 user="admin")
    print(d.description)
    print(d.title)
    d.save()

    d2 = Document.objects.get(id=4)
    print(d2.title)

    print(Document.objects.all())

    d3 = Document.objects.filter(user__startswith='admin')
    print(d3)

    d4 = Document.objects.filter(timestamp__day=timezone.now().day)
    print(d4)

    d5 = Document.objects.get(pk=9)
    print(d5.docfile)

    d5.title = "Change of title"
    d5.save()

    d4.delete()


    root.mainloop()


    return 0


if __name__ == '__main__':
    #startApp()
    app = App()
    app.mainloop()