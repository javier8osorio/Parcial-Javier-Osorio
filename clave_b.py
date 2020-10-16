from math import pi

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 3 numeros
2+4+6 = 12
"""


# start-->
def suma(numero1, numero2, numero3):
    resultado = numero1 + numero2 + numero3
    print(resultado)
    return resultado



"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros impares del 1 al 1000
"""


# start-->
def sumaImpares():
    numeros = []

    numero = 0
    while numero<1000:
        numero+=1
        if numero % 2 != 0:
            numeros.append(numero) #Añade el numero al array


    result = sum(numeros)

    print(result)

    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el perimetro, area y el volumen de un esfera
radio = 12 m

perimetro: 2*pi*r
area: 4*pi*r^2
volumen: (4/3)*pi*r^3
"""
#Profe en este no me da el pass, asi que le imprimi 
#los valores ya que los valores si me dan

# start-->
def definicionEsfera(radio):
    result = print(f"perimetro: {obtenerPerimetro()} area: {obtenerArea()} volumen: {obtenerVolumen()}")
    return result


def obtenerPerimetro():
    result = float(2 * pi * 12)
    return result


def obtenerArea():
    result = float(4 * pi * 12**2)
    return result


def obtenerVolumen():
    result = float((4/3) * pi * 12**3)
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""

#Profe en este no me da el pass, asi que le imprimi 
#los valores ya que los valores si me dan


# start-->
class Esfera:
    def definicionEsfera(self, radio):
        self.radio = radio
        result = print(f"perimetro: {obtenerPerimetro()} area: {obtenerArea()} volumen: {obtenerVolumen()}")
        return result

    def obtenerPerimetro(self):
        result = float(2 * pi * self.radio)
        return result


    def obtenerArea(self):
        result = float(4 * pi * self.radio**2)
        return result


    def obtenerVolumen(self):
        result = float((4/3) * pi * self.radio**3)
        return result
        
    


"""
***************************************************************
@@ ejercicio 5 @@
Banco
Cliente
    nombre
    lugar
    numero de cuenta
    transaccion - retiro o abono
    monto
"""


class Banco:
    def __init__(self):
        self.listaClientes = []

    def procesar(self, nombre, ciudad, id, operacion, monto):
        cliente = Cliente(nombre, ciudad, id, operacion, monto)
        self.listaClientes.append(cliente)

    def abonosSanSalvador(self):
        abonototal = 0
        for Cliente in self.listaClientes:
            ciudad = Cliente.getCiudad()
            proceso = Cliente.getOperacion()
            if ciudad == "san salvador" and proceso == "abono":
                abonototal = abonototal + Cliente.getMonto()
        return abonototal


    def abonosBalYRod(self):
        abonototal = 0
        for Cliente in self.listaClientes:
            nombre1 = Cliente.getNombre()
            proceso = Cliente.getOperacion()
            nombre2 = Cliente.getNombre()
            if (nombre1 == "rodrigo" or nombre2 == "balbino") and proceso == "abono"  :
                abonototal = abonototal + Cliente.getMonto()
        return abonototal


class Cliente:
    def __init__ (self, nombre, ciudad, id, operacion, monto):
        self.nombre = nombre
        self.ciudad = ciudad
        self.id = id
        self.operacion = operacion
        self.monto = monto

    def getNombre(self):
        return self.nombre

    def getCiudad(self):
        return self.ciudad

    def getId(self):
        return self.id

    def getOperacion(self):
        return self.operacion

    def getMonto(self):
        return self.monto


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/javier8osorio/Parcial-Javier-Osorio.git"
