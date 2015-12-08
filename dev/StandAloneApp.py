__author__ = 'Reid'

import os
import sys
from tkinter import *
from media.documents import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

import os

from Project.SecureWitness.models import Report, UserProfile, Upload
from django.contrib.auth.models import User


from datetime import datetime
from django.utils import timezone

import django

import tkinter as tk

from dev import encrypt

from Crypto.Cipher import AES
from Crypto import Random

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import *

import unittest

django.setup()

block = AES.block_size #16

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

    def create_frame(self, c, u, k):
        t = tk.Toplevel(self)
        container = tk.Frame(self)
        frame = c(t, container, self, u, k)
        self.frames[c] = frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(c)

class BaseFrame(tk.Frame):
    def __init__(self, window, parent, controller, userIn):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        raise NotImplementedError


class StartPage(BaseFrame):
    def create_widgets(self):
        N = 0
        label = tk.Label(self, text ="This is the start page")
        label.grid(row=0)


        e1 = Entry(self)
        e3 = Entry(self)
        e2 = Entry(self)

        N+=1
        tk.Label(self, text="Username").grid(row=N)
        e1.grid(row=N, column=1)

        N+=1
        tk.Label(self, text="Password").grid(row=N)
        e3.grid(row=N, column=1)

        N += 1
        tk.Label(self, text="PrivateKey").grid(row=N)
        e2.grid(row=N, column=1)

        def login():
            uTry = e1.get()
            pTry = e3.get()
            kTry = e2.get()
            userList = User.objects.all()
            for u in userList:
                if (uTry == u.username):
                    #print("Username is valid")
                    if(u.check_password(pTry)):
                        #print("Password is valid")
                        #try:
                            #try to make private key object
                        private = (kTry).encode('utf-8')
                        private = private[:31] + b'\n' + private[31:]
                        for i in range(1, 13):
                            private = private[:(31 + (65 * i))] + b'\n' + private[(31 + (65 * i)):]
                        private = private[:860] + b'\n' + private[860:]
                        priKey = RSA.importKey(private)
                        print(priKey)
                        userIn = uTry
                        self.controller.create_frame(PageOne, userIn, kTry)
                        break
                        #except:
                            #print("That is not a correct private key!")
                            #break
            e1.delete(0, END)
            e3.delete(0, END)
            e2.delete(0, END)


        N+=1
        tk.Button(self, text='Quit', command=self.quit).grid(row=N, column=0,
                                                             sticky=W, pady=4)
        tk.Button(self, text='Login', command=login).grid(row=N, column=1,
                                                        sticky=W, pady=4)


