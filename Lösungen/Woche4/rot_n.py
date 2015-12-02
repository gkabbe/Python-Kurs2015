#!/usr/bin/env python


def rot_n(n):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_lower_verschoben = alphabet_lower[n:] + alphabet_lower[:n]
    alphabet_upper = 'abcdefghijklmnopqrstuvwxyz'.upper()
    alphabet_upper_verschoben = alphabet_upper[n:] + alphabet_upper[:n]

    verschluesselungs_dict = dict()
    
    for alphabet, alphabet_verschoben in ((alphabet_lower, alphabet_lower_verschoben), (alphabet_upper, alphabet_upper_verschoben)):
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
    return caesar


r1 = rot_n(1)
r2 = rot_n(2)
print r1("hallo welt")
print r_m2("Hallo Welt")
