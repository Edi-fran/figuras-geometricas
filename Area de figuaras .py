def area_perimetro_circulo(radio):
    pi = 3.1416
    area = pi * radio ** 2
    perimetro = 2 * pi * radio
    return area, perimetro

def area_perimetro_rectangulo(ancho, largo):
    area = ancho * largo
    perimetro = 2 * (ancho + largo)
    return area, perimetro

def area_perimetro_triangulo(base, altura):
    area = (base * altura) / 2
    perimetro = None
    return area, perimetro

def mostrar_menu():
    print("Menú de selección de figuras geométricas:")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Salir")

def calcular_figura(opcion):
    if opcion == 1:
        radio = float(input("Ingrese el radio del círculo: "))
        area, perimetro = area_perimetro_circulo(radio)
    elif opcion == 2:
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        largo = float(input("Ingrese el largo del rectángulo: "))
        area, perimetro = area_perimetro_rectangulo(ancho, largo)
    elif opcion == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area, perimetro = area_perimetro_triangulo(base, altura)
    else:
        print("Opción no válida.")
        return

    print(f"Área: {area}")
    if perimetro is not None:
        print(f"Perímetro: {perimetro}")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 4:
            print("Saliendo del programa.")
            break
        calcular_figura(opcion)