class PageOne(BaseFrame):
    def __init__(self, window, parent, controller, userIn, priKey):
        tk.Frame.__init__(self,parent)
        global rKey
        rKey = priKey
        #print(userIn)
        #get user from private key
        #print(priKey)

        if(userIn == None):
            report_list = []
            group_report_list = []
            shared_report_list = []
            public_report_list = []
            admin_report_list = []
        else:
            group_report_list = []
            report_list = Report.objects.filter(user__username=userIn)
            u = User.objects.get(username=userIn)
            g_list = []
            #print(u)
            for g in u.groups.all():
                g_list.append(g)
            g_report_list = Report.objects.filter(group__in=g_list).exclude(user=u).exclude(
                sharedusers=u).exclude(private=False).order_by('timestamp')

            for i in g_report_list:
                if i not in group_report_list:
                    group_report_list.append(i)

            # INTENTIONALLY DOESN'T EXCLUDE GROUPS, JUST LEAVE IT
            shared_report_list = Report.objects.filter(sharedusers=u).exclude(user=u).exclude(
                private=False).order_by('timestamp')

            public_report_list = Report.objects.filter(private=False).exclude(user=u)
            admin_report_list = Report.objects.exclude(user=u).exclude(group__in=g_list).exclude(
                sharedusers=u).exclude(private=False).order_by('timestamp')

            #List all available reports
            #d = Report.objects.all()
            #print(d)
        dList = []
        num = 1
        for name in report_list:
            dObject = (name, num)
            dList.append(dObject)
            num += 1
        for name in group_report_list:
            dObject = (name, num)
            dList.append(dObject)
            num += 1
        for name in shared_report_list:
            dObject = (name, num)
            dList.append(dObject)
            num += 1
        for name in public_report_list:
            dObject = (name, num)
            dList.append(dObject)
            num += 1
        for name in admin_report_list:
            dObject = (name, num)
            dList.append(dObject)
            num += 1

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        v = IntVar()
        v.set(0)

        var = StringVar()

        selections = [
            ("Decrypt", 1),
            ("Download", 2)
        ]

        decryptTrue = False
        downloadTrue = False

        def getDocfile():
            #get timestamp
            #turn into report
            report = Report.objects.get(timestamp=var.get())
            #find file(s) from report
            upload = Upload.objects.filter(report=report)
            fileList = []
            for u in upload:
                fileList.append(u.file)
            #print(fileList)
            #get address from file
            addressList = []
            address = BASE_DIR + '\\media\\'
            for f in fileList:
                addressList.append(address + str(f).replace('/', '\\'))
            #print("addressList is: ")
            #print(addressList)
            if var1.get() == 1:
                #print("DECRYPT!!")
                timestamp = var.get()
                #print(timestamp)
                #report = Report.objects.get(timestamp=var.get())
                #print(report)
                #print(userIn)
                #i = UserProfile.objects.all().filter(user__username=userIn)
                u = UserProfile.objects.get(user__username=userIn)
                aesKeyLocked = report.key
                print("aesKeyLocked is " + str(aesKeyLocked))
                #print(rKey)
                #DECRYPTION STUFF!!]
                for a in addressList:
                    print("HeyyyyOooooo")
                    print(a)
                    print(rKey)
                    print("aesKeyLocked is " + str(aesKeyLocked))
                    decryptFile(a, rKey, aesKeyLocked)

            if var2.get() == 1:
                print("Opening file at " + address)
                #os.system("start " + address)

        def decryptLink():
            print("decrypt: %d, \ndownload: %d"%(var1.get(), var2.get()))

        label2 = tk.Label(window,
              text="""Choose a file:""",
              justify=LEFT,
              padx=20).grid()

        var1 = IntVar()
        Checkbutton(window,
                    justify = CENTER,
                    text="decrypt",
                    width = 20,
                    padx = 50,
                    variable = var1).grid()
        var2 = IntVar()
        Checkbutton(window,
                    justify = CENTER,
                    text="download",
                    width = 20,
                    padx = 50,
                    variable=var2).grid()

        for report, val in dList:
            #print(name.docfile)
            tk.Radiobutton(window,
                        justify = CENTER,
                        text=report,
                        indicatoron=0,
                        width=20,
                        padx=50,
                        variable=var,
                        command=getDocfile,
                        value=report.timestamp).grid()

        Button(window, text="Quit", command=window.quit).grid()
        Button(window, text="Show", command=decryptLink).grid()

class PageTwo(BaseFrame):
    def __init__(self, window, parent, controller, userIn):
        tk.Frame.__init__(self,parent)





def populateKeys():
    u = UserProfile.objects.all()
    for user in u:
        rsaKey = RSA.generate(1024, Random.new().read)
        rExport = rsaKey.exportKey('PEM')
        uExport = rsaKey.publickey().exportKey('PEM')
        user.publickey = uExport
        user.tempprivate = rExport
        user.save()

def encryptFile(fileIn, publickey):
    aesKey = Random.new().read(16)
    print("aesKeyUnlocked is " + str(aesKey))
    encrypt.Encrypt(fileIn, aesKey)

    pKey = (publickey).encode('utf-8')
    public_key = pKey[:26] + b'\n' + pKey[26:]
    for i in range(1, 4):
        public_key = public_key[:(26 + (65 * i))] + b'\n' + public_key[(26 + (65 * i)):]
    public_key = public_key[:246] + b'\n' + public_key[246:]
    pubKey = RSA.importKey(public_key)

    cipher = PKCS1_OAEP.new(pubKey)
    aesKeyLocked = cipher.encrypt(aesKey)
    return aesKeyLocked

