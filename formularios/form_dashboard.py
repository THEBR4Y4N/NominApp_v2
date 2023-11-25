import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from database import total_empleados, datos_salarios

from config import COLOR_CUERPO_PRINCIPAL


class Form_Dashboard:
    def __init__(self, panel_principal) -> None:
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Dashboard")
        self.labelTitulo.config(fg="#222d33", font=("Arial", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True, pady=10)
        info_frame = tk.Frame(panel_principal, bg="white", width=400)
        info_frame.pack(fill=tk.BOTH, expand=False)
        info_frame.pack_propagate(False)
        info_frame.pack(pady=(0, 5))
        frame_etiqueta_empleados = tk.Frame(info_frame, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_empleados.grid(row=0, column=0, padx=20, pady=5)
        self.labelEmpleados = tk.Label(frame_etiqueta_empleados, text="Numero de empleados:", justify='left')
        self.labelEmpleados.config(fg="#222d33", font=("Arial", 20), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelEmpleados.pack(side=tk.LEFT, fill='both', expand=False, pady=10, anchor='w')
        self.label_valor = tk.Label(frame_etiqueta_empleados, text="")
        self.label_valor.config(fg="#222d33", font=("Arial", 20), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_valor.pack(padx=20, pady=10)
        self.actualizar_label()
        self.frame_grafico = tk.Frame(panel_principal)
        self.frame_grafico.pack(fill=tk.BOTH, expand=True)
        nombres_empleados, salarios = datos_salarios()
        fig, ax = plt.subplots(figsize=(9, 5))
        bars = ax.barh(nombres_empleados, salarios, color='skyblue')
        for bar, salario in zip(bars, salarios):
            ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{salario:,}',
                    va='center', ha='left', fontsize=8, color='black')
        ax.set_xlabel('Salario neto')
        ax.set_title('Salarios de los empleados')
        ax.invert_yaxis()
        plt.gca().xaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
        plt.tight_layout()
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame_grafico)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def actualizar_label(self):
        total = total_empleados()
        if total is not None:
            self.label_valor.config(text=total)
        else:
            self.label_valor.config(text=0)