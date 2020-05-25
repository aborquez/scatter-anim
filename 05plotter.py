import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#Control de animacion

control = int(raw_input('1 <= control <= 10 : '))

#Obtencion de datos

t  = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

#Lee los datos guardados

archivo = open('data')
for linea in archivo:
	linea = linea.strip()        #quita los \n
	linea = linea.split(':')     #convierte la linea en una lista de elementos
	t.append(int(linea[0]))
	x1.append(float(linea[1]))
	y1.append(float(linea[2]))
	x2.append(float(linea[3]))
	y2.append(float(linea[4]))
	x3.append(float(linea[5]))
	y3.append(float(linea[6]))
archivo.close()

#Define a callback function; i: Frames; fig: Figure Object; scat: Scatter Object; set_offsets([x1, y1], ..., [xN, yN])

def update_plot(i, fig, scat):
	scat.set_offsets(([x1[i], y1[i]], [x2[i], y1[i]], [x3[i], y3[i]]))
	print("Frames: %d" %i)
	return scat,

#Posiciones iniciales

x = [x1[0], x2[0], x3[0]]
y = [y1[0], y2[0], y3[0]]

#Grafico

fig = plt.figure()

ax = fig.add_subplot(111)
ax.grid(True, linestyle = '-', color = '0.75')
ax.set_xlim([-150, 150])
ax.set_ylim([-150, 150])

#Ubica las particulas

area = np.pi * (6)**2 
scat = plt.scatter(x, y, s = area, c = ['k', 'b', 'r'])

#Se encarga de la animacion

anim = animation.FuncAnimation(fig, update_plot, fargs = (fig, scat), frames = len(t), interval = len(t)*control)

#Muestra el resultado

plt.show()

#Por Andres Borquez Carcamo