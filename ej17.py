def desencriptando(line):
    valores = int(line.rstrip().split(";")[0]) -1
    palabra = list(line.rstrip().split(";")[1])
    if valores == -1:
        resultado = " "
    elif valores > -1:
        resultado = palabra[valores]
    else:
        resultado = ''
    return resultado

def main():
    contrasenia = []
    try:
        with open("archivos/De_Entrada/palabras.csv", "r", encoding="utf8") as file:
            for line in file:
                contrasenia.append(desencriptando(line))
        with open("archivos/De_Salida/contraseña.txt", "w", encoding="utf8") as file:
            for i in range(len(contrasenia)):
                file.write(contrasenia[i])
    except FileNotFoundError:
        print("El archivo no palabras.csv no existe")
main()