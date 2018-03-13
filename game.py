def game(p1,p2):
    """
    Enter values that present the player choice
    Return 1 if player wins otherway p2
    """ 
    if (p1 =='piedra' and p2=='tijera') or (p1 == 'tijera' and p2 == 'papel')or(p1 == 'papel' and p2 == 'piedra'):
        return 'gana p1'
    elif(p1==p2):
        return'empate'
    else:
        return'gana p2'
 
