#!/usr/bin/python

def pascal_zeile(line_number):
    if line_number == 0: # in der nullten Zeile (also an der Spitze) steht nur eine Eins
        return [1]
    else:
        result = (line_number+1)*[0] # in der i-ten Zeile stehen i+1 Zahlen
        result[0] = 1 # am Anfang und am..
        result[-1] = 1 # ..Ende jeder Zeile steht eine Eins
        for i in xrange(1, line_number):
            result[i] = pascal_zeile(line_number-1)[i-1] + pascal_zeile(line_number-1)[i] # jede Zahl ergibt sich durch Addition zweier Zahlen aus der darüberliegenden Zeile
    return result
    
    
def print_pretty_pascal(n):
    result = []
    for i in range(n):
        result.append(pascal_zeile(i))
    maxlen = len(" ".join(map(str, result[-1])))
    for r in result:
        r_str = " ".join(map(str, r))
        print r_str.center(maxlen)


n = 8

print_pretty_pascal(n)    
