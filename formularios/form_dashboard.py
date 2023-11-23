import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Form_Dashboard:
    def __init__(self, panel_principal) -> None:
        figura = Figure(figsize=(8, 6), dpi=100)
        ax1 = figura.add_subplot(211)
        figura.subplots_adjust(hspace=0.4)
        self.grafico1(ax1)

        canvas = FigureCanvasTkAgg(figura, master=panel_principal)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def grafico1(self, ax):
        x = [1, 2, 3, 4, 5]
        y = [6, 7, 8, 9, 10]
        ax.bar(x, y, label="grafico 1", color="blue", alpha=0.7)
        ax.set_title("Grafico de prueba")
        ax.set_xlabel("eje x")
        ax.set_ylabel("eje y")
        ax.legend()
        for i, v in enumerate(y):
            ax.text(x[i] - 0.1, v + 0.1, str(v), color='black')
        ax.grid(axis='y', linestyle='--', alpha=0.7)
