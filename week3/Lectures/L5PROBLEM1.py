def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    total = 1
    iterator = int(exp)
    while iterator > 0:
        total *= base
        iterator -= 1
    return total     
        
