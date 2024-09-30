# Abrir el archivo "my_notes.txt" en modo de escritura y usar write() para agregar contenido
with open("my_notes.txt", "w") as file:
    file.write("Planificar el proyecto de desarrollo web para la próxima semana.\n")
    file.write("Revisar el informe técnico y agregar las conclusiones finales.\n")
    file.write("Practicar ejercicios de algoritmos para mejorar en programación.\n")

# Leer el archivo "my_notes.txt" usando readline() para leer línea por línea
with open("my_notes.txt", "r") as file:
    # Leer y mostrar cada línea con readline()
    line = file.readline()
    while line:
        print(line.strip())  # Elimina los caracteres de nueva línea al final
        line = file.readline()  # Lee la siguiente línea
