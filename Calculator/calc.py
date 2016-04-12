#En väldigt enkle miniräknare skrivet i python'
#Denna täcker väldigt basic saker metoder, if-satser, loopar, enkelt matte, samt input och output

#methods
def add(tal1, tal2):
	return tal1 + tal2

def sub(tal1, tal2): #<--- kom ihåg : efter saker
	return tal1 - tal2

def mult(tal1, tal2):
	return tal1 * tal2

def div(tal1, tal2):
	return tal1/tal2

def printMenu():
	print("Welcome to this calculater!\nplease select a option")
	print("1: Add")
	print("2: Substraction")
	print("3: Multiplication")
	print("4: Divide")
	print("5: Exit")


def menu():
	while True:
		printMenu()
		menuChoice = input("Pls select and option: ")
		if menuChoice == "1":
			result = add(int(input("Tal1: ")), int(input("Tal2: ")))
			print(result)

		elif menuChoice == "2":
			result = sub(int(input("Tal1: ")), int(input("Tal2: ")))
			print(result)

		elif menuChoice == "3":
			result = mult(int(input("Tal1: ")), int(input("Tal2: ")))
			print(result)

		elif menuChoice == "4":
			result = div(int(input("Tal1: ")), int(input("Tal2: ")))
			print(result)

		else:
			sys.exit() #kills the script

		#stannar tråden i 5 sek
		time.sleep(5) #för denna behövs import time se överst
		#tömmer terminal fönstret
		os.system('cls') #för denna behöver import os se överst

#start call
menu()