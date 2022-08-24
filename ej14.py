"""
Ejercicio 1

Roger y Anita andan cortos de plata, por lo que quieren anotar a algunos dálmatas al
concurso de piruetas. Como la inscripción por cada perro tiene un costo, primero los
entrenarán para luego filtrarlos y anotar solamente a aquellso candidatos qu den
esperanzas de ganar el gran premio

Dado un archivo donde cada linea representa las 10 piruetas quehizo cada perrito dálmata
en el entrenamiento.

Se pide

Generar un archivo de salida con:

	* ID del dálmata
	* Cantidad total de vueltas válidas en sentido horario
	* Cantidad total de vueltas válidas en sentido antihorario

El archivo de salida debe contener los datos de aquellos dálmatas que cumplan todas las
siguientes condiciones:

	* Por lo menos dieron 3 vueltas válidas en sentido horario
	* Por lo menos dieron 2 vueltas válidas en sentido antihorario
	* Su pirueta final sea una vuelta válida "perfecta".

Aclaraciones
	
	* Cada pirueta está representada por el sentido y los grados del giro
	* Los grados que gira cada perrito están entre 100 y 400
	* Una vuelta válida es una pirueta de 360 +/- 15 grados
	* Una vuelta válida "perfecta" es una pirueta de 360 +/- 2 grados
	* Los datos pedidos en el archivo de salida deben estar separados por ';'
	* El número de línea en el archivo de entrada representa el id del dálmata, por ejemplo la
	  primer línea representa las vueltas del dálmata 1
	* El archivo de salida debe estar ordenado por ID del dálmata

Ejemplo
	
	piruetas.csv
		A343;A340;A342;H360;H361;A360;H376;H370;H377;A358
		H363;H363;H363;H363;H363;A363;A363;A363;A363;A363
		H360;H360;H360;H360;H360;H360;H360;H360;H360;H360
		A360;A361;A362;A358;A340;H340;H350;H354;H358;H360
		A344;A376;A344;H376;A344;A376;H344;H344;A376;H361

	Se obtiene

	candidatos.csv
		1;3;2
		4;4;4
"""

def clasificacion_salto(angulo, rango):
    return True if abs(angulo - 360) <= rango else False
        
def appendear_datos(line_h, saltos_h, line_a, saltos_a, line_id, id):
	line_h.append(saltos_h)
	line_a.append(saltos_a)
	line_id.append(id)  

def obtener_datos(file, line_a, line_h, line_id):
	rango_v, rango_p = 15, 2
	id = 0
	for line in file:
		id += 1
		pir_a, pir_h, line = 0, 0, line.rstrip().split(";")
		for i in range(len(line)):
			element = line[i]
			sentido, angulo = element[0], int(element[1:])
			if clasificacion_salto(angulo, rango_v) == True:
				pir_h += 1 if sentido == "H" else False
				pir_a += 1 if sentido == "A" else False
			appendear_datos(line_h, pir_h, line_a, pir_a, line_id, id) if clasificacion_salto(angulo, rango_p) == True and pir_h >= 3 and pir_a >= 2 and i == len(line)-1 else False
					

def main():
	linea_saltos_h, linea_saltos_a, linea_id = [], [], []
	try:
		with open ('archivos/De_Entrada/piruetas.csv', 'r', encoding='utf8') as file:
			obtener_datos(file, linea_saltos_a, linea_saltos_h, linea_id)
		with open ('archivos/De_Salida/candidatos.csv', 'w', encoding='utf8') as file:
			for i in range (len(linea_id)):
				file.write(str(linea_id[i]) + ';' + str(linea_saltos_h[i]) + ';' + str(linea_saltos_a[i]))
				if i != len(linea_id) -1:
					file.write("\n")
	except FileNotFoundError:
		print("El archivo piruetas.csv no se puede abrir o es ilegible")

main()

"""TERMINADO"""