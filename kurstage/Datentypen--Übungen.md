### Listen ###

* Quadratzahlen korrigieren  
  Gegeben sei folgende Liste:
  ```python
  quadrat_zahlen = [1, 4, 9, 16, 26, 36, 49, 64, 81, 100]
  ```
  Finden Sie die fehlerhafte Quadratzahl und ersetzen Sie sie mit der korrekten Zahl.

* Einkaufliste:
  * Erstellen Sie eine Einkaufsliste bestehend aus 10 Produkten, sowie eine Liste mit den dazugehörigen Preisen

  * Iterieren Sie nun über Gegenstand und Preis, so dass Sie als Ausgabe bekommen:
    ```
    Gegenstand_1, Preis_1
    Gegenstand_2, Preis_2
    ...
    Gegenstand_10, Preis_10
    ```

  * Lassen Sie sich nun nur jeden zweiten Gegenstand ausgeben

* Erstellen Sie eine Liste der Quadratzahlen von 1 bis 400


### Wortzähler ###

The Zen of Python, by Tim Peters

Beautiful is better than ugly  
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
Namespaces are one honking great idea  let us do more of those


* Schreiben Sie ein Programm, das die Häufigkeit jedes Wortes im obigen Text zählt.
  
  Hilfestellungen:
  * Speichern Sie den Text entweder als String mit 3 Anführungszeichen am Anfang und am Ende (dann kann er sich auch über mehrere Zeilen erstrecken), oder lesen Sie ihn aus einer Datei aus, in die Sie ihn vorher geschrieben haben.

  * Angenommen, Sie haben den gesamten Text in der Variablen _text_ gespeichert. Dann können Sie mit 
    ```python
    wortliste = text.split()
    ```
  eine Liste der einzelnen Wörter erstellen.

  * Um ungewünschte Zeichen aus dem Text zu entfernen, benutzen Sie:
    ```python
    text.replace(zu_ersetzendes_zeichen, "")
    ```

  * Zum Zählen der Wörter ist ein Dictionary sehr hilfreich! 

* Schreiben Sie das Programm nun so um, dass es die Häufigkeit der einzelnen Buchstaben zählt.

* Benutzen Sie Sets (Mengen), um herauszufinden, welche Wörter in jeder der ersten 6 Zeilen vorkommen.

* Erstellen Sie mithilfe von Sets eine Liste aller Buchstaben, die in dem Text vorkommen