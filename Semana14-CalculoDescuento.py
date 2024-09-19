import tkinter as tk
from tkinter import messagebox


def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado al monto total según el porcentaje de descuento.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (default es 10%).
    :return: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def aplicar_descuento():
    try:
        monto_total = float(entry_monto.get())
        porcentaje_descuento = float(entry_descuento.get())

        descuento = calcular_descuento(monto_total, porcentaje_descuento)
        monto_final = monto_total - descuento

        result_text = (
            f"Monto Total: ${monto_total:.2f}\n"
            f"Porcentaje de Descuento: {porcentaje_descuento}%\n"
            f"Monto del Descuento: ${descuento:.2f}\n"
            f"Monto Final a Pagar: ${monto_final:.2f}"
        )
        messagebox.showinfo("Resultado del Descuento", result_text)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Descuento")

# Crear y colocar widgets
tk.Label(ventana, text="Monto Total:").grid(row=0, column=0, padx=10, pady=10)
entry_monto = tk.Entry(ventana)
entry_monto.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Porcentaje de Descuento:").grid(row=1, column=0, padx=10, pady=10)
entry_descuento = tk.Entry(ventana)
entry_descuento.grid(row=1, column=1, padx=10, pady=10)

btn_calcular = tk.Button(ventana, text="Calcular Descuento", command=aplicar_descuento)
btn_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

# Ejecutar la aplicación
ventana.mainloop()
