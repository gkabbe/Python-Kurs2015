#!/usr/bin/python

import numpy as np
from PIL import Image


def main(*args):
    real = np.linspace(-2, 2, 8000)
    imag = np.linspace(-1, 1, 4000)[:, np.newaxis]
    c = real + 1j*imag
    
    z = np.zeros(c.shape, dtype=np.complex)
    counter = np.zeros(c.shape, dtype=np.int)

    for i in xrange(100):
        z = z**2 + c
        counter += np.abs(z) < 10
        
    counter = np.array(counter/100. * 255, dtype=np.uint8)
    img = Image.fromarray(counter)
    img.save("test.png")
    

if __name__ == "__main__":
    main()
