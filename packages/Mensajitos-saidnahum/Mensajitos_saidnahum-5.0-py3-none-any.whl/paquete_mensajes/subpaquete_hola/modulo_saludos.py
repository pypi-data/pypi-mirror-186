import numpy as np

def saludar(nombre):
   print(f"Hola {nombre} desde saludos.saludar()")
   
def prueba():
   print("Esto es una prueba de la nueva version")
   
def generar_array(numeros):
   return np.arange(numeros)

class Saludo:
   def __init__(self):
      print("Hola desde Saludo.__init__")

# Para correr sólo en este script y no desde otro importado
if __name__ == '__main__':
   print(generar_array(5))