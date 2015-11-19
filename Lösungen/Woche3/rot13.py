#!/usr/bin/env python

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_verschoben = alphabet[13:] + alphabet[:13]

verschluesselungs_dict = dict()

for c1, c2 in zip(alphabet, alphabet_verschoben):
    verschluesselungs_dict[c1] = c2

def caesar(text):
    verschluesselt = []
    for c in text:
        if c in verschluesselungs_dict:
            verschluesselt.append(verschluesselungs_dict[c])
        else:
            verschluesselt.append(c) # wenn der Buchstabe nicht im Dictionary gespeichert ist, speichern wir den Buchstaben selbst
    return "".join(verschluesselt)
    
print caesar("hallo welt")
print caesar(caesar("hallo welt")) # test, ob wir alles richtig gemacht haben. zwei mal angewandt kommt wieder der klartext raus
