import time
import random
import matplotlib.pyplot
import matplotlib

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
    matplotlib.pyplot.savefig('testi.png')
    
    img = matplotlib.image.imread('testi.png')
    imgplot = matplotlib.pyplot.imshow(img)
    matplotlib.pyplot.show()

def main():
    '''Main Funktion '''
    plot()


if __name__ == "__main__":
    main()