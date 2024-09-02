import tkinter as tk
from tkinter import messagebox

matriz = [
    [30, 10, 20],
    [60, 50, 40],
    [90, 70, 80]
]

# Función para ordenar una fila específica de la matriz
def ordenar_fila():
    try:
        fila_index = int(entry.get())  # Tomar el índice de la fila a ordenar
        if fila_index < 0 or fila_index >= len(matriz):
            raise IndexError  # Si el índice es inválido

        matriz[fila_index].sort()  # Ordenar la fila seleccionada
        mostrar_matrices()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
    except IndexError:
        messagebox.showerror("Error", "Índice de fila fuera de rango.")

# Función para mostrar la matriz original y la ordenada
def mostrar_matrices():
    # Mostrar la matriz original
    matriz_original = "\n".join([str(fila) for fila in matriz])
    resultado_label.config(text=f"Matriz ordenada:\n{matriz_original}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ordenar Fila de Matriz")

# Configurar tamaño y colores
root.geometry("400x400")
root.configure(bg="#4682B4")

# Etiqueta
label = tk.Label(root, text="Ingresa el índice de la fila a ordenar (0, 1, 2):", bg="#4682B4", fg="white", font=("Helvetica", 14))
label.pack(pady=20)

# Entrada de texto
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

# Botón de ordenar
sort_button = tk.Button(root, text="Ordenar", command=ordenar_fila, bg="#2E8B57", fg="white", font=("Helvetica", 14))
sort_button.pack(pady=20)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, bg="#4682B4", fg="white", font=("Helvetica", 12))
resultado_label.pack(pady=20)

root.mainloop()
