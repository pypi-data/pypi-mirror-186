# #importando todo el módulo
# import saludos

# saludos.saludar()


# # importacion selectiva
# from saludos import saludar
# saludar()

# # importacion de todas las definiciones
# from saludos import *
# saludar()
# Saludo()

# importación desde paquete
from paquete_mensajes.subpaquete_hola.modulo_saludos import *
from paquete_mensajes.subpaquete_adios.modulo_despedidas import *

saludar("Said")
Saludo()

despedir()
Despedida()