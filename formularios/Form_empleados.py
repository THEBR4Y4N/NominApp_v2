import tkinter as tk
import csv
from fpdf import FPDF
from tkinter import ttk, messagebox
from config import COLOR_CUERPO_PRINCIPAL, COLOR_BARRA_SUPERIOR
from database import Reporte_personal_basico


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
            rows, column_names = Reporte_personal_basico()
            if not rows:
                print("No se han obtenido datos para generar el PDF.")
                return

            pdf = FPDF(orientation='L', unit='in', format='legal')
            pdf.add_page()

            pdf.set_font("Arial", 'B', 16)
            pdf.cell(8.3, 0.5, "Lista de empleados", 0, 1, 'C')
            pdf.ln(0.2)
            pdf.set_font("Arial", size=12)
            col_width = 1.3  # Ajustar el ancho de las celdas
            cell_height = 0.3  # Ajustar la altura de las celdas
            spacing = 0.1

            for column in column_names:
                pdf.cell(col_width, cell_height + spacing, column, 1, 0, 'C')
            pdf.ln()
            # Imprimir datos
            for row in rows:
                for item in row:
                    pdf.cell(col_width, cell_height + spacing, str(item), 1, 0, 'C')
                pdf.ln()
            pdf_output = "consulta_resultados.pdf"
            pdf.output(pdf_output)
            messagebox.showinfo("Reporte Generado Exitosamente", "Se ha generado el archivo PDF con los resultados de la consulta.")

        def exportar_csv():
            with open("ReporteEmplados.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(column_names)  # Escribir encabezados
                for dato in datos_desde_bd:
                    writer.writerow(dato)

        rows = Reporte_personal_basico()
        self.boton_pdf = tk.Button(panel_principal, text="Exportar a PDF",
                                   command=exportar_pdf,
                                   bg=COLOR_BARRA_SUPERIOR,
                                   fg="white", bd=0)
        self.boton_pdf.pack(side=tk.LEFT, padx=20, pady=10)

        self.boton_csv = tk.Button(panel_principal, text="Exportar a CSV", command=exportar_csv,
                                   bg=COLOR_BARRA_SUPERIOR, fg="white", bd=0)
        self.boton_csv.pack(side=tk.LEFT, padx=20)
