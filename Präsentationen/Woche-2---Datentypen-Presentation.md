# Organisatorisches #
* Hat es schon jemand geschafft, Python bei sich auf dem Laptop zu installieren?
* Hat es jemand nicht geschafft und braucht Hilfe?
* Vorschlag: nach Beendigung der Grundlagen Projektarbeit? Wahl zwischen physikalischen, chemischen, ... Problemstellungen und anschließende kurze Präsentation

# Listen #

## Erstellen einer Liste ##

```python
meine_liste = []
meine_zweite_liste = list()
```

oder

```python
meine_liste = ["a", "b", "c"]
```

oder

```python
meine_liste = []
meine_liste.append("a")
meine_liste.append("b")
meine_liste.append("c")
```
___

## Zugreifen auf ein Element ##


```python
dreier_liste = ["bla", "bli", "Blub"]
element1 = dreier_liste[0]
element2 = dreier_liste[1]
element3 = dreier_liste[-1] # geht auch von hinten
```

## Entfernen von Elementen ##

```python
entferntes_element = meine_liste.pop(2)
```

## Listen miteinander verknüpfen ##


```python
l1 = [1, 2, 3]
l2 = ["a", "b", "c"]
liste_gesamt = l1 + l2
print liste_gesamt
```
___


## Element in Liste enthalten? ##

```python

buchstaben = ["a", "b", "c", "d", "e"]
print "c" in buchstaben
print "f" in buchstaben
```


## Was kann eine Liste speichern? ##


```python
bunt_gemischt = ["hallo", [1, 2, 3], 3.456, 5+3j, 
                 True, False] # geht, muss aber nicht...
```

## Iterieren über Listen ##

```python
for element in bunt_gemischt:
    print element
```

## Enumerate ##

```python
for i, element in enumerate(bunt_gemischt):
    print "Das", i, "te Element meiner Liste ist:", 
    print element
```

___

### Ein praktisches Beispiel ###

Ein Chemiker hat in seinem Grundpraktikum alle 20 Sekunden die Konzentration eines bestimmten Stoffes aufgeschrieben. Die resultierende Liste sieht dann so aus:

```python
konzentrationen = [1.000,
                   0.880,
                   0.756,
                   0.656,
                   0.582,
                   ...
                   0.130,
                   0.109,
                   0.099,
                   0.079,
                   0.078,
                   0.064
                  ] 
```

___

```python
print "Zeit in Sekunden,  Konzentration"
for index, messwert in enumerate(konzentrationen):
    print index*20, messwert
```

___

## Listen "slicen" ##

* Möglichkeit auf Teilliste zuzugreifen?
  (z.B. jedes zweite Element, nur die ersten 9 Elemente, etc.)

```python
teil_liste = liste[start:stop:schritt]
```

Bsp: nur jedes dritte Element bis Index 30


Unser Beispiel:

```python
teil_liste = zahlenliste[0:30:3]
```

Übungsaufgabe: Teilliste erstellen, _ohne_ die Slicing Syntax zu benutzen.

___

### Merkhilfe für die Index-Benutzung beim Slicen ###

