######################################################
#       PROJET M2 APPRENTISSAGE NON SUPERVISEE       #
#       WINDOWS.py FILE                              #
#       AUTHORS :                                    #
#           *** Masood S.                            #
#           *** Ben A.                               #
#           *** Frank  K2                            #
#       LAST UPDATE : 06/02/2020                     #
#       OBJECT : User interface's development file   #
######################################################

#============================================== Frank Add
import matplotlib.pyplot as pltlib # MatPlotLib module import
import tkinter
import main

class MyWindows:
    ### Datas init for the principal object 
    zone_texte = None
    X          = None
    S          = None
    TraceDeS2  = None
    Absciss    = None
    Ordonnee   = None
    InitDone   = 0
    
    ### End data init
    
    def __init__(self, msg='HOME'):
        self.msg = msg
        
        #Textbox
        self.zone_texte = tkinter.Label (
            text = "Hello! Pliz press the init button and wait until the init process ends", width ="75",
                        pady="20", padx="15", bg ="light gray")
        
        
        self.zone_texte.pack(side= tkinter.TOP)
        #End textbox
        
        
        # Button for initialisation
        Btn_init = tkinter.Button(overrelief = "sunken",
            activeforeground = "red", width ="30", pady="20", padx="15")
        Btn_init.config(text="Data Init and compute" , command=self.InitAndProcess, fg = "blue")   
        Btn_init.pack()       
        #End  Button for initialisation
        
        
        # Button for plot
        Btn_plot = tkinter.Button(overrelief = "sunken",
            activeforeground = "red", width ="30", pady="20", padx="15")
        Btn_plot.config(text="Results plot", command=self.Plot, fg = "blue") 
        Btn_plot.pack()
        #End Button for plot
        
        # Button for quit
        Btn_quit = tkinter.Button(overrelief = "sunken",
            activeforeground = "red", width ="30", pady="20", padx="15")
        Btn_quit.config(text="Quit the App" , command=self.Bye, fg = "blue")
        Btn_quit.pack()
        
        #End Button for quit

    def Bye (self): # Quit function
        print("App closed")
        exit()
        
    def InitAndProcess(self): # init function
        if (self.InitDone == 0):
            print("Initialzing")
            self.zone_texte.config (
                text = "Thanks for waiting ! Now you can press plot buton for result ploting")
            
            self.X, self.S, self.TraceDeS2, self.Absciss, self.Ordonnee = main.initialize() # Read, compute datas, ...
            self.InitDone = 1
        elif (self.InitDone ==1):
            print("init process allready done")
            self.zone_texte.config (
                text = "Init process allready done ! Now you can press plot btn for result ploting")
    
    def Plot(self): # plot funvtion
        if (self.InitDone == 1):
            print("Ploting")
            pltlib.plot(self.Absciss, self.Ordonnee, label ="Perte(p)")
            pltlib.title("Variation des pertes (%) en fonction du nombre de composante considéré")
            pltlib.ylabel("Perte")
            pltlib.xlabel("Nombre de composante considéré")
            pltlib.legend()
            pltlib.show()
        else :
            print("Pliz ! Make sure the init process is well done before ploting")
            self.zone_texte.config (
            text = "Pliz ! Make sure the init process is well done before ploting ! Press init button")
            
# User interface lunch
mainWindows = tkinter.Tk()
label = tkinter.Label(mainWindows, text="Apprentissage non supervisée - Analyse de composante principale",
                      relief ="ridge", fg = "red")
label.pack()
MW = MyWindows()
print("App openned")
tkinter.mainloop()


#============================================== End Frank Add