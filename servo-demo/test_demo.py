import pytest
import time
import random
import matplotlib.pyplot
from PIL import Image

def foo():
    return 5

def plot():
    '''Plottet die Laufzeiten der Sortierverfahren in einem Diagramm '''
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1,1,1)

    # Funktion [x ; y]
    # x: Anzahl der Elemente -- y: Zeit zum sortieren
    ax.plot([x for x in range(0, 10)], [t for t in range(0, 10)],  '-', color='c', )

    # Legende
    ax.set_title('Servo Demo RPM Verlauf')
    ax.legend(['BubbleSort'])
    ax.set_xlabel('Zeit in s')
    ax.set_ylabel('rpm')
    matplotlib.pyplot.savefig('test.png')
    # matplotlib.pyplot.show()
    return 1

def show():
    image = Image.open('test.png')
    image.show()
    return 1

def test_foo():
    assert foo() == 5

def test_rpm():
    assert plot() == 1
    assert show() == 1
    