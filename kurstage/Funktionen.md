# Funktionen #

## Grundlagen ##

Um eine Funktion zu erstellen wird das _def_ keyword benötigt, anschließend kommt der Funktionsname, und dahinter eine Klammer, in die die Funktionsargumente geschrieben werden (falls die Funktion welche benötigt).

```python
def quadrat(x):
    return x*x
```

In dem oberen Beispiel hat die Funktion einen Rückgabewert. Das muss aber auch nicht zwingend sein:

```python
def hello_world():
    print("Hello World")
```

Man kann den Funktionsargumente Defaultwerte geben, die benutzt werden, falls die Funktion ohne Parameter aufgerufen wird:

```python
def summe(a=0, b=0, c=0):
    return a + b + c
    
print(summe())
```

Ausgabe:
```
0
```

Es ginge aber z.B. auch:

```python
summe(1, 2) # a und b werden auf 1 und 2 gesetzt, c bleibt 0

summe(a=100) # a wird auf 100 gesetzt

summe(3, c=99.912) # a wird auf 3 und c auf 99.912 gesetzt
```

Darüberhinaus ist es möglich, eine Funktion zu schreiben, die beliebig viele Argumente akzeptiert:

```python
def summe(*args):
    total = 0
    for value in args:
        total += value
    return total
```




## Besonderheiten in Python ##

## Funktionen als Objekte ##

