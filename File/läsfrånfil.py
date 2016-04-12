#Läs och skriv till fil
import sys

#Detta skriver till filen
def write():
	filename = input("Ange namnet på din nya fil: ")
	file = open(filename, "w")
	newText = input("Vad vill du skriva till filen?: ")
	file.write(newText)
	file.close()

#Detta läser från samma fil
def read():
	filename = input("Ange namnet på den fil du vill öppna: ")
	file = open(filename)
	print(file.read())

#Main
write()
read()