from math import *
import os
import platform
import inquirer
import random
import time

if platform.system() == "Windows":
    def clear():
        os.system("cls")
if platform.system() == 'Linux':
    def clear():
        os.system("clear")

def update_print(positions):
	print(f"""
		   A   B   C
		  -----------
		1| {positions[0]} | {positions[1]} | {positions[2]}  
		 |---+---+---
		2| {positions[3]} | {positions[4]} | {positions[5]}  
		 |---+---+---
		3| {positions[6]} | {positions[7]} | {positions[8]} 
	""")

def user_choice(positions, using):
	while True:
		reponse = input(f"Vous avez les {using}, ou voulez vous placez votre {using} [>] ")
		for i in range(len(positions)):
			match i:
				case 0:
					if reponse.lower() == "a1":
						positions[i] = using
						clear()
						update_print(positions)
						return positions
				case 1:
					if reponse.lower() == "b1":
						positions[i] = using
						clear()
						update_print(positions)
						return positions
				case 2:
					if reponse.lower() == "c1":
						positions[i] = using
						clear()
						update_print(positions)
						return positions
				case 3:
					if reponse.lower() == "a2":
						positions[i] = using
						clear()
						update_print(positions)
						return positions
				case 4:
					if reponse.lower() == "b2":
						positions[i] = using
						clear()
						update_print(positions)
						return positions
				case 5:
					if reponse.lower() == "c2":
						positions[i] = using
						clear()
						update_print(positions)
						return positions
				case 6:
					if reponse.lower() == "a3":
						positions[i] = using
						clear()
						update_print(positions)
						return positions
				case 7:
					if reponse.lower() == "b3":
						positions[i] = using
						clear()
						update_print(positions)
						return positions
				case 8:
					if reponse.lower() == "c3":
						positions[i] = using
						clear()
						update_print(positions)
						return positions
				case _:
					pass

def python_choice(positions, using):
	positions_pasChoisies = [i for i, position in enumerate(positions) if position == " "]
	choix = random.choice(positions_pasChoisies)
	if using == "0":
		positions[choix] = "X"
	else:
		positions[choix] = "0"
	clear()
	update_print(positions)
	return positions

def verifie_victoire(positions, using):
	gagnantes = [
	    [0, 1, 2],
	    [3, 4, 5],
	    [6, 7, 8],
	    [0, 3, 6],
	    [1, 4, 7],
	    [2, 5, 8],
	    [0, 4, 8],
	    [2, 4, 6],
	]
	if using == "0":
		bot = "X"
	else:
		bot="0"
	for combinaison in gagnantes:
		if positions[combinaison[0]] == positions[combinaison[1]] == positions[combinaison[2]] == using:
			return "moi"
		if positions[combinaison[0]] == positions[combinaison[1]] == positions[combinaison[2]] == bot:
			return "bot"
	return False

def attendre(time):
	count = 0
	while count == time:
		time.sleep(1)
		print(f"veuillez attendre {count}s")
		count += 1


def morpion():
	positions = [" "," "," "," "," "," "," "," "," "]
	update_print(positions)
	nombre = random.randint(1, 2)
	loose = False
	if nombre == 1:
		using = "0"
		Haszero = True
	else:
		using = "X"
		Haszero = False
	game = 1
	while not loose and game <= 5:
		print(f"vous êtes a la manche {game}")
		positions = user_choice(positions, using)
		if game < 5:
			positions = python_choice(positions, using)
		isloosing = verifie_victoire(positions,using)
		if isloosing == False:
			pass
		if isloosing == "bot":
			loose = True
		if isloosing == "moi":
			loose = True
		game += 1

	if isloosing == "bot":
		attendre(5)
		input("Vous avez perdu contre le bot! apuyer sur n'import quel touche pour continuer")
		main()
	if isloosing == "moi":
		attendre(5)
		input("Vous avez gagner! apuyer sur n'import quel touche pour continuer")
		main()
	else:
		attendre(5)
		input("Egalité! apuyer sur n'import quel touche pour continuer")
		main()






def main():
	clear()
	print("""
███╗   ███╗ ██████╗ ██████╗ ██████╗ ██╗ ██████╗ ███╗   ██╗
████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██║██╔═══██╗████╗  ██║
██╔████╔██║██║   ██║██████╔╝██████╔╝██║██║   ██║██╔██╗ ██║
██║╚██╔╝██║██║   ██║██╔══██╗██╔═══╝ ██║██║   ██║██║╚██╗██║
██║ ╚═╝ ██║╚██████╔╝██║  ██║██║     ██║╚██████╔╝██║ ╚████║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
		""")

	questions = [
        inquirer.List('share',
			message="Que voulais faire ? ",
            choices=['Play', 'Quit'],
        ),
    ]
	answers = inquirer.prompt(questions)['share']
	if answers == "Quit":
		quit()
	if answers == "Play":
		clear()
		morpion()

main()