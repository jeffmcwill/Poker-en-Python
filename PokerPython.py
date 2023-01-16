import random
import os
import numpy
import time

#juego de poker codificado en python 3 

#falta agregarle un metodo para ganar y perder, *(ya hecho)que la ia agregue tambien dinero a la partida, *(ya hecho)limite de cantidad de cartas q se puede agregar.
#ya le añadi metodos para ganar y perder, para apostar, para agregar cartas y la ia obtiene tambien cartas y apuesta. 
#faltaria añadirle algun metodo que el dinero del jugador y el crupier se guarde en cada nuevo juego.
#pude corregir el bug para q el juego siga jugandose reiniciandose las cartas de los jugadores pero manteniendole el dinero, lo que si aun no pude hacer que lo apostado
# por los jugadores si pierden, se reste en los demas juegos.
#corrigiendose aun
# el bug del dinero del jugador q no se resta, aun no lo pude corregir.
# se pudo corregir el bug asiendo un pequeño sistema que eliminaba la lista para que deje solamente lo que quedo de la apuesta anterior del jugador
#costo pero se pudo
#ahora solo faltaria que al ganar haga un conteo de la cantidad de partidas ganadas, perdidas y el dinero ganado.
#15/1/23
#resolvido error de numeros erroneos

#ya no se pierde el puntaje, se añaden las apuestas y termina el juego apropiadamente.
#ya termino el juego...
#logre añadirle para que el jugador pierda si se queda sin dinero y tambien si la mesa ya no posee mas dinero, el juego termina.

dinero = [500]
dineroCrupier = [1200]
partida = [0]
partidasGanadas = []
partidasPerdidas = []

def sumaTotal(lista):
	suma = 0
	for elem in lista:
		suma+=elem
	return suma

