/* 
  Ejercicio 2 de Final 1 1C2022 Algo1 Camejo

  NO ARREGLADO

    Por fin encontramos el tesorod espués de tanta búsqueda, finalmente vamos a abrirlo yyyy...
    "Por favor ingrese la contraseña.". Estamos perdidos!
    Nos dimos cuenta que atrás del mapa hay unas pistas... a ver que dice:
        
        Si el tesoro es lo que quieres,
        una contraseña es lo que tienes,
        en una matriz dentro de un archivo,
        con un cálculo muy intensivo.
    
    Se tiene un archivo pistas.csv donde la primer linea nos dice la dimensión de la matriz (se sabe
    que es cuadrada por lo que sólo será un número), seguida de una matriz de enteros:

    Se pide
        1. Obtener los datos de la matriz, y luego escribir en otro archivo contrasenia.txt, el vector
            resultante de la resta de la diagonal principal de la matriz, con la diagonal inversa.

    Ejemplo
        pista.csv

        3
        5;8;9
        3;6;3
        2;1;4
    
    Con la matriz del ejemplo, 3 es la dimensión de la matriz, (5, 6, 4) es la diagonal principal y
    (9, 6, 2) la diagonal inversa. El 5 debería restarse con el 9, el 6 con el 6 (ambos son el centro), y
    el 4 con el 2, dando así, el vector resultante: (-4, 0, 2)

        contrasenia.txt

        (-4;0;2)
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include "archivos/utils.h"

#define MAX_SIZE 100
#define MAX_BUFFER 10000

void cargar_datos(FILE* leer_archivo, int matriz[MAX_SIZE][MAX_SIZE], int* tope){
	int i, k;
	fscanf(leer_archivo, "%i\n", tope);
	for(i = 0; i < *tope; i++){
		for (k = 0; k < *tope; k++){
			fscanf(leer_archivo, "%i;", &matriz[i][k]);
		}
		fscanf(leer_archivo, "[^\n]");
	}
} 

void desencriptar(int matriz[MAX_SIZE][MAX_SIZE], int contrasenia[MAX_SIZE], int tope){
	for(int i = 0; i < tope; i++){
		contrasenia[i] = matriz[i][i] - matriz[i][tope-1-i];
	}
}

void enviar_contrasenia(FILE* escribir_archvo, int contrasenia[MAX_SIZE], int tope){
	fprintf(escribir_archvo, "(");
	for(int i = 0; i < tope; i++){
		fprintf(escribir_archvo, "%i", contrasenia[i]);
		if(i != tope-1){
			fprintf(escribir_archvo, ";");
		} else {
			fprintf(escribir_archvo, ")");
		}
	}
}

int main(){
	FILE *leer_archivo = fopen("archivos/pista.csv", "r");
	FILE *escribir_archivo = fopen("archivos/contrasenia.txt", "w");
	int matriz[MAX_SIZE][MAX_SIZE], contrasenia[MAX_SIZE], tope;
	if(isReadable(leer_archivo)){
		fclose(leer_archivo);
		leer_archivo = fopen("archivos/pista.csv", "r");
		cargar_datos(leer_archivo, matriz, &tope);
		desencriptar(matriz, contrasenia, tope);
		enviar_contrasenia(escribir_archivo, contrasenia, tope);
	}
	fclose(escribir_archivo);
	fclose(leer_archivo);
	return 0;
}

//TERMINADO