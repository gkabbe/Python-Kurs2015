# !/usr/bin/python
# coding=utf-8

n_max = 1000
numbers = set(range(2, n_max+1)) # erstellt eine Menge mit Zahlen von 2 bis n_max
next_prime = 2

while next_prime < n_max/2:
    if next_prime in numbers: 
        to_be_deleted = {next_prime*i for i in range(2, n_max/next_prime+1)} # lösche alle Vielfachen der Primzahl
        numbers -= to_be_deleted # äquivalent zu numbers = numbers - to_be_deleted. subtrahiert alle Vielfachen von numbers
    next_prime += 1
    
for number in numbers:
    print number,
