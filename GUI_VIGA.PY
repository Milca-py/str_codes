import tkinter as tk
from math import sqrt


def calcular_area_acero():
    b = float(ancho_viga.get())           # cm - ancho de la viga
    h = float(alto_viga.get())            # cm - altura de la viga
    r = float(recubrimiento.get())        # cm - recubrimiento de la viga
    # kg/cm2 - resistencia del concreto
    fc = float(resistencia_concreto.get())
    # kg/cm2 - resistencia del acero
    fy = float(resistencia_acero.get())
    # kg-cm - momento flector último
    Mu = float(momento_flector.get())
    φ = 0.9                                 # factor de reducción (flexion)
    d = h - r                               # cm - peralte efectivo

    As = (0.85 * b * d * fc) / fy * \
        (1 - sqrt(1 - (2.353 * Mu) / (φ * b * d ** 2 * fc)))
    resultado.set(As)


ventana = tk.Tk()
ventana.title("Cálculo de Área de Acero en Viga")

# Entradas de datos
tk.Label(ventana, text="Ancho de la viga (cm):").grid(
    row=0, column=0, sticky='w')
ancho_viga = tk.Entry(ventana)
ancho_viga.grid(row=0, column=1)

tk.Label(ventana, text="Altura de la viga (cm):").grid(
    row=1, column=0, sticky='w')
alto_viga = tk.Entry(ventana)
alto_viga.grid(row=1, column=1)

tk.Label(ventana, text="Recubrimiento (cm):").grid(row=2, column=0, sticky='w')
recubrimiento = tk.Entry(ventana)
recubrimiento.grid(row=2, column=1)

tk.Label(ventana, text="Resistencia del concreto (kg/cm2):").grid(row=3,
                                                                  column=0, sticky='w')
resistencia_concreto = tk.Entry(ventana)
resistencia_concreto.grid(row=3, column=1)

tk.Label(ventana, text="Resistencia del acero (kg/cm2):").grid(row=4,
                                                               column=0, sticky='w')
resistencia_acero = tk.Entry(ventana)
resistencia_acero.grid(row=4, column=1)

tk.Label(ventana, text="Momento flector último (kg-cm):").grid(row=5,
                                                               column=0, sticky='w')
momento_flector = tk.Entry(ventana)
momento_flector.grid(row=5, column=1)

# Botón de cálculo
boton_calcular = tk.Button(
    ventana, text="Calcular Área de Acero", command=calcular_area_acero)
boton_calcular.grid(row=6, column=0, columnspan=2)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, text="Área de Acero (cm2):").grid(
    row=7, column=0, sticky='w')
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.grid(row=7, column=1)

ventana.mainloop()
