#!/usr/bin/python
#encoding=utf-8
import numpy as np


# Explizite Formel (siehe z.B. Wikipedia)
def inverse_2x2(mat):
    if mat.shape != (2, 2):
        raise ValueError("Bitte nur 2x2 Matrizen eingeben!")
    
    return 1./np.linalg.det(mat) * np.array([[mat[1, 1], -mat[0, 1]], [-mat[1, 0], mat[0, 0]]])


# Bestimme die Adjunkte einer Matrix
def adjugate(mat):
    adj = np.zeros(mat.shape)
    for i in xrange(mat.shape[0]):
        for j in xrange(mat.shape[1]):
            # Erzeuge eine boolsche Matrix mit True gefüllt
            selection_mat = np.ones(adj.shape, dtype=bool)
            # Zeile i, und Spalte j werden auf False gesetzt
            selection_mat[i, :] = False
            selection_mat[:, j] = False
            # ipdb.set_trace()
            adj[i, j] = (-1)**(i+j) * np.linalg.det(mat[selection_mat].reshape((mat.shape[0]-1, mat.shape[1]-1)))
    return adj.T


# Bestimme die Inverse mittels der Cramerschen Regel
def inverse(mat):
    return 1./np.linalg.det(mat) * adjugate(mat)


x = np.random.randint(1, 125, size=(10, 10))
inv = inverse(x)
# Test, ob alles stimmt:
print np.allclose(inv, np.linalg.inv(x))

# Hinweis: np.linalg.inv bestimmt die Inverse einer Matrix