def poker():

	cartas = [2,3,4,5,6,7,8,9,10,11]

	player = 0
	barajaJugador = []
	barajaCrupier = []
	manos = [1]
	cantCartas = 0
	apuesta = [0]

	repartirJugador = numpy.random.choice(cartas)
	repartirCrupier = numpy.random.choice(cartas)

	barajaJugador.append(repartirJugador)
	barajaCrupier.append(repartirCrupier)

	while True:

		try:
			if sumaTotal(dineroCrupier) > 0:
				
				os.system("cls")
				print("------------------------------------")
				print("Dinero: ",sumaTotal(dinero) - sumaTotal(apuesta),"  | Cartas: ",sumaTotal(manos), "| Partida: ",sumaTotal(partida))
				print("------------------------------------")
				print("/ Crupier /")
				print("-----------------------")
				print("/Sus cartas: ",sumaTotal(manos))
				print("/Su dinero: ",sumaTotal(dineroCrupier) - sumaTotal(apuesta))
				print("-----------------------")

				print("* Pozo: ",sumaTotal(apuesta) + sumaTotal(apuesta))

				print("-----------------------")
				print("/ Jugador /")
				print("-----------------------")
				print("/ Tus cartas:",barajaJugador)
				print("/ Total: ",sumaTotal(barajaJugador))
				print("-------------------------")

				print("1. Tomar otra carta.")
				print("2. Quedarse.")
				print("3. Apostar.")
				print("4. Salir de la partida.")

				print("-------------------------")
				player = int(input("> "))

				if player == 1:

					if sumaTotal(manos) != 5:
						os.system("cls")
						num1 = 1
						otracarta1 = numpy.random.choice(cartas)
						otracarta2 = numpy.random.choice(cartas)

						barajaJugador.append(otracarta1)
						barajaCrupier.append(otracarta2)
						manos.append(num1)

						print("Tomas otra carta...")
						print("El crupier tambien tomo otra carta...")

					else:
						print("Lo lamento ya ambos tienen demasiadas cartas en sus manos.")

				elif player == 2:
					os.system("cls")
					print("Decides quedarte...")

					if sumaTotal(barajaJugador) > sumaTotal(barajaCrupier):
						
						print("++++++++++++++++++++")
						print("¡JUGADOR GANA MANO!")
						print("++++++++++++++++++++")

						ganar = sumaTotal(apuesta) + sumaTotal(dinero)
						perder = sumaTotal(dineroCrupier) - sumaTotal(apuesta)
						partida1 = 1
						puntoGanador = 1

						del dinero[0]
						del dineroCrupier[0]

						partidasGanadas.append(puntoGanador)
						partida.append(partida1)
						dinero.append(ganar)
						dineroCrupier.append(perder)

						if sumaTotal(dinero) > 0:
							time.sleep(2)
							poker()
							break

						if sumaTotal(dineroCrupier) == 0:
							print("Lo lamento, la mesa se quedo sin dinero... MESA CERRADA.")
							print("---------------------------------")
							print("GRACIAS POR JUGAR.")
							print("---------------------------------")
							print("PARTIDAS GANADAS: ",sumaTotal(partidasGanadas))
							print("PARTIDAS PERDIDAS: ",sumaTotal(partidasPerdidas))
							print("---------------------------------")	
							break

					elif sumaTotal(barajaJugador) < sumaTotal(barajaCrupier):

						print("++++++++++++++++++++")
						print("¡CRUPIER GANA MANO!")
						print("++++++++++++++++++++")

						ganar = sumaTotal(apuesta) + sumaTotal(dineroCrupier)
						perder = sumaTotal(dinero) - sumaTotal(apuesta)
						partida1 = 1
						puntoPerdedor = 1

						del dinero[0]
						del dineroCrupier[0]

						partidasPerdidas.append(puntoPerdedor)
						partida.append(partida1)
						dinero.append(perder)
						dineroCrupier.append(ganar)
						
						#corregir error que el jugador no se le quita el dinero apostado. y se lo suma cuando deberia de ser alrevez.

						#system("cls")

						if sumaTotal(dinero) > 0:
							time.sleep(2)
							poker()
							break

						elif sumaTotal(dinero) == 0:
							print("Lo lamento, te quedaste sin dinero... MESA CERRADA.")
							print("---------------------------------")
							print("GRACIAS POR JUGAR.")
							print("---------------------------------")
							print("PARTIDAS GANADAS: ",sumaTotal(partidasGanadas))
							print("PARTIDAS PERDIDAS: ",sumaTotal(partidasPerdidas))
							print("---------------------------------")
							time.sleep(5)
							break

					elif sumaTotal(barajaJugador) == sumaTotal(barajaCrupier):
						print("++++++++++++++++++++")
						print("EMPATE.")
						print("++++++++++++++++++++")
						print("NADIE PIERDE...")
						print("++++++++++++++++++++")
						#dinero.append(apuesta)
						#dineroCrupier.append(apuesta)
						partida1 = 1
						partida.append(partida1)

						time.sleep(2)

						#os.system("cls")
						poker()
						break

				elif player == 3:
					os.system("cls")

					if (sumaTotal(dinero) - sumaTotal(apuesta)) > 0:

						user2 = 0

						while True:
							
							try:
								os.system("cls")
								print("-------------------------")
								print("¿Cuanto quieres apostar?")
								print("Tu dinero: ",sumaTotal(dinero) - sumaTotal(apuesta))
								print("-------------------------")

								user2 = int(input("> "))

								if user2 < sumaTotal(dinero):

									apuestaAhora = sumaTotal(dinero) - user2

									apuesta.append(user2)

									print("cantidad apostada: ",user2)

									print("Ahora tienes: ",apuesta)
									print("El crupier tambien apuesta...")

									break

								elif user2 > sumaTotal(dinero):
									print("Lo lamento, estas poniendo mas dinero del que posees...")
									continue

								elif user2 == sumaTotal(dinero):

									apuestaAhora = sumaTotal(dinero) - user2

									apuesta.append(user2)

									print("cantidad apostada: ",user2)

									print("Ahora tienes: ",apuesta)
									print("El crupier tambien apuesta...")

									break

							except:
								print("ponga solo numeros.")
								continue

					elif (sumaTotal(dinero) - sumaTotal(apuesta)) == 0:
						print("Lo lamento ya no tienes mas dinero para apostar...")

				elif player == 4:
					os.system("cls")
					print("Saliendo de la partida.")
					print("---------------------------------")
					print("GRACIAS POR JUGAR.")
					print("---------------------------------")
					print("PARTIDAS GANADAS: ",sumaTotal(partidasGanadas))
					print("PARTIDAS PERDIDAS: ",sumaTotal(partidasPerdidas))
					print("---------------------------------")
					time.sleep(10)
					break
				
				else:
					print("Numero que ingresaste no esta soportado por ningun comando.")
					continue

			else:
				print("Lo lamento, la mesa se quedo sin dinero")
				print("---------------------------------")
				print("GRACIAS POR JUGAR.")
				print("---------------------------------")
				print("PARTIDAS GANADAS: ",sumaTotal(partidasGanadas))
				print("PARTIDAS PERDIDAS: ",sumaTotal(partidasPerdidas))
				print("---------------------------------")

				time.sleep(10)
				break

		except:
			print("Comando ingresado incorrecto, ingrese el soportado por el programa.")
			continue


def main():

	user = 0

	while True:

		print("""------------------------ 
 _____
|A .  |	/POKER PYTHON/
| /.\ |  
|(_._)| - 1. COMENZAR
|  |  |	- 2. SALIR
|____V|""")
		print("------------------------")

		user = int(input("> "))

		if user == 1:
			os.system("cls")
			print("Ok, empezemos con el juego.")
			time.sleep(1)
			poker()
			break

		elif user == 2:
			os.system("cls")
			print("Saliendo del juego...")
			break
			
if __name__ == "__main__":
	main()
	#poker()