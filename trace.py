######################################################
#       PROJET M2 APPRENTISSAGE NON SUPERVISEE       #
#       TRACE.py FILE                                #
#       AUTHORS :                                    #
#           *** Masood S.                            #
#           *** Ben A.                               #
#           *** FRANK K2                             #
#       LAST UPDATE : 06/02/2020                     #
#       OBJECT :                                     #
#               compute trace(S^2) when learning p   #
#                  informations                      #
######################################################

#============================================== Frank Add

def traceComputer (s, p):
    trace = 0
    i = 0
    while (i< p):
        trace +=s[i]*s[i]
        i+=1
    return trace

#============================================== End Frank Add