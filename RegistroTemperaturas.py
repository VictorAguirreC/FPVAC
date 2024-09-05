import tkinter as tk

root = tk.Tk()
root.title("Promedios de Temperaturas por Ciudad y Semana")

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

resultado_texto = tk.Text(root, height=20, width=50)
resultado_texto.pack()

def calcular_promedios():
    resultado_texto.delete("1.0", tk.END)
    for ciudad_idx, ciudad in enumerate(temperaturas):
        resultado_texto.insert(tk.END, f"Promedios de temperaturas en {ciudades[ciudad_idx]}:\n")
        for semana_idx, semana in enumerate(ciudad):
            suma_temperaturas = sum(dia['temp'] for dia in semana)
            promedio_semana = suma_temperaturas / len(semana)
            resultado_texto.insert(tk.END, f"  Semana {semana_idx + 1}: {promedio_semana:.2f}°C\n")
        resultado_texto.insert(tk.END, "\n")

boton_calcular = tk.Button(root, text="Calcular Promedios", command=calcular_promedios)
boton_calcular.pack()

root.mainloop()
