def calcular(multipicando, multiplicador, suma):
    resultado = multipicando * multiplicador + suma
    return resultado

if __name__ == "__main__":
    multiplicando = float(input("Introduce el valor del multiplicando: "))
    multiplicador = float(input("Introduce el valor de multiplicador: "))
    suma = float(input("Introduce el valor de suma: "))
    resultado = calcular(multiplicando, multiplicador, suma)
    print(f"El resultado de {multiplicando} * {multiplicador} + {suma} es: {resultado}")


