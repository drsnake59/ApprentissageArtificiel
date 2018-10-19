#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def figure():
	X = np.array([[6], [8], [10], [14], [18]])
	Y = [7, 9, 13, 17.5, 18]
	plt.scatter(X,Y)
	m = LinearRegression()
	m.fit(X,Y)
	plot_x = np.arange(0,25,0.1).reshape(-1,1)
	plt.plot(plot_x,m.predict(plot_x))
	plt.show()
	
def RSS():
	

def main():
	figure()

main()
