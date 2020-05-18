######################################################
#       PROJET M2 APPRENTISSAGE NON SUPERVISEE       #
#       REMAKE.py FILE                            #
#       AUTHORS :                                    #
#           *** Masood S.                            #
#           *** Ben A.                               #
#           *** Frank K2                             #
#       LAST UPDATE : 06/02/2020                     #
#       OBJECT :                                     #
#               reconstruct the initial DataBase     #
#                with param samples                  #
######################################################

# ============================================== Frank Add
import numpy as np

def remake(In, Param):
    data = In
    ########## Centrer
    data_centered= data - data.mean(axis=0); 
    ########## SVD
    U, s, Vt = np.linalg.svd(data_centered, full_matrices=False)

    Sigma = np.zeros((data_centered.shape[0], data_centered.shape[1]))
    Sigma= np.diag(s)
    ########## Select components
    Sigma = Sigma[:Param, :Param]
    Vt = Vt[:Param, :]
    U = U[:, :Param]
    
    ##########  Remake
    R = U.dot(Sigma.dot(Vt))
    R = R + data.mean(axis=0)
    
    return R
