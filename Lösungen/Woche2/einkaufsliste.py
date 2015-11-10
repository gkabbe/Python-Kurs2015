#!/usr/bin/python
#encoding=utf-8


einkaufs_liste = ["apfel", "milch", "banane", "joghurt", "käse"]
preise = [0.40, 0.59, 0.30, 1.20, 2.30]

for elem in einkaufs_liste:
    print elem

for i, elem in enumerate(einkaufs_liste):
    print i, ". Element ist", elem # wem das Leerzeichen nach i nicht gefällt, kann folgendes schreiben:
    print "{}. Element ist {}".format(i, elem)

for elem, preis in zip(einkaufs_liste, preise):
    print "{} kostet {:.2f} €".format(elem, preis) # .2f in {} sorgt für 2 Nachkommastellen


print "# Nur jedes zweite Element:"
for elem, preis in zip(einkaufs_liste, preise)[::2]:
    print "{} kostet {:.2f} €".format(elem, preis)
