persona = {}

loop = True

while loop:
    clave = input("Dato a introducir: ")
    valor = input(clave + ": ")
    persona[clave]= valor
    print(persona)

    seguir = input("Ingrese 0 si quiere salir, cualquier otra cosa para continuar ingresando datos: ")
    if seguir == "0":
        loop = False