import tkinter as tk
import csv
from tkinter import ttk
from config import COLOR_CUERPO_PRINCIPAL, COLOR_BARRA_SUPERIOR
from database import Reporte_personal_basico
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class Form_Empleados:

    def __init__(self, panel_principal) -> None:
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Gestion de personal")
        self.labelTitulo.config(fg="#222d33", font=("Arial", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True, pady=10)

        # tabla
        datos_desde_bd, column_names = Reporte_personal_basico()
        tabla_frame = tk.Frame(panel_principal, bg="white", width=400)
        tabla_frame.pack(fill=tk.BOTH, expand=True)
        tabla_frame.pack_propagate(False)
        tabla_container = tk.Frame(tabla_frame)
        tabla_container.pack(fill=tk.BOTH, expand=True)
        self.tabla = ttk.Treeview(tabla_container, columns=column_names, show="headings")
        for col in column_names:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100)

        scrollbar_x = ttk.Scrollbar(tabla_frame, orient="horizontal", command=self.tabla.xview)
        self.tabla.configure(xscrollcommand=scrollbar_x.set)
        self.tabla.pack(fill=tk.BOTH, expand=True)
        scrollbar_x.pack(fill=tk.X)

        for dato in datos_desde_bd:
            self.tabla.insert('', 'end', values=dato)

        self.tabla.pack(fill=tk.BOTH, expand=True, pady=10)

        def exportar_pdf():
            pdf = canvas.Canvas("ReporteEmplados.pdf", pagesize=letter)
            y = 750
            for dato in datos_desde_bd:
                x = 50
                for valor in dato:
                    pdf.drawString(x, y, str(valor))
                    x += 100
                y -= 20
            pdf.save()

        def exportar_csv():
            with open("ReporteEmplados.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(column_names)  # Escribir encabezados
                for dato in datos_desde_bd:
                    writer.writerow(dato)

        self.boton_pdf = tk.Button(panel_principal, text="Exportar a PDF", command=exportar_pdf,
                                   bg=COLOR_BARRA_SUPERIOR,
                                   fg="white", bd=0)
        self.boton_pdf.pack(side=tk.LEFT, padx=20, pady=10)

        self.boton_csv = tk.Button(panel_principal, text="Exportar a CSV", command=exportar_csv,
                                   bg=COLOR_BARRA_SUPERIOR, fg="white", bd=0)
        self.boton_csv.pack(side=tk.LEFT, padx=20)
