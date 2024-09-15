import tkinter as tk

# Ventana principal
root = tk.Tk()
root.title("Promedio de Temperaturas por Ciudad y Semana")

# Lista de ciudades
ciudades = ["Guayaquil", "Quito", "Cuenca"]

# Datos de temperaturas reales en °C para 3 ciudades, 4 semanas, 7 días
temperaturas = [
    [   # Guayaquil
        [{"day": "Lunes", "temp": 30}, {"day": "Martes", "temp": 31}, {"day": "Miércoles", "temp": 30}, {"day": "Jueves", "temp": 29}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 32}, {"day": "Domingo", "temp": 31}],
        [{"day": "Lunes", "temp": 31}, {"day": "Martes", "temp": 32}, {"day": "Miércoles", "temp": 33}, {"day": "Jueves", "temp": 32}, {"day": "Viernes", "temp": 31}, {"day": "Sábado", "temp": 30}, {"day": "Domingo", "temp": 31}],
        [{"day": "Lunes", "temp": 30}, {"day": "Martes", "temp": 31}, {"day": "Miércoles", "temp": 32}, {"day": "Jueves", "temp": 30}, {"day": "Viernes", "temp": 31}, {"day": "Sábado", "temp": 32}, {"day": "Domingo", "temp": 33}],
        [{"day": "Lunes", "temp": 30}, {"day": "Martes", "temp": 31}, {"day": "Miércoles", "temp": 30}, {"day": "Jueves", "temp": 29}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 32}, {"day": "Domingo", "temp": 31}]
    ],
    [   # Quito
        [{"day": "Lunes", "temp": 20}, {"day": "Martes", "temp": 21}, {"day": "Miércoles", "temp": 22}, {"day": "Jueves", "temp": 21}, {"day": "Viernes", "temp": 20}, {"day": "Sábado", "temp": 19}, {"day": "Domingo", "temp": 20}],
        [{"day": "Lunes", "temp": 21}, {"day": "Martes", "temp": 22}, {"day": "Miércoles", "temp": 23}, {"day": "Jueves", "temp": 22}, {"day": "Viernes", "temp": 21}, {"day": "Sábado", "temp": 20}, {"day": "Domingo", "temp": 21}],
        [{"day": "Lunes", "temp": 20}, {"day": "Martes", "temp": 21}, {"day": "Miércoles", "temp": 22}, {"day": "Jueves", "temp": 20}, {"day": "Viernes", "temp": 21}, {"day": "Sábado", "temp": 22}, {"day": "Domingo", "temp": 23}],
        [{"day": "Lunes", "temp": 20}, {"day": "Martes", "temp": 21}, {"day": "Miércoles", "temp": 20}, {"day": "Jueves", "temp": 19}, {"day": "Viernes", "temp": 20}, {"day": "Sábado", "temp": 22}, {"day": "Domingo", "temp": 21}]
    ],
    [   # Cuenca
        [{"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 19}, {"day": "Miércoles", "temp": 20}, {"day": "Jueves", "temp": 19}, {"day": "Viernes", "temp": 18}, {"day": "Sábado", "temp": 17}, {"day": "Domingo", "temp": 18}],
        [{"day": "Lunes", "temp": 19}, {"day": "Martes", "temp": 20}, {"day": "Miércoles", "temp": 21}, {"day": "Jueves", "temp": 20}, {"day": "Viernes", "temp": 19}, {"day": "Sábado", "temp": 18}, {"day": "Domingo", "temp": 19}],
        [{"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 19}, {"day": "Miércoles", "temp": 20}, {"day": "Jueves", "temp": 18}, {"day": "Viernes", "temp": 19}, {"day": "Sábado", "temp": 20}, {"day": "Domingo", "temp": 21}],
        [{"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 19}, {"day": "Miércoles", "temp": 18}, {"day": "Jueves", "temp": 17}, {"day": "Viernes", "temp": 18}, {"day": "Sábado", "temp": 20}, {"day": "Domingo", "temp": 19}]
    ]
]

# Función para calcular el promedio de temperatura por ciudad y semana
def calcular_promedio_temperaturas(ciudades, datos_temperaturas):
    promedios = {}
    for ciudad_idx, ciudad in enumerate(ciudades):
        promedios[ciudad] = []
        for semana in datos_temperaturas[ciudad_idx]:
            suma_temperaturas = sum(dia['temp'] for dia in semana)
            promedio_semana = suma_temperaturas / len(semana)
            promedios[ciudad].append(promedio_semana)
    return promedios

# TextBox para mostrar resultados
resultado_texto = tk.Text(root, height=20, width=50)
resultado_texto.pack()

def mostrar_resultados():
    resultado_texto.delete("1.0", tk.END)
    promedios = calcular_promedio_temperaturas(ciudades, temperaturas)
    for ciudad, promedios_semanales in promedios.items():
        resultado_texto.insert(tk.END, f"Promedio de temperaturas en {ciudad}:\n")
        for semana_idx, promedio in enumerate(promedios_semanales):
            resultado_texto.insert(tk.END, f"  Semana {semana_idx + 1}: {promedio:.2f}°C\n")
        resultado_texto.insert(tk.END, "\n")

# Botón para calcular y mostrar resultados
boton_calcular = tk.Button(root, text="Calcular Promedios", command=mostrar_resultados)
boton_calcular.pack()

root.mainloop()
