import tkinter as tk
from tkinter import messagebox

# Crear el diccionario
informacion_personal = {
    "nombre": "Juanito Francisco Alcachofa Delaón",
    "edad": 45,
    "ciudad": "Turi",
    "profesion": "Ingeniero en Minas",
    "Residencia": "Sin especificar",
    "Estado Civil": "Viudo",
    "Trabajo Actual": "Docente en una institución educativa"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Quito"  # Modificar la ciudad

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0994503601"  # Número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad")

ventana = tk.Tk()
ventana.withdraw()

# Convertir el diccionario a un string para mostrarlo en el mensaje
mensaje = "\n".join(f"{clave}: {valor}" for clave, valor in informacion_personal.items())

messagebox.showinfo("Información Personal", mensaje)

ventana.destroy()
