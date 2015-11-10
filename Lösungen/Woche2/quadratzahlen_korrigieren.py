#!/usr/bin/python
#encoding=utf-8

# Variante 1 - manuell

quadrat_zahlen = [1, 4, 9, 16, 26, 36, 49, 64, 81, 100]
quadrat_zahlen[4] = 25
quadrat_zahlen.append(121)
print quadrat_zahlen

# Variante 2 - automatisch

quadrat_zahlen = [1, 4, 9, 16, 26, 36, 49, 64, 81, 100]
for i, qz in enumerate(quadrat_zahlen, 1):
    if i*i != qz:
        quadrat_zahlen[i-1] = i*i
quadrat_zahlen.append((len(quadrat_zahlen)+1)**2)
print quadrat_zahlen


# Achtung, folgendes geht nicht!
quadrat_zahlen = [1, 4, 9, 16, 26, 36, 49, 64, 81, 100]
for i, qz in enumerate(quadrat_zahlen, 1):
    if i*i != qz:
        qz = i*i # das ändert den Wert von quadrat_zahlen[4] nicht!
print quadrat_zahlen
