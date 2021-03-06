#!/usr/bin/python
#encoding=utf-8

text = """Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Flat is better than nested
Sparse is better than dense
Readability counts
Special cases are not special enough to break the rules
Although practicality beats purity
Errors should never pass silently
Unless explicitly silenced
In the face of ambiguity refuse the temptation to guess
There should be one and preferably only one obvious way to do it
Although that way may not be obvious at first unless you are Dutch
Now is better than never
Although never is often better than right now
If the implementation is hard to explain it is a bad idea
If the implementation is easy to explain it may be a good idea
Namespaces are one honking great idea let us do more of those"""

# Folgendes Dictionary speichert jedes im Text vorkommende Wort als Key. Als Value wird die Häufigkeit im Text gespeichert.
word_count = dict()

for word in text.split():
    if word not in word_count: # Falls das Wort noch nicht als Key in word_count enthalten ist...
        word_count[word] = 1 # setzen wir die Häufigkeit auf 1
    else:
        word_count[word] += 1 # Ist es schon enthalten, wird die Häufigkeit um 1 erhöht
        
print word_count


# Die obige Version hat jedoch noch ein kleines Problem: das Programm unterscheidet zwischen Groß- und Kleinschreibung. 
# Das Wort "Complex" wird z.B. einmal groß, einmal klein geschrieben. 
# Die Lösung besteht darin, alle Wörter klein zu speichern:

word_count = dict()

for word in text.split():
    if word.lower() not in word_count: # Die String Methode lower() macht alle Buchstaben zu Kleinbuchstaben
        word_count[word.lower()] = 1 
    else:
        word_count[word.lower()] += 1 
        
# Noch ein kleiner Trick: 
from operator import itemgetter # Was hier genau passiert besprechen wir bald...

print ""
print ""
print "Häufigkeiten:"
for word, number in sorted(word_count.items(), key=itemgetter(1), reverse=True): # key=itemgetter(i) lässt uns nach dem iten Element in Tupeln sortieren. Um nach der Häufigkeit zu sortieren, müssen wir also itemgetter(1) benutzen
    print number, "x", word


# Hier nun die Häufigkeiten der einzelnen Buchstaben:

letter_counter = dict()
text2 = text.replace(" ", "").replace("\n", "") # Entferne alle Leerzeichen und Zeilenumbrüche aus text
for letter in text2:
    if letter.upper() not in letter_counter:
        letter_counter[letter.upper()] = 1
    else:
        letter_counter[letter.upper()] += 1
print ""
print ""
print "Häufigkeiten der einzelnen Buchstaben:"
for letter, number in sorted(letter_counter.items(), key=itemgetter(1), reverse=True):
    print number, "x", letter


# Welche Wörter kommen in jeder der ersten 6 Zeilen vor?
beginning = text.splitlines()[:6] # Betrachten nur die ersten 6 Zeilen
gemeinsame_woerter = set(beginning[0].split()) # Erstelle eine Menge aus den Wörtern der nullten Zeile
for line in beginning[1:]:
    gemeinsame_woerter = gemeinsame_woerter & set(line.split()) # die neue Menge ist der Schnitt der alten Menge mit der Menge der Wörter aus der nächsten Zeile
print ""
print ""
print "Gemeinsame Wörter der ersten sechs Zeilen:"
print gemeinsame_woerter


# Liste aller Buchstaben:
buchstaben = sorted(list(set(text2)))
print buchstaben

