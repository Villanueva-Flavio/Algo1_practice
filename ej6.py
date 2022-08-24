"""
  Ejercicio 3 de Final 1 1C2022 Algo1 Camejo

  NO ARREGLADO

	Anita y Rogers e mudaron al interior y consiguieron una hermosa casa con un parque
	enorrrrrme donde los 101 dálmatas pueden ser felices y correr en libertad

	Se tiene un archivo de coordenadas llamado coordenadas.csv donde está cada una de las posiciones de los dálmatas en el parque.

	Se pide
		1. Generar un archivo distancias.txt que contenga la información de los 2 dálmatas que
		   están mas cerca entre ellos y de los 2 dálmatas que esten más alejados
	
	Ejemplo
		Aclaracion: las coordenadas pueden ser números con coma.
	
	coordenadas.csv

		5;8
		6.5;15
		2;2
		0;0
		45;20
	
	distancias.txt

		Más cerca: (0;0) - (2;2)
		Más alejados: (0;0) - (45;20)
"""
import math

def distancia_entre(x1, y1, x2, y2):
	a, b = [float(x1), float(y1)], [float(x2), float(y2)]
	return math.dist(a, b)

def obtener_coordenadas(x, y, distantes):
	a, b, c, d = 0, 0, 0, 0
	distancia = 0 if distantes == True else 1000000
	for i in range(len(x)):
		for k in range(len(x)):
			if i != k:
				if distancia < distancia_entre(x[i], y[i], x[k], y[k]) and distantes == True:
					a, b, c, d = x[i], y[i], x[k], y[k]
					distancia = distancia_entre(x[i], y[i], x[k], y[k])
				elif distancia > distancia_entre(x[i], y[i], x[k], y[k]) and distantes == False:
					a, b, c, d = x[k], y[k], x[i], y[i]
					distancia = distancia_entre(x[i], y[i], x[k], y[k])
	return [a, b, c, d]

def main():
	x, y = [], []
	with open("archivos/De_Entrada/coordenadas.csv", "r", encoding="utf8") as file:
		for line in file:
			x.append(line.rstrip().split(";")[0])
			y.append(line.rstrip().split(";")[1])		
		mas_distantes = obtener_coordenadas(x, y, True)
		mas_cercanos = obtener_coordenadas(x, y, False)
	with open("archivos/De_Salida/distancias.txt", "w", encoding="utf8") as file:
		file.write("Más cerca: (" + mas_cercanos[0] + ";" + mas_cercanos[1] + ") - (" + mas_cercanos[2] + ";" + mas_cercanos[3] + ")\n")
		file.write("Más alejados: (" + mas_distantes[0] + ";" + mas_distantes[1] + ") - (" + mas_distantes[2] + ";" + mas_distantes[3] + ")")

main()

"""TERMINADO"""