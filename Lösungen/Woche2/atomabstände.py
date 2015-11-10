atom_list = [] # hier werden die Atomnamen gespeichert...
position_list = [] # und hier ihre Positionen
with open("molecule-example.xyz", "r") as f:
    for i, line in enumerate(f):
        if i >= 2: # wir ignorieren die ersten beiden Zeilen
            line_split = line.split() # jede Zeile wird gesplittet in eine Liste, die Atomname, x-, y- und z-Position enthält
            atom_list.append(line_split[0]) # der Name kommt in atom_list
            position_list.append([float(pos) for pos in line_split[1:]]) # die Liste der Atompositionen enthält noch Strings, und muss daher zu float gecastet werden


atom_counter = 0
for atom1, position1 in enumerate(atom_list, position_list):
    if atom1 == "H":
        x1, y1, z1 = position1
        for atom2, position2 in enumerate(atom_list, position_list):
            if atom2 == "O":
                x2, y2, z2 = position2
                if 
