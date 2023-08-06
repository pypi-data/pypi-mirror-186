import json

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
BLACK = '\033[30m'

with open("config.json", "r") as f:
    data = json.load(f)
    
personas = {}

messages = data["messages"]

welcome_message = messages["welcomeMessage"]
goodbye_message = messages["goodbyeMessage"]
save_message = messages["saveMessage"]
edit_message = messages["editMessage"]
error_message = messages["errorMessage"]
delete_message = messages["deleteMessage"]


def showWelcome():
    print("========================*********========================")
    print(BLUE+"\t"+welcome_message)
    print("========================*********========================")

def showGoodBye():
    print("========================*********========================")
    print("\t"+goodbye_message)
    print("========================*********========================")

def showSave():
    print("========================*********========================")
    print("+\t"+GREEN+save_message)
    print("========================*********========================")
    print("     -")

def showEdit():
    print("========================*********========================")
    print(YELLOW+"\t"+edit_message)
    print("========================*********========================")

def showDelete():
    print("========================*********========================")
    print(RED+"\t"+delete_message)
    print("========================*********========================")

def showError():
    print("========================*********========================")
    print("\t"+error_message)
    print("========================*********========================")

# Definimos la clase que representará a cada registro del CRUD
class Registro:
  def __init__(self, *args, **kwargs):
    # Creamos atributos dinámicamente con los nombres y valores especificados en kwargs
    for k, v in kwargs.items():
      setattr(self, k, v)

# Definimos una lista que almacenará los registros del CRUD
registros = []

# función que permita al usuario ingresar la cantidad de campos que desea en el CRUD
def definir_campos():
  
  num_campos = data["campos"]["cantidad"]
  # num_campos = int(input(BLUE+"Ingrese la cantidad de campos que desea en el CRUD: "))
  print("")
  print(f"La cantidad es -{num_campos}")
  print("La cantidad depende de los campos en el archivo config.json")
  print("")
  return num_campos

# función que permita al usuario ingresar el nombre y tipo de datos de cada campo
def ingresar_campos(num_campos):
  campos = []  
  for i in range(num_campos):
    nombre = input(f"Ingrese el nombre del campo {i+1}: ")
    tipo = input(f"Ingrese el tipo de datos del campo {i+1} (p.ej. str, int, float): ")

    campos.append((nombre, tipo))
  showSave()
  return campos


# función que permita al usuario crear un nuevo registro
def crear_registro(campos):
  kwargs = {}
  for nombre, tipo in campos:
    valor = input(BLUE+f"Ingrese el valor del campo {nombre}: ")
    if tipo == "str":
      kwargs[nombre] = str(valor)
    elif tipo == "int":
      kwargs[nombre] = int(valor)
    elif tipo == "float":
      kwargs[nombre] = float(valor)
  # Creamos una instancia de la clase Registro y la agregamos a la lista de registros
  registros.append(Registro(**kwargs))
  showSave()


# función que permita al usuario consultar todos los registros
def consultar_registros():
  for i, r in enumerate(registros):
    print(f"Registro {i+1}:")
    print("================================")
    # Mostramos los valores de cada campo del registro
    for k, v in r.__dict__.items():
      print(MAGENTA+f"{k}: {v}")
    print("================================")
      

# función que permita al usuario actualizar un registro existente
def actualizar_registro(campos):
  
  id_registro = int(input("Ingrese el ID del registro a actualizar: "))
  # Obtenemos el registro con el ID especificado
  registro = registros[id_registro - 1]
  # Iteramos sobre cada campo del registro
  for nombre, tipo in campos:
    valor = input(f"Ingrese el nuevo valor para el campo {nombre}: ")
    # Convertimos el valor a su tipo correspondiente antes de asignarlo al registro
    if tipo == "str":
        setattr(registro, nombre, str(valor))
    elif tipo == "int":
        setattr(registro, nombre, int(valor))
    elif tipo == "float":
        setattr(registro, nombre, float(valor))
  showEdit()

# función que permita al usuario eliminar un registro existente
def eliminar_registro():
  id_registro = int(input("Ingrese el ID del registro a eliminar: "))
  # Eliminamos el registro con el ID especificado de la lista de registros
  del registros[id_registro - 1]
  showDelete()


def screenHandler(case_option = None, extension_function = None):
    num_campos = definir_campos()
    campos = ingresar_campos(num_campos)
    while True:
        showWelcome()
        print("Seleccione una opción:")
        opciones = ["1. Crear un nuevo registro", "2. Consultar todos los registros", "3. Actualizar un registro existente", "4. Eliminar un registro existente", "5. Salir"]
        if extension_function:
            opciones = extension_function(opciones)
        for opcion in opciones:
            if case_option == "upper":
                opcion = opcion.upper()
            elif case_option == "lower":
                opcion = opcion.lower()
            print(opcion)
        opcion = int(input())
        if opcion == 1:
            crear_registro(campos)
        elif opcion == 2:
            consultar_registros()
        elif opcion == 3:
            actualizar_registro(campos)
        elif opcion == 4:
            eliminar_registro()
        elif opcion == 5:
            showGoodBye()
            break

