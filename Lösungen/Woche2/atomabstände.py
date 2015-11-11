#!/usr/bin/python
#encoding=utf-8

atom_list = [] # hier werden die Atomnamen gespeichert...
position_list = [] # und hier ihre Positionen
with open("molecule-example.xyz", "r") as f:
    for i, line in enumerate(f):
        if i >= 2: # wir ignorieren die ersten beiden Zeilen
            line_split = line.split() # jede Zeile wird gesplittet in eine Liste, die Atomname, x-, y- und z-Position enthält
            atom_list.append(line_split[0]) # der Name kommt in atom_list
            position_list.append([float(pos) for pos in line_split[1:]]) # die Liste der Atompositionen enthält noch Strings, und muss daher zu float gecastet werden


atom_counter = 0
# Wir iterieren über alle Atome und suchen uns die Hs raus
for atom1, position1 in zip(atom_list, position_list):
    if atom1 == "H":
        # Sobald wir ein H gefunden haben, speichern wir seine Position und suchen nach Sauerstoffatomen
        x1, y1, z1 = position1
        for atom2, position2 in zip(atom_list, position_list):
            if atom2 == "O":
                x2, y2, z2 = position2
                distance_squared = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
                if distance_squared <= 4:
                    atom_counter += 1
                    break # Sobald wir wissen, dass es ein nahegelegenes Sauerstoffatom gibt, müssen wir nicht weiter suchen. Die Schleife über atom2, position2 wird abgebrochen

print "{} Wasserstoffatome sind nicht mehr als 2 Angström von einem Sauerstoffatom entfernt".format(atom_counter)



# Jetzt das ganze für Phosphor. Diesmal müssen wir jedoch für jedes Phosphoratom zählen

phosphorus_counter = 0
# Wir iterieren über alle Atome und suchen uns die Ps raus
for atom1, position1 in zip(atom_list, position_list):
    if atom1 == "P":
        # Sobald wir ein P gefunden haben, speichern wir seine Position, setzen den Sauerstoff-Zähler auf Null und suchen nach Sauerstoffatomen
        phosphorus_counter += 1 # Optional zählen wir noch die Phosphoratome
        oxygen_counter = 0
        x1, y1, z1 = position1
        for atom2, position2 in zip(atom_list, position_list):
            if atom2 == "O":
                x2, y2, z2 = position2
                distance_squared = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
                if distance_squared <= 4:
                    oxygen_counter += 1
        print "In der Nähe von Phosphoratom Nr.{} sind {} Sauerstoffatome".format(phosphorus_counter, oxygen_counter)

