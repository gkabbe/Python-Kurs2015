#!/usr/bin/python
#encoding=utf-8
from getpass import getpass


unbekanntes_wort = getpass("Bitte zu ratendes Wort eingeben\n").decode("utf-8") # das decode ist nur notwendig für Wörter mit Umlaut oder Sonderzeichen
geratene_woerter = set()

maximale_fehlversuche = 11
fehlversuche = 0

while True:
    print "Sie haben noch {} Versuche".format(maximale_fehlversuche - fehlversuche)
    neuer_buchstabe = raw_input("Bitte einen Buchstaben raten:\n").decode("utf-8").lower() # alle eingegeben Wörter werden mit lower() kleingemacht, um zu vermeiden, dass zwischen Groß- und Kleinbuchstaben unterschieden wird
    if len(neuer_buchstabe) > 1: # Wenn der User mehr als einen Buchstaben eingibt, weisen wir ihn darauf hin
        print "Nur einen Buchstaben!"
    else:
        if neuer_buchstabe in geratene_woerter: # Falls der Buchstabe schon geraten wurde, sind wir so fair und weisen darauf hin
            print "Dieser Buchstabe wurde schon geraten"
            print "Sie haben bisher geraten:", ", ".join(geratene_woerter)
        else:
            geratene_woerter.add(neuer_buchstabe)
            if neuer_buchstabe not in unbekanntes_wort: # Falls der geratene Buchstabe nicht im zu ratenden Wort vorkommt, wird die Zahl der Fehlversuche um 1 erhöht
                fehlversuche += 1
    
    # Hier zählen wir die Anzahl der noch nicht geratenen Buchstaben
    missing = 0
    for buchstabe in unbekanntes_wort:
        if buchstabe.lower() in geratene_woerter:
            print buchstabe,
        else:
            print "-",
            missing += 1
    print ""
    
    if missing == 0: # Wenn kein Buchstabe mehr fehlt, hat der User gewonnen
        print "Glückwunsch!"
        break
   
    if fehlversuche == maximale_fehlversuche: # Bei zu vielen Fehlversuchen erscheint Game Over
        print "Zu viele Fehlversuche"
        print "Game Over"
        break

