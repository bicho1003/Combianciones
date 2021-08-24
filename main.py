import os
import functions as fun


 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Experimento Simple")
	print ("\t2 - Experimento compuesto")
	print ("\t9 - salir")
 
 
while True:
	totalRes = 0
	numComp = 0
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		numComp = int(input("Cuantos experimentos simples tiene el experimento compuesto: "))
		fun.combinaciones(numComp)
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")