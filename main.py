######################################################
#       PROJET M2 APPRENTISSAGE NON SUPERVISEE       #
#       MAIN.py FILE                                 #
#       AUTHORS :                                    #
#           *** Masood S.                            #
#           *** Ben A.                               #
#           *** Frank  K2                            #
#       LAST UPDATE : 06/02/2020                     #
#       UP TO NOW :                                  #
#               *** file.dat reading and conversion  #
#                to   array  2D                      #
#               *** compute svd of X centered        # 
#               *** compute trace (S^2)              #
#               *** plot function                    #
#       OBJECT : Programmer principal file           #
######################################################

#============================================== Frank Add

import numpy as npy  # Numpy module import
import matplotlib.pyplot as pltlib # MatPlotLib module import
import centering
import trace
import PlotDataCompute

# Datas init
MaxLine = 10000
MaxCol = 142
OurList = []
ColSum = [0 for i in range(MaxCol)]
# ...
# End Datas init


def initialize(): # Init function
    try:
        Datafile = open("Output.dat", "r")  # Data file openning
    except:
        print("Error openning Output.dat file")
        exit()
        

    for line in Datafile.readlines():  # Reading file line/line

        OurList.append([])  # Another line in the list

        positionInColAverage = 0
        for i in line.split():  # for every elt in the current line

            OurList[-1].append(float(i))   # add to the list
            ColSum[positionInColAverage] += float(i)   # Compute the moyenne of cols every iteration
            positionInColAverage += 1

    Datafile.close()  # Data file can be closed now

    X         = npy.asarray(OurList)  # Conversion from list to Array 2D

    X         = centering.Center(X, MaxLine, MaxCol, ColSum, True)  # Centering the matrice

    S         = npy.linalg.svd(X, compute_uv= False) # S computation


    TraceDeS2 = trace.traceComputer(S, len(S)) # trace(S^2) computation

    Absciss, Ordonnee      = PlotDataCompute.PlotDataComputer(S, len(S)) # Plot Datas compute
    
    return X, S, TraceDeS2, Absciss, Ordonnee


def plotFunction():
    
    X, S, TraceDeS2, Absciss, Ordonnee = initialize() # Read, compute datas, ...
    pltlib.plot(Absciss, Ordonnee, label ="Perte(p)")
    pltlib.title("Variation des pertes (%) en fonction du nombre de composante considéré")
    pltlib.ylabel("Perte")
    pltlib.xlabel("Nombre de composante considéré")
    pltlib.legend()
    pltlib.show()
  
############################ TRES IMPORTANT
    #ce fichier est le fichier principale pour le développeur.
    #Pour travailler ici, exécuter ou faire un test,
    #il faudra décommenter la ligne d'appel à la fonction plotFunction()
    # qui est la suivante :
#plotFunction()
    # N'oublier surtout pas de le re-commenter avant de lancer l'interface
    #utilisateur
############################ TRES IMPORTANT
   
   
   
#============================================== End Frank Add