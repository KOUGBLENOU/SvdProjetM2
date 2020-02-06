######################################################
#       PROJET M2 APPRENTISSAGE NON SUPERVISEE       #
#       PLOTDATACOMPUTE.py FILE                      #
#       AUTHORS :                                    #
#           *** Masood S.                            #
#           *** Ben A.                               #
#           *** Frank K2                             #
#       LAST UPDATE : 06/02/2020                     #
#       OBJECT :                                     #
#           *** compute trace([0 => p ])             #
#           *** X[p'] et Y[trace(p')]                #
######################################################

#============================================== Frank Add
import trace

def PlotDataComputer(S,p):
    
## We have to find a way to optimize this function!!! it takes too long time
    i=0
    X=[0 for i in range(0,p)]
    Y=[0 for i in range(0,p)]
    pp=0
    TraceForAllP     = trace.traceComputer(S,p) # Compute trace (p)
    while ( pp < p) :
        X[pp] = pp  # Abscice
        Y[pp] = 100*(TraceForAllP - trace.traceComputer(S,pp) )/TraceForAllP # ordonnee
        #Y[pp] = trace.traceComputer(S,pp)
        pp   += 1
        
    return X,Y
    

#============================================== End Frank Add