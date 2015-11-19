def max1(a, b):
    if a > b:
        return a
    else:
        return b
        

def max_liste(l):
    maxi = None
    for zahl in l:
        if maxi == None or zahl > maxi:
            maxi = zahl
    return maxi
