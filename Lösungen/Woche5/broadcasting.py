#!/usr/bin/python

import numpy as np
import ipdb

atoms = np.array([[0., 0., 0.],
                  [3., 3., 3.],
                  [2., 8., 7.]]
                 )

masses = np.array([1., 1., 5.])


new_positions = atoms + [1, 2, 3]

center_of_mass = atoms.mean(axis=0)
