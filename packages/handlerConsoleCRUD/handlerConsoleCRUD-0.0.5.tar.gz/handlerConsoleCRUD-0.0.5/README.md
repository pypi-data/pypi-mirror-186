# Librería que te permite hacer un CRUD con los campos que quieras

[Por Carlos Soto De Dios](https://www.linkedin.com/in/carlos-soto-537655224/)

# 💡Pre-requisitos

[Python 3](https://www.python.org/downloads/release/python-370/)

## Instalación

Para instalar la libreria necesitas introducir en la consola

```
pip install handlerConsoleCRUD
```

<br>

- Esta librería que te permite crear un programa en consola que te permite hacer un CRUD y los campos son a eleccion tuya.

- Tienes la libertad de alterar el nombre de las opciones del Menu del CRUD para eso debes crear una funcion y pasarla como parametro.

# Lo que necesitas

Necesitas un archivo JSON llamado > config.json < en tu directorio con la siguiente estructura

```
{
  "campos": {
    "cantidad": 1
  },
  "messages": {
    "welcomeMessage": "Welcome to the application!",
    "goodbyeMessage": "Thank you for using the application",
    "saveMessage": "Saved!!",
    "editMessage": "Edited Data!!",
    "errorMessage": "Oops there was an error",
    "deleteMessage": "Bye bye Charlie"
  }
}
```

- Aqui puedes modificar **Cantidad** que se refiere a la cantidad de campos que quieres que tenga tu CRUD.

- **Messages** lo puedes modificar para que presente un mensaje por cada operación realizada.

# - Estas son las opciones predeterminadas en el MENU a la que puedes Sobre escribir

```
opciones = ["1. Crear un nuevo registro", "2. Consultar todos los registros", "3. Actualizar un registro existente", "4. Eliminar un registro existente", "5. Salir"]
```

<br>

### 📚 Para implementarlo puedes Crear una funcion que te permita cambiar dichos valores y pasarlo como parametros

Como ejemplo le estoy pasando una funcion **change_option_function** OJO esta funcion la debes crear a como entiendas para modificar las opciones

```
from handlerConsoleCRUD import screenHandler

screenHandler(change_option_function)
```

### Tienes la opcion de poner el Menu de poner los valores todo en Mayusculas o todo en Minusculas solamente pasandole un parametro.

```
from handler import screenHandler

# En este caso le estamos pasando el parametro que los valores del Menu sean Mayusculas
screenHandler("upper",change_option_function)
```
