#!/usr/bin/python3
#-*-coding:Utf-8 -*

import math						#Importe le module "math"
from random import randrange				#Importe la fonction "randrange"
from math import ceil					#Importe la fonction "ceil"

cash = 500						#Somme dépensable au départ.
print("Vous venez au casino avec :", cash,"$")

num = input("Saisissez le numéro d'une case (compris entre 0 et 49) :")
num = int(num)

bet = input("Saisissez le montant de votre mise :")
bet = int(bet)

result = randrange(50)					#Simulation d'un hasard dans l'intervalle 0 à 49.
print("Le numéro gagnant est :", result)

while cash > 0:						#Tant que la somme dépensable est supérieure à 0.
	if num == result:				#En cas d'égalité entre le numéro choisit(num) et le numéro gagnant(result).
		cash += bet * 3
		print("Vous remportez", bet * 3,"$ !")
	elif num != result and num % 2 == result % 2:	#Numéros différents mais couleur identique.
		bet = ceil(bet * 0.5)
		print("Vous récupérez la moitié de votre mise :", bet,"$.")
		cash += bet
	else:						#Numéros et couleurs différentes.
		print("Vous perdez votre mise.")
		cash -= bet

	if cash <= 0:					#Comportement quand le portefeuille est vide.
     		print("Vous n'avez plus d'argent.")
	else:
            	print("Il vous reste :", cash,"$.")
