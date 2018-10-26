#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import random
from math import *
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
"""
def ptsAlea():
	li=[]
	bruit=bruit()
	for i in range (-3,11):
		if i==0:
			li.append(0+bruit[i])
			continue
		li.append((10*sin(i)/i)+bruit[i])
	return li
##
def bruit():
	bruit=np.random.normal(0,1,15)
	print(bruit)
	return bruit
"""
def tableau():
	np.random.seed(1337)
	x=[np.random.uniform(-3,10) for x in range(15)]
	x=np.sort(x)
	y=10*np.sin(x)/x + np.random.normal(0,1,15)
	return [x,y]

def model():
	model=make_pipeline(PolynomialFeatures(deg),Ridge())#au degre deg
	return model

def affichagePoint(tab):
	plt.scatter(tab[0],tab[1])
	plt.show()

def main():
	tab=tableau()
	tab[0]=tab[0].reshape(-1,1)
	model=make_pipeline(PolynomialFeatures(1),Ridge())
	model.fit(tab[0],tab[1])
	affichagePoint(tab)
	
	#affichage(tab)
	#model=model()
main()
