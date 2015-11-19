def mat_mul(mat_a, mat_b):
    result = [len(mat_b[0])*[0] for i in range(len(mat_a))] # erzeuge leere Liste von Listen, die so viele Zeilen wie Matrix A und Spalten wie Matrix B hat
    for i in range(len(result)):
        for j in range(len(result[0])):
            for k in range(len(mat_a[0])):
                result[i][j] += mat_a[i][k]*mat_b[k][j]
    return result


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
e = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
c = mat_mul(e, a)

for line in c:
    for c in line:
        print c,
    print ""
