#!/usr/bin/python -u
#encoding=utf-8

import numpy as np
from PIL import Image


def main(*args):
    # An diesen Parametern darf (und soll!) gedreht werden ---------------------
    X_MIN, X_MAX = -2.2, .5 # kleinster und größter Realteil von c
    Y_MIN, Y_MAX = -1, 1 # kleinster und größter Imaginärteil von c
    WIDTH = 1200 # Pixel für die Breite
    # --------------------------------------------------------------------------
    HEIGHT = int(float(Y_MAX-Y_MIN)/(X_MAX-X_MIN) * WIDTH) # HEIGHT ergibt sich aus der Breite und dem gewählten Bildausschnitt
    
    real = np.linspace(X_MIN, X_MAX, WIDTH)
    imag = np.linspace(Y_MIN, Y_MAX, HEIGHT)[:, np.newaxis]
    c = real + 1j*imag
    
    z = np.zeros(c.shape, dtype=np.complex)
    counter = np.zeros(c.shape, dtype=np.int)

    for i in xrange(100):
        z = z**2 + c
        counter += np.abs(z) < 10
        print i, "\r",
    print ""
        
    counter = np.array((counter)/100. * 255, dtype=np.uint8)
    img = Image.fromarray(counter)
    img.save("mandelbrot.png")
    

if __name__ == "__main__":
    main()
