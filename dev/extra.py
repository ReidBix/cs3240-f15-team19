__author__ = 'Reid'

    """
    def __init__(self):
        tk.Tk.__init__(self)
        userIn = "NotAUser"
        self.title("Title")
        self.create_widgets(userIn)
        self.resizable(0,0)
    """

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

"""
button1 = tk.Button(self, text="Go to Page One",
                    command=lambda: controller.show_frame(PageOne))
N+=1
button1.grid(row=N)
"""

# label = tk.Label(window, text = "Page 1")
# label.pack(side="top",fill="x",pady=10)
# button = tk.Button(window,text = "Go to start page",
#                   command=lambda: controller.show_frame(StartPage))
# button.pack()


    #compound = image drawn corresponding to text (BOTTOM, LEFT, RIGHT, TOP, CENTER)
    #justify = justify a text on the LEFT, RIGHT, or CENTER
    #padx = add additional horizontal padding around a text label
    #pady = add additional vertical padding around a text label

"""
    t = datetime.now()
    print(t)
    y = t.strftime("%Y")
    m = t.strftime("%m")
    d = t.strftime("%d")
    dfile = 'documents/' + str(y) + '/' + str(m) + '/' + str(d) + '/'

    d = Report(title="testdocument.txt", description="Test document for StandAloneApp",
                 detailed_description="", encrypted=True, private=True,
                 docfile=dfile,timestamp=t,
                 user="admin")
    print(d.description)
    print(d.title)
    d.save()

    print(Repo.objects.all())

    d3 = Report.objects.filter(user__startswith='admin')
    print(d3)

    d4 = Report.objects.filter(timestamp__day=timezone.now().day)
    print(d4)

    d4.delete()
    """
    """
    aesKey = Random.new().read(AES.block_size)
    print("Creating new AES Key:")
    print("\t" + str(aesKey))

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dLink = var.get().replace('/', '\\')
    address = BASE_DIR + '\\media\\' + dLink
    docString = "documents\\2015\\11"
    doc1 = "\\04\\Guest_speaker_feedback.docx"
    address = address + docString + doc1
    print("Encrypting file at " + address)

    encrypt.Encrypt(in_file=address, key=aesKey)
    #encrypt.Decrypt(in_file=address+".enc", key=aesKey)

    #print("Complete!")
   """

"""
pKey = user.publickey
pKey = (pKey).encode('utf-8')
public_key = pKey[:26] + b'\n' + pKey[26:]
for i in range(1, 4):
    public_key = public_key[:(26 + (65 * i))] + b'\n' + public_key[(26 + (65 * i)):]
public_key = public_key[:246] + b'\n' + public_key[246:]
pubKey = RSA.importKey(public_key)


#GET USERS PRIVATE KEY
private = (private).encode('utf-8')
private = private[:31] + b'\n' + private[31:]
for i in range(1, 13):
    private = private[:(31 + (65 * i))] + b'\n' + private[(31 + (65 * i)):]
private = private[:860] + b'\n' + private[860:]
priKey = RSA.importKey(private)
"""