def decryptFile(fileIn, privkey, aesKeyLocked):

    private = (privkey).encode('utf-8')
    private = private[:31] + b'\n' + private[31:]
    for i in range(1, 13):
        private = private[:(31 + (65 * i))] + b'\n' + private[(31 + (65 * i)):]
    private = private[:860] + b'\n' + private[860:]
    priKey = RSA.importKey(private)

    print("A")
    uncipher = PKCS1_OAEP.new(priKey)
    #aesKeyLEncode = aesKeyLocked.encode("utf-8")
    #try:
    print("B")
    print(type(aesKeyLocked))
    aesKeyUnlocked = uncipher.decrypt(aesKeyLocked)
    print("C")
    print("aesKeyUnlocked is " + str(aesKeyUnlocked))
    print("D")
    encrypt.Decrypt(in_file=fileIn, key=aesKeyUnlocked)
    #except ValueError:
        #print("The wrong key has been used to decrypt!")


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
            #print("Hello you idiot!")
            pass

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

    d = Report.objects.all()
    dList = []
    num = 1
    for name in d:
        dObject = (name, num)
        dList.append(dObject)
        num+=1

    def getDocfile():
        dLink = var.get().replace('/','\\')
        address = BASE_DIR + '\\media\\' + dLink
        #print("Opening file at " + address)
        os.system("start "+address)

    Label(root,
          text="""Choose a file:""",
          justify = LEFT,
          padx = 20).pack()



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


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dLink = var.get().replace('/', '\\')
    address = BASE_DIR + "\media\\files\\2015\\12\\06\\Llamas DB Poster 1-v1.pdf"

    user = UserProfile.objects.get(user__username='User1')
    pubKey = user.publickey
    aesKeyLocked = encryptFile(address,pubKey)
    print("1")
    print(type(aesKeyLocked))
    print("aesKeyLocked is " + str(aesKeyLocked))
    print("2")
    #need .enc after
    priKey = user.tempprivate # to be given in App
    #aesKeyLocked = aesKeyLocked.encode('utf-8')
    print("3")
    print(type(aesKeyLocked))
    print(aesKeyLocked)







    decryptFile(address+".enc",priKey,aesKeyLocked)

    #Encrypt with whatever public key you want the owner of to see

    #Decrypt with private key of public key


    r = Report.objects.filter(user__username="admin")
    #r = Report.objects.all()
    for r2 in r:
        #print(r2.key)
        u = Upload.objects.all()
        for u2 in u:
            #Get
            pass
    #print(r)
    """
    up = UserProfile.objects.get(user__username=uTry)
    print(up.publickey)
    """

    root.mainloop()


    return 0

def encryptEasy(fileName, userName):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    #Change dates if necessary
    address = BASE_DIR + "\media\\files\\2015\\12\\07\\"
    address = address + fileName
    user = UserProfile.objects.get(user__username=userName)
    pubKey = user.publickey
    aesKeyLocked = encryptFile(address, pubKey)
    print("aesKeyLocked is " + str(aesKeyLocked))
    return(aesKeyLocked)

if __name__ == '__main__':
    #populateKeys()
    startApp()
    #EncryptEasy File
    fileName = "ACM_Code_of_Ethics_Essay.docx"
    userName = "admin"
    aesKeyLocked = encryptEasy(fileName, userName) #string
    print("aesKeyLocked is " + str(aesKeyLocked) + "!!!")
    t = datetime.now()
    path = "C:\\Users\\Reid\\git\\cs3240-f15-team19\\dev\\media\\"
    filepath = "files\\2015\\12\\07\\"
    user = User.objects.get(username=userName)
    #Store into report
    #Store key in report
    r2 = Report.objects.filter(title="EncryptionTest")
    r2.delete()

    #print(Upload._meta.get_all_field_names())


    r = Report(title="EncryptionTest", description="Test document for StandAloneApp",
                detailed_description="This is long", private=True,
                   timestamp=t, user=user, key=aesKeyLocked)
    r.save()

    #print(r)
    u = Upload(name=fileName+'.enc',file=filepath+fileName+'.enc',report=r,encrypted=True,)
    u.save()
    #ez
    app = App()
    app.mainloop()
