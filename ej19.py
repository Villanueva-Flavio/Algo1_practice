def descansable(datos):
    inicio, final, principe = "I", "F", "principe"
    resultado = False
    for i in range(len(datos)):
        if datos[i] == inicio or datos[i] == final or datos[i] == principe:
            resultado = True
    return resultado

def main():
    inicio, final = "I", "F"
    horas, minutos, minutos_descansados = 0, 0, 0
    arranca = False
    try:
        with open("archivos/De_Entrada/sueños.csv", "r", encoding="utf8") as file:
            for line in file:
                datos = line.rstrip().split(";")
                if datos[0] == inicio:
                    arranca = True
                if descansable(datos) and arranca == True:
                    minutos_descansados += int(datos[1])
                if datos[0] == final:
                    arranca = False
            horas = minutos_descansados//60
            minutos = minutos_descansados%60
        with open("archivos/De_Salida/salida.txt", "w", encoding="utf8") as file:
            file.write(str(horas) + "h" + str(minutos) + "m")
    except FileNotFoundError:
        print("El archivo sueños.csv no existe")
        
main()