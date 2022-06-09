class Alumno():
    def __init__(self, nombre, dni, hermanos = 0) -> None:
        self.nombre = nombre
        self.dni = dni
        self.legajo = self.generar_legajo()
        self.hermanos = hermanos
        self.materias = []

    def generar_legajo(self) -> str:
        strDni = str(self.dni)
        legajo = "ALU_" + strDni[:3]
        return legajo
    
    def completar_materias(self):
        cantidad = int(input("Escriba el número de materias a ingresar: "))
        while cantidad <= 0:
            cantidad = int(input("Error, debe haber al menos una materia:"))
        
        for x in range(cantidad):
            materia = input("Ingrese el nombre de la materia " + str(x + 1) + " : ")
            self.materias.append(materia)
    
    def registrar_notas(self):
        aprobadas = []
        for materia in self.materias:
            nota =  int(input("Ingrese la nota de " + materia + " : "))
            while nota < 0 or nota > 10:
                nota =  int(input("Error, ingrese nuevamente, la nota debe ser un número entre 1 y 10: "))
            
            if nota >= 6:
                aprobadas.append(materia)

        for materia in aprobadas:
            self.materias.remove(materia)
        
        print("Asignaturas pendientes: " + str(self.materias))

# Pruebas:
alumno = Alumno("Javier", 44444444, 5)
alumno.completar_materias()
alumno.registrar_notas()
alumno = Alumno("Ignacio", 40000000)
alumno.completar_materias()
alumno.registrar_notas()