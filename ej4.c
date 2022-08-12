/*
  Ejercicio 1 de Final 1 1C2022 Algo1 Camejo

  NO ARREGLADO

    Oh no! Russell y Carl tienen peso de más en la casa de Up y se estan cayendo! Te animás a
    ayudarlos a encontrar los globos con más presión para que puedan inflarlos un poco más, y
    puedan elevarse?

    Se tiene un archivo presiones.csv donde se encuentra el color de cada globo, seguido de la presión del mismo.

    Se pide

    1. Obtener todos los globos que tengan la presión mínima, y escribirla en un archivo nuevo, globos_a_inflar.csv

    Ejemplo
    Recibiendo el archivo:

    presiones.csv

    rojo;21
    negro;12
    verde;20
    rosa;12
    violeta;17

    Se obtiene:
    globos_a_inflar.csv

    negro;12
    rosa;12

    Aclaración: El ejercicio fue realizado con fines prácticos de programación, No aceptamos quejas sobre química.
*/

#include "./archivos/utils.h"

void conseguir_indices_m1(FILE* leer_archivo, int indices, int *tope_indices){
    int presion, presiones[MAX_INDICES];
    char color[MAX_COLORES];
    
    fscanf(leer_archivo, "%s;%i", color, presiones);
    
}

/*
* Procedimiento que consigue los indices de todos los globos a inflar y los guarda en un vector
*
* Process that get the index of all the balloons to fill and it saves into an array
*/
void conseguir_indices(FILE *leer_archivo, int indices[MAX_INDICES], int *tope_indices){
    char buffer[MAX_BUFFER], *ptr;
    int i = 0, presion[MAX_INDICES];
    while(!feof(leer_archivo)){
        fgets(buffer, MAX_BUFFER, leer_archivo);
        while(ptr != NULL){
            ptr = strtok(buffer, ";");
            ptr = strtok(NULL, "\n");
            presion[i] = atoi(ptr);
            i++;
        }
    }
}

void guardar_indices(FILE *leer_archivo, FILE *escribir_archivo, int indices[MAX_INDICES], int tope){
    int i, presion;
    char buffer_in[MAX_BUFFER], *ptr, buffer_out[MAX_BUFFER];
    for(i = 0; i < tope; i++){
        fgets(buffer_in, MAX_BUFFER, leer_archivo);
        if(buscar_valor(indices, tope, i)){
            ptr = strtok(buffer_in, ";");
            sprintf("%s", ptr);
            ptr = strtok(buffer_in, "\n");
            presion = atoi(ptr);
            fprintf(escribir_archivo, "%s;%i\n", buffer_out, presion);
        }
    }
}


int main(){
    FILE *leer_archivo = fopen("./archivos/presiones.csv", "r");
    FILE *escribir_archivo = fopen("./archivos/globos_a_inflar.csv", "w");
    int indices[MAX_INDICES], tope_indices;
    if(leer_archivo!=NULL){
        conseguir_indices(leer_archivo, indices, &tope_indices)
        guardar_indices(leer_archivo, escribir_archivo, indices, tope_indices);
    }
    fclose(leer_archivo);
    fclose(escribir_archivo);
    return 0;
}

//TERMINADO