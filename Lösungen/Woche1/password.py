passwort = "geheim"
fehlversuche = 0

while True:
    user_input = raw_input("Passwort eingeben:\n")
    if user_input == passwort:
        print "Hello User!"
        break
    else:
        fehlversuche += 1
        print "Fehlversuche:", fehlversuche
    if fehlversuche == 3:
        print "Zu viele Fehlversuche"
        break
        
