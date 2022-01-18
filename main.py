"""Class y object (Código estructurado I)"""
#Class "paquetizar" datos y funciones en una misma entidad
#Define el tipo de dato
#Object: variables y metodos dentro de las clases
#Ej: datos_coche es una clase y lista_coches es el obajeto
#Podemos tener variables que las compartan todos los objetos de una clase.
#Función de clase 1: __init_
#Función de clase 2:
#Variable self(hace referencia al objeto)
"""Ejercicio Clase 10"""
class Car:
    def __init__(self, marca, modelo, combustible, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.pos_x = 0
        self.pos_y = 0

    def move_to(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_incr(self, x, y):
        self.pos_x += x #poner esto
        self.pos_y += y             #Y poner esto, es lo mismo!

    def get_pos(self):
        return self.pos_x, self.pos_y

lista_coches = []

while True:
    marca = input("Introduce la marca: ")
    if marca == "fin":
        break
    modelo = input("Introduce el modelo: ")
    combustible = input("Introduce el combustible: ")
    cilindrada = input("Introduce la cilindrada: ")

#Añadimos a un diccionario las variables
    diccionario_coche = {}
    diccionario_coche["Marca"] = marca
    diccionario_coche["Modelo"] = modelo
    diccionario_coche["Combustible"] = combustible
    diccionario_coche["Cilindrada"] = cilindrada
#Añadimos a la lista los diccionarios
    lista_coches.append(diccionario_coche)
    C = Car(marca, modelo, combustible, cilindrada)

    print(C.marca)
    print(C.modelo)
    print(C.combustible)
    print(C.cilindrada)
    print(C.get_pos())
    C.move_to(100, 25)
    print(C.get_pos())
    C.move_incr(10, 20)
    print(C.get_pos())

class Wheel:
    def __init__(self, ancho, rodadura, diametro):
        self.ancho = ancho
        self.rodadura = rodadura
        self.diametro = diametro
        self.presion = 0

    def set_pressure(self, presion):
        self.presion = presion

    def print_info(self):
        return "Ancho en mm", self.ancho,"\nPorcentaje de rodadura: ", self.rodadura,"\nDiametro en pulgadas: ", self.diametro,"\nPresion: ", self.presion

while True:
    ancho = input("Ancho de rueda: ")
    if ancho == "fin":
        break
    rodadura = input("Porcentaje rodadura: ")
    diametro = input("Introduce diametro: ")
    presion = input("Introduce presión: ")
    R = Wheel(ancho, rodadura, diametro)

    print(R.presion)
    seleccion_presion = input("Selecciona la presión que necesites: ")
    R.set_pressure(seleccion_presion)
    print(R.presion)
    print(R.print_info())
