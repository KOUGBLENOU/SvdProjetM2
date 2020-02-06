import tkinter
class HelloQuitButton:
    def __init__(self, msg='Quit'):
        self.msg = msg
        b = tkinter.Button(None)
        b.config(text=self.msg, command=self.handle)
        b.pack(side=tkinter.RIGHT)
    def handle(self):
        print (self.msg)
        exit()

class HelloQuitButto:
    def __init__(self, msg='Qui'):
        self.msg = msg
        b = tkinter.Button(None)
        b.config(text=self.msg, command=self.handle)
        b.pack(side=tkinter.LEFT)
        zone_texte = tkinter.Label (text = "premier texte")
        zone_texte.pack(side=tkinter.TOP)
    def handle(self):
        print (self.msg)
        #exit()
win = tkinter.Frame()
win.pack()
hqb = HelloQuitButton()
hqba = HelloQuitButto()
tkinter.mainloop()