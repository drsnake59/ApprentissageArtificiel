#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def figure():
	X = np.array([[6], [8], [10], [14], [18]])
	Y = [7, 9, 13, 17.5, 18]
	
	plt.scatter(X,Y)
	m = LinearRegression()
	m.fit(X,Y)#regression X et Y
	
	plot_x = np.arange(0,25,0.1).reshape(-1,1)#de 0 à 25 par pas de 0.1
	plt.plot(plot_x,m.predict(plot_x))
	plt.show()

def rss(X,Y):
	sommeRss=0
	for i in range(len(Y)):
		sommeRss=sommeRss+(Y[i]-X[i])*(Y[i]-X[i])
	return sommeRss

def var(X):
	val=np.var(X, ddof=1)
	return val

def coVar(X,Y):
	val=np.cov(X.transpose(), Y)[0][1]
	return val
	
def alpha(X,Y):
	alpha=coVar(X,Y)/var(X)
	return alpha
	
def beta(X,Y):
	beta=np.mean(Y)-alpha(X,Y)*np.mean(X)
	return beta


def main():
	X = np.array([[6], [8], [10], [14], [18]])
	Y = [7, 9, 13, 17.5, 18]
	
	X2 = np.array([[8], [9], [11], [16], [12]])
	Y2 = [11, 8.5, 15, 18, 11]

	#figure()
	
	valrss=rss(X,Y)
	valvar=var(X)
	valcovar=coVar(X,Y)
	valalpha=alpha(X,Y)
	valbeta=beta(X,Y)
	m2 = LinearRegression()
	m2.fit(X,Y)
	valeur=m2.score(X2,Y2)

	
	print("La valeur RSS est {0},\nvaleur variance {1},\nvaleur covariance {2},\nvaleur alpha {3},\nvaleur beta {4},\nvaleur {5}".format(valrss,valvar,valcovar,valalpha,valbeta,valeur))

main()
