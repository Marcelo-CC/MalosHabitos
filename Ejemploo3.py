# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(anchura, longitud):
    area = anchura * longitud
    return area

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

# Función principal
if __name__ == "__main__":
    anchura = float(input("Introduce la anchura del rectángulo: "))
    longitud = float(input("Introduce la longitud del rectángulo: "))
    area_rectangulo = calcular_area_rectangulo(anchura, longitud)
    print(f"Área del rectángulo ({anchura} * {longitud}): {area_rectangulo}")

    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    area_triangulo = calcular_area_triangulo(base, altura)
    print(f"Área del triángulo (0.5 * {base} * {altura}): {area_triangulo}")