Folgendes Schaubild ([Quelle](https://docs.python.org/2/tutorial/introduction.html#strings)) macht anschaulich klar, wie die Indizes beim Slicen zu verstehen sind.

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

Trennlinien zwischen den Elementen zählen!

___

## Listen sortieren ##

Entweder mit der Methode _sort_, oder mit der Funktion _sorted_ sortieren.

**sorted**

```python
l1 = [8, 3, 12, 2]
l2 = sorted(l1)
```

-> neue sortierte Liste, alte bleibt erhalten!


**sort**

```python
l1 = [8, 3, 12, 2]
l1.sort()
```

-> l1 wird sortiert, alte Sortierung geht verloren!

___

### Absteigend sortieren ###


```python
l1 = [8, 3, 12, 2]
l1.sort(reverse=True)
```

___

## Unveränderliche Listen (Tupel) ##

```python
mein_tupel = (1, 2, 3)
```


```python
meine_liste = [1, 2, 3]
mein_tupel = tuple(meine_liste)
```

___

### Listen/Tupel entpacken ###

```python
dreier_tupel = ("Müller", "Daniel", 1.0)
```

Wie speichern wir die drei Werte in die 3 Variablen Vorname, Nachname und Note?

___

__Methode 1__

```python
nachname = dreier_tupel[0]
vorname = dreier_tupel[1]
note = dreier_tupel[2]
```

___


__Methode 2__

```python
(nachname, vorname, note) = dreier_tupel
```

-> linke Seite, rechte Seite brauchen gleich geschachtelte Tupel!

```python
name, vorname = "Müller", "Heinz"
```
___

## Listen zippen (der Reißverschluss) ##

Wie iteriert man am besten über Elemente mehrerer Listen gleichzeitig?

Beispiel: 

```python
nachnamen_liste = ["Müller", "Maier", "Schulz"]
vornamen_liste = ["Daniel", "Dieter", "Elise"]
noten_liste = [1.0, 2.3, 3.7]
```


```python
for vn, nn, note in zip(vornamen_liste, nachnamen_liste, noten_liste):
    print vn, nn, note
    
```

___

Betrachte das Ergebnis von zip:

```python
print zip(nachnamen_liste, vornamen_liste, noten_liste)
```

Ausgabe:

```
[('Müller', 'Daniel', 1.0), 
('Maier', 'Dieter', 2.3), 
('Schulz', 'Elise', 3.7)]
```

-> Liste von Tupeln!

-> In jedem Durchlauf der For-Schleife wird ein Tupel entpackt


<!-- Noch ein wichtiger Hinweis:

Möchten wir nur über gezippte Listen iterieren (wie im obigen Beispiel mit den Namen und Noten), reicht
```python
for el1, el2, el3, ... in zip(liste1, liste2, liste3, ...):
    ...
```

Möchten wir jedoch explizit eine Liste erhalten, müssen wir schreiben:
```python
liste_gezippt = list(zip(liste1, liste2, liste3, ...))
```
-->

___

## List comprehensions ##

Bestimme Teilliste aus vorhandener Liste nach bestimmten Kriterien

```python
tiere = ["Affe", "Löwe", "Giraffe", "Schlange", "Nashorn"]
```

Nur Tiere mit Namen, die mindestens 5 Buchstaben lang sind:

```python
tiere_2 = [tier for tier in tiere if len(tier) >= 5]
```

Ungerade Zahlen von 1 bis 20:

```python
ungerade_zahlen = \
[zahl for zahl in range(1, 20) if zahl % 2 != 0]
```

# Strings <-> Listen Vergleich #

Gemeinsamkeiten Strings - Listen:

___

## Addition ##

```python
s1 = "Guten "
s2 = "Tag"
s3 = s1 + s2
print(s3)
```
Ausgabe:
```
Guten Tag
```

## Slicen ##

```python
text = "Einen schönen guten Tag"
print(text[::2]) # gibt jeden zweiten Buchstaben aus
```
Ausgabe:
```
EnnshnngtnTg
```

## Außerdem ##

* Iterieren
* Sortieren

# Mengen (Sets) #

Erstellen via

```python
menge = set([1, 2, 3, 4, 1, 2])
print menge
```

oder 

```python
menge = {1, 2, 3, 4, 1, 2}
print menge
```

Da eine Menge jedes Element nur einmal enthält, ist die Ausgabe:

```
{1, 2, 3, 4}
```
___

## Mengenoperationen ##

### Schnitt ###
 
````python
a = {1, 2, 3, 4}
b = {1, 4, 6, 7, 8}

print a & b
````
Ausgabe:

````
{1, 4}
````

___

### Vereinigung ###
 
````python
a = {1, 2, 3, 4}
b = {1, 4, 6, 7, 8}

print a | b
````

Ausgabe:

````
{1, 2, 3, 4, 6, 7, 8}
````
___


### Differenz ###
 
````python
a = {1, 2, 3, 4}
b = {1, 4, 6, 7, 8}

print a - b
print b - a
````
Ausgabe:

````
{2, 3}
{6, 7, 8}
````
___


### Symmetrische Differenz ###
 
````python
a = {1, 2, 3, 4}
b = {1, 4, 6, 7, 8}

print a ^ b
````

Ausgabe:

````
{2, 3, 6, 7, 8}
````
___


### Test, ob Element in Menge ###

```python
print 1 in {1, 2, 3}
print "a" in {1, 2, 3}
```
Ausgabe:

```
True
False
```

___

## Set Comprehensions ##


```python
gerade_zahlen = {i for i in range(0, 200, 2)}
```

# Assoziatives Datenfeld bzw. Wörterbücher (Dictionaries) #


## Erstellen eines Dictionaries ##


```python
my_dict = dict(a=1, b=2, c=3)
my_dict_2 = {"a":1, "b":2, "c":3}
```

```python
print my_dict["a"]
```
Ausgabe:
```
1
```

___

## Iterieren über alle Key, Value Paare ##


```python
my_dict = dict(a=1, b=2, c=3)
for key in my_dict:
    print key
```

Ausgabe:
```
a
c
b
```

Reihenfolge?

___


## Iterieren über Key und Value ##

```python
for key, value in my_dict.items():
    print key, ":", value
```

Ausgabe:

```
a : 1
c : 3
b : 2
```

## Dictionary Comprehensions ##


```python
quadrat_zahlen_dict = {i: i*i for i in range(10)}
```
