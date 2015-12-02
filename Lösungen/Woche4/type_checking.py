#!/usr/bin/python
#encoding=utf-8
import types

def check_if_number(fct):
    def new_fct(*args):
        for a in args:
            if type(a) != types.IntType and type(a) != types.FloatType:
                raise ValueError("Argument ist weder int noch float")
        return fct(*args)
    return new_fct
    
# Hier ein kleiner Test

@check_if_number
def summe(a, b, c):
    return a+b+c
    
print summe("Hallo ", "Welt", "!") # Bricht mit ValueError ab. Wenn wir den Decorator oben aber entfernen, funktioniert es
