######################################################
#       PROJET M2 APPRENTISSAGE NON SUPERVISEE       #
#       CENTERING.py FILE                            #
#       AUTHORS :                                    #
#           *** Masood S.                            #
#           *** Ben A.                               #
#           *** Frank K2                             #
#       LAST UPDATE : 06/02/2020                     #
#       OBJECT :                                     #
#               Center the input matrice X if the    #
#                "flag" is true                      #
######################################################

# ============================================== Frank Add


def Center(inputX, MaxLine, MaxCol, SumVector, flag):

    # ReturnArray = [[0 for i in range(MaxCol)] for i in range(MaxLine)] # A [MaxLine, MaxCol ] matrice
    ReturnArray = inputX
    if flag:
        for i in range(0, MaxLine, 1):
            for j in range(0, MaxCol, 1):
                ReturnArray[i][j] -= SumVector[j]/MaxLine  # Subtract the average

    return ReturnArray

# ============================================== Frank Add
