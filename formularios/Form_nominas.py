import tkinter as tk
from config import COLOR_CUERPO_PRINCIPAL, COLOR_BARRA_SUPERIOR


class nominas:
    def __init__(self, panel_principal) -> None:
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Gestion de nominas")
        self.labelTitulo.config(fg="#222d33", font=("Arial", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True, pady=10)
