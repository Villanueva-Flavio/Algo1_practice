"""
  Ejercicio 1 de Final 2 1C2022 Algo1 Camejo

    NO ARREGLADO

    El gerente de la casa de Mickey Mouse organizó un torneito de metegol

    El torneo consiste en jugar todos contra todos y el ganador del torneo tendrá 2 dáis libres en
    estas vacaciones de invierno para poder descansar de los niños.

    El ganador de un partido se lleva 3 puntos, el perdedor se lleva 0 puntos y en caso de empate,
    cada uno se lleva 1 punto

    Se sabe que no son mas de 20 competidores

    Se pide
        1. Obtener el ganador del torneo, escribirlo en un archivo nuevo, recibido como argumento.

    Aclaraciones
        * Tomar que siempre va a haber un ganador definido. Es decir, no considerar casos:
            - Empate entre posibles ganadores
            - Archivo vacío

    Ejemplo

        Recibiendo el archivo:
            partidos.csv

                MKY 3 - 0 PLT
                DNL 1 - 2 MNY
                PLT 1 - 0 MNY
                MKY 2 - 2 DNL
                MNY 1 - 1 MKY
                DNL 0 - 4 PLT
        Se obtiene:
            ganador.txt

                PLT

"""

def main():
    jugadores, victorias = ["MKY", "PLT", "DNL", "MNY"], [0, 0, 0, 0]
    try:
        with open("archivos/partidos.csv", "r", encoding="utf8") as file:
            for line in file:
                partido = line.rstrip().split(" - ")
                score1 = partido[0].split(" ")[1]
                personaje1 = partido[0].split(" ")[0]
                score2 = partido[1].split(" ")[0]
                personaje2 = partido[1].split(" ")[1]
                if score1 > score2:
                    victorias[jugadores.index(personaje1)] += 1
                elif score2 > score1 :
                    victorias[jugadores.index(personaje2)] += 1
        with open("archivos/ganador.txt", "w", encoding="utf8") as file:
            file.write(str(jugadores[victorias.index(max(victorias))]))
    except FileNotFoundError:
        print("El archivo partidos.csv no existe o es ilegible")
main()