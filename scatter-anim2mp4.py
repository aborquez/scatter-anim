# scatter-anim2mp4.py
# gravitons branch

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker
import numpy as np

# remove toolbar
plt.rcParams['toolbar'] = 'None'

# animation control
control = float(raw_input('0.0001 <= control <= 1 : '))

# setup animation
Writer = animation.writers['ffmpeg']
writer = Writer(fps = 30, metadata=dict(Artist='me'), bitrate=1800)

# define arrays to store data
t  = []
x1 = []
y1 = []
x2 = []
y2 = []

# read data file
archivo = open('out.txt')
for linea in archivo:
	linea = linea.strip()        # removes \n
	linea = linea.split(':')     # converts text line into array
	t.append(float(linea[0]))
	x1.append(float(linea[1]))
	y1.append(float(linea[2]))
	x2.append(float(linea[3]))
	y2.append(float(linea[4]))
archivo.close()

# define a callback function; i: Frames; fig: Figure Object; scat: Scatter Object; set_offsets([x1, y1], ..., [xN, yN])
def update_plot(i, fig, scat):
	scat.set_offsets(([x1[i], y1[i]], [x2[i], y2[i]]))
	print("Frames: %d" %i)
	return scat,

# define font options
font = {'family' : 'serif', 'color' : 'black', 'weight' : 'normal', 'size' : 16}

# define initial positions
x = [x1[0], x2[0]]
y = [y1[0], y2[0]]

# define plot
fig = plt.figure()

# assign plot and axes titles
plt.title('Scattering', fontdict = font, size = 24) # pad = 10
plt.xlabel('x (m)', fontdict = font)
plt.ylabel('y (m)', fontdict = font)

# define axes and grid
ax = fig.add_subplot(111)
ax.set_axisbelow(True) # put grid behind the particles!
ax.grid(True, linestyle = '-', color = '0.75')
ax.set_xlim([-0.1, 0.1])
ax.set_ylim([-0.1, 0.1])

# axis tick labels in scientific notation
yfmt = ticker.ScalarFormatter(useMathText = True)
ax.xaxis.set_major_formatter(yfmt)
ax.yaxis.set_major_formatter(yfmt)
ax.ticklabel_format(axis = 'x', style = 'sci', scilimits = (0,0))

# text box
ax.text(-0.062, 0.087, "M_g = ... (kg)", ha = 'center', va = 'center', size = 16, bbox=dict(boxstyle = 'square', fc = 'w')) # fc = facecolor

# set particles shape, size, initial positions and colors
area = np.pi * (2.5)**2 
scat = plt.scatter(x, y, s = area, c = ['k', 'b']) # 'k' = black, 'b' = blue

# start animation
anim = animation.FuncAnimation(fig, update_plot, fargs = (fig, scat), frames = len(t), interval = len(t)*control)

# save animation
anim.save('out.mp4', writer=writer)
        
# show plot
plt.show()
