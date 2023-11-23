import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL


class Formulario_construccion():

    def __init__(self, panel_principal, logo):
        self.barra_Superior = tk.Frame(panel_principal)
        self.barra_Superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.barra_Inferior = tk.Frame(panel_principal)
        self.barra_Inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        self.label_imagen = tk.Label(self.barra_Inferior, image=logo)
        self.label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        self.label_imagen.config(fg="#fff", font=("Roboto", 10), bg=COLOR_CUERPO_PRINCIPAL)
