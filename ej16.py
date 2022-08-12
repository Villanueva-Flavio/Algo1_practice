"""
Ejercicio 3

WALL-E adoptó un babyrobot y en el baby shower muchos de sus baby amigos le
regalaron baby insumos para el baby cuidado del mismo. Como cada baby insumo es
especial para cada baby modelo necesita organizarse pero, como su baby memoria es
corta, solamente puede retener baby informacion de 3 baby insumos a organizar.

Dado un archivo donde:
	
	* La primera línea contiene el modelo del baby robot de WALL-E
	* La segunda línea contiene el listado de los 3 insumos que quiere organizar separados por ';'.
	* La tercera línea en adelante contienen insumos que recibió como regalo, en el formato
	  "modelo baby robot: insumo".

Se pide

Generar un archivo de salida donde cada línea sea un insumo que quiere organizar junto a
la cantidad que le regalaron, con el formato "insumo : cantidad".

Aclaraciones

	* El orden de los insumos a organizar debe ser el mismo en el que aparecen en la 
	segunda línea del archivo de entrada.

Ejemplo
	
	apunte.csv

	BabyBot2A
	aceite recien nacido;pañales aluminio premium;chupete acero quirurgico
	AD12 : aceite recien nacido
	BabyBot2A : pañales aluminio premium
	BBotS : pañales aluminio premium
	BabyBot2A : pañales aluminio premium
	BabyBot2A : toallitas lubricantes
	BabyBot2A : aceite recien nacido
	AD12 : chupete acero quirurgico

	Se obtiene
	salida.txt

	aceite recien nacido : 1
	pañales lauminio premium : 2
	chupete acero quirurgico : 0
"""

def get_Bot(file):
    return file.readline().rstrip()

def get_Insumos(file):
    return file.readline().rstrip().split(';')

def obtener_datos(line, bot, insumos, cantidad):
	line = line.rstrip().split(' : ')
	if line[0] == bot and line[1] in insumos:
		cantidad[insumos.index(line[1])] += 1

def guardar_datos(file, insumos, cantidad):
	for i in range(len(insumos)):
		file.write(str(insumos[i]) + ' : ' + str(cantidad[i]))
		file.write('\n') if i != len(insumos) -1 else 0

def main():
	try:
		with open ('archivos/apunte.csv', 'r', encoding='utf8') as file:
			bot, insumos = get_Bot(file), get_Insumos(file)
			cantidad = [0 for elemento in insumos]
			for line in file:
				obtener_datos(line, bot, insumos, cantidad)
		with open ('archivos/salida.txt', 'w', encoding='utf8') as file:
				guardar_datos(file, insumos, cantidad)
	except FileNotFoundError():
		print("IO Error, el archivo: 'apunte.csv' no existe o no es legible")
        
main()

"""TERMINADO"""