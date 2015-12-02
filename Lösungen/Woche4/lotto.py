#!/usr/bin/python -u
#encoding=utf-8

import random
from collections import defaultdict

lottery_numbers = range(1, 50)

def lottery_draw():
    random.shuffle(lottery_numbers)
    return lottery_numbers[:6]

def count(guess, drawing):
    counter = 0
    for number in guess:
        if number in drawing:
            counter += 1
    return counter

# Unser Tipp: 
guess = lottery_draw() # wer will, darf auch seine eigene Glückskombination hier eintragen. Ändert eh nichts ;-)
histogram = defaultdict(int)

for i in xrange(1000000): # Tipp: xrange ist etwas effizienter im Speicherverbrauch als range, da hierfür keine Liste mit 10**6 Einträgen erstellt wird
    draw = lottery_draw()
    histogram[count(guess, draw)] += 1
    if i % 1000 == 0:
        print i,"\r",
print ""
    
for i in range(7):
    print i, "richtige:", histogram[i]
    
