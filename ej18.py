def main():
    vuelta, recorrido = 360, 0
    mano, contramano = "M", "C"
    try:
        with open("tramos.csv", "r", encoding="utf8") as file:
            for line in file:
                sentido = line.rstrip().split(";")[0]
                grados = int(line.rstrip().split(";")[1])
                if sentido == mano:
                    recorrido += grados
                else:
                    recorrido -= grados
            vueltas_hechas =  recorrido//vuelta
            if recorrido % vuelta != 0 and recorrido < 0:
                vueltas_hechas += 1
            print (vueltas_hechas)
        with open("salida.txt", "w", encoding="utf8") as file:
            file.write(str(vueltas_hechas) + " vuelta")
            if vueltas_hechas != 1 and vueltas_hechas != -1:
                file.write("s")
    except FileNotFoundError:
        print("El archivo tramos.csv no existe")

main()