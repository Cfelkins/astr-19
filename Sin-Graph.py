import numpy as np
import matplotlib.pyplot as plt

def main():
	#make x axis range between 0 and 2pi broken into 1000 points 
	x = np.arange(0, 2*np.pi, .001)
	#y is the sin of x
	y = np.sin(x)

	plt.plot(x,y)    #make a plot of this relationship
	#label the axes
	plt.xlabel('x')
	plt.ylabel('sin(x)')
	plt.show()            #show the graph on screen
if __name__ == "__main__":
	main()
