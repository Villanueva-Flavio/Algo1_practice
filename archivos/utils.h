#ifndef __UTILS_H__
#define __UTILS_H__

#define MAX_BUFFER 10000
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>

#define MAX_COLORES 50
#define MAX_INDICES 100
#define MAX_BUFFER 10000
#define METODO_UNO "fscanf"
#define METODO_DOS "fgets"
#define MAX_LINES 100
/*
* Funcion que recibe un archivo de lectura y verifica que este disponible
*
* Function that receives a read-only file and it checks if its available
*/
bool isReadable(FILE *leer_archivo){
    bool resultado;
    char buffer_in[MAX_BUFFER], *ptr;
    if(leer_archivo!=NULL){            // Existe el archivo?
        fgets(buffer_in, MAX_BUFFER, leer_archivo); // Cargo un buffer
        if(buffer_in != NULL){
            resultado = true; // Existen datos?
        } else {
            resultado = false;
            printf("Pista.csv esta vacio\n");
        }
    } else {
        resultado = false;
		printf("Pista.csv no existe\n");
    }
    return resultado;
}

/*
* Funcion que busca si existe un numero en un vector
*
* Function that looks if a number matches in the array
*/
bool buscar_valor(int indices[MAX_INDICES], int tope, int i){
    bool resultado = false;
    for(int j = 0; j < tope; j++){
        if(indices[j] == i){
            resultado = true;
        }
    }
    return resultado;
}

#endif