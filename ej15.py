"""
Ejercicio 2

El Rayo MCQueen se va de vacaciones, y quiere aprovechar el viaje para pasar por una
determinada ciudad. Por eso necesita analizar todos los caminos que pasan por ella.

Se tiene un archivo que recibe en su primera línea el código de una ciudad por la cual
quiere pasar el Rayo. Las líneas restantes son sus rutas de viajes.

Se pide

Generar un archivo de salida con la cantidad de caminos que pasan por la ciudad que 
quiere el Rayo.

Aclaraciones

	* se dice que un camino pasa por la ciudad que quiere el rayo si:
		* La ciudad está presente en el camino
		* La ciudad no es el origen ni el destino del camino
	* Las ciudades pueden ser de más o menos de 3 caracteres de largo, el ejemplo es solo
	  ilustrativo.

Ejemplo

	viajes.txt
	
	DDD
	AAA->BBB->CCC
	AAA->DDD->CCC
	AAA->DDD
	BBB->EEE
	DDD->CCC->FFF
	BBB->CCC->FFF
	AAA->DDD->FFF
	AAA->DDD->GGG
	AAA->DDD->CCC->FFF
	DDD->FFF

	Se obtiene
	
	salida.txt
	
	4
"""

def calcular_rutas(file):
	rutas, ciudad = 0, file.readline().rstrip()
	for line in file:
		camino = line.rstrip().split("->")
		for i in range(len(camino)):
			if i != 0 and i != len(camino) -1 and camino[i] == ciudad:
				rutas += 1
	return rutas

def main():
	try:
		with open("archivos/De_Entrada/viajes.txt", "r", encoding="utf8") as file:
			rutas = calcular_rutas(file)
			print(str(rutas))
		with open("archivos/De_Salida/salida.txt", "w", encoding="utf8") as file:
			file.write(str(rutas))
	except FileNotFoundError:
		print("El archivo viajes.txt no existe o no es legible")
  
main()