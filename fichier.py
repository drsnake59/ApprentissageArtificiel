#!/usr/bin/python3
import pandas
import matplotlib.pyplot as plt

def somme(a, b):
	return a + b
	
# parcourt d'une liste
def fun():
	for i in [1, 2, 3, 4, 5]:
		print(i) # affichage de la variable i
	for j in [1, 2, 3, 4, 5]:
		print(j)
		print(i+j)
	print("Fin de bloc")

def fun2():
	chaine1 = 'une chaine'
	chaine2 = "une autre chaine"
	taille = len(chaine1)
	print("La chaine 1 est {0} et a une taille de {1} la chaine 2 est {2}".format(chaine1,taille,chaine2))
	chaine3 = chaine1 + chaine2
	print("La chaine 3 est {}".format(chaine3))
	bjr = 'bonjour'
	print(bjr[1]) # affiche o
	print(bjr[0:2]) # affiche bo
	print(bjr[:2]) # affiche bo
	print(bjr[2:]) # affiche njour

def fun3():
	chaine1 = 'une chaine'
	chaine2 = "une autre chaine"
	taille = len(chaine1)
	print("La chaine 1 est {0} et a une taille de {1} la chaine 2 est {2}".format(chaine1,taille,chaine2))
	chaine3 = chaine1 + chaine2
	print("La chaine 3 est {}".format(chaine3))
	bjr = 'bonjour'
	print(bjr[1]) # affiche o
	print(bjr[0:2]) # affiche bo
	print(bjr[:2]) # affiche bo
	print(bjr[2:]) # affiche njour

def fun4():
	li = [] # Déclare une liste vide
	li.append(1) # li est maintenant [1]
	li.append("bonjour") # li est maintenant [1,'bonjour'] (liste hétérogène)
	autre_li = [1,2,3,4,5]
	liste_de_liste = [ li, autre_li ] # [[1, 'bonjour'], [1, 2, 3, 4, 5]]
	autre_li[2:4] # [3,4]
	del autre_li[3] # suppression du 3ieme élément
	autre_li[2:4] # [3, 5]
	autre_li[-1] # 5 (dernier élément)
	autre_li[-2] # 3 (avant dernier élément)
	len(li) # taille d'une liste
	li.extend(autre_li)
	

def square_and_cube(x):
	return(x*x,x*x*x)

def fun5():	
	d = dict() # Déclare un dictionnaire vide
	nombres = { "un" : 0, "deux" : 2, "dix" : 10 }
	nombres["un"] = 1 # remplace la valeur
	nombres["cinq"] = 5 # ajoute l'entrée
	nombres.get("deux") # 2
	nombres.keys() # liste de toutes les clés
	nombres.values() # liste de toutes les valeurs
	nombres.items() # liste de tuples des pairs clés/valeurs
	for k,v in nombres.items():
		print("La valeur de la clé {} est {}".format(k,v))

#print(somme(2,3))
#print(fun())
#print (fun2())
#print(fun4()) pas d'affichage
def main():
	a,b = square_and_cube(3) # a=9, b=27
	_,c = square_and_cube(2) # c=8
	print(a,b,c)
	print(fun5())

main()
