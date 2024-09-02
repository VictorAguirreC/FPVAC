import tkinter as tk
from tkinter import messagebox

matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

def buscar_valor():
    try:
        valor_buscado = int(entry.get())  # Tomar el valor del campo de texto
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == valor_buscado:
                    resultado = f"Valor {valor_buscado} encontrado en la posición ({i}, {j})"
                    messagebox.showinfo("Resultado de Búsqueda", resultado)  # Mostrar el resultado
                    return
        resultado = f"Valor {valor_buscado} no encontrado en la matriz"
        messagebox.showinfo("Resultado de Búsqueda", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Búsqueda en Matriz")

# Configurar tamaño y colores
root.geometry("400x300")
root.configure(bg="#2E8B57")

# Etiqueta
label = tk.Label(root, text="Ingresa el valor a buscar:", bg="#2E8B57", fg="white", font=("Helvetica", 14))
label.pack(pady=20)

# Entrada de texto
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

# Botón de búsqueda
search_button = tk.Button(root, text="Buscar", command=buscar_valor, bg="#4682B4", fg="white", font=("Helvetica", 14))
search_button.pack(pady=20)

root.mainloop()
