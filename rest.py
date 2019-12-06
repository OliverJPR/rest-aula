import requests
import json

class Estudiante:
    def __init__(self, nombre, correo, carrera, matricula=None):
        self.nombre = nombre
        self.correo = correo
        self.carrera = carrera
        self.matricula = matricula

    def __str__(self):
        estudiante = "Nombre: " + str(self.nombre) + "\nMatricula: " + str(
            self.matricula) + "\nCorreo: " + str(self.correo) + "\nCarrera: " + str(self.carrera)
        return estudiante

# Crea un string formatiado de python JSON object 
def object2json(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Funcion para obtener todos los estudiantes del api
def get_estudiantes():
    req = requests.get('http://localhost:4567/rest/estudiantes/')
    object2json(req.json())

#Funcion para crear un estudiante en el api
def post_estudiante():
    print("\n")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    carrera = input("Carrera: ")
    estudiante = Estudiante(nombre, correo, carrera)
    requests.post('http://localhost:4567/rest/estudiantes/',json=estudiante.__dict__)
    print("Estudiante generado ")
   

#Funcion para obtener un estudiante en especifico del api
def get_estudiante():
    matricula = int(input("Digite matricula: "))
    response = requests.get(
        "http://localhost:4567/rest/estudiantes/" + str(matricula))
    estudiante = Estudiante(
        response.json()["nombre"], response.json()["correo"], response.json()["carrera"], response.json()["matricula"])
    print("\n" + str(estudiante))
    return estudiante


#Menu de opciones
    opcion = -1
while True:
    print("**************Menu********************")
    print(" 1. Listar Todos los estudiantes")
    print(" 2. Consultar estudiantes")
    print(" 3. Crear un nuevo estudiante ")
    print(" 0. Exit")
    print("**************************************")
   
    opcion = int(input("Opción tomada: "))

    if opcion == 0:
        break
    elif opcion == 1:
        get_estudiantes()
    elif opcion == 2:
        get_estudiante()
    elif opcion == 3:
        post_estudiante()




