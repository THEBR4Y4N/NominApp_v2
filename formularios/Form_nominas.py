import tkinter as tk
from tkinter import ttk, font, messagebox
from config import COLOR_CUERPO_PRINCIPAL, COLOR_BARRA_SUPERIOR
from database import personal_info, Desprendible




def validate_input(new_value):
    return new_value.isdigit() or new_value == ''


class nominas:
    def __init__(self, panel_principal) -> None:
        font_awesome = font.Font(family='FontAwesome', size=12)
        self.encontrado = None
        self.habilitado = False
        self.cedula_id = None
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.labelTitulo = tk.Label(self.barra_superior, text="Gestion de nominas")
        self.labelTitulo.config(fg="#222d33", font=("Arial", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True, pady=10)
        # subtitulo
        self.labelTitulo2 = tk.Label(self.barra_superior, text="Desprendibles por empleado", justify='left')
        self.labelTitulo2.config(fg="#222d33", font=("Arial", 20), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo2.pack(side=tk.LEFT, fill='both', expand=False, pady=10, anchor='w')
        # información
        datos_empleados, column_names = personal_info()
        info_frame = tk.Frame(panel_principal, bg="white", width=400)
        info_frame.pack(fill=tk.BOTH, expand=False)
        info_frame.pack_propagate(False)
        info_frame.pack(pady=(0, 5))
        frame_etiqueta_cedula = tk.Frame(info_frame, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_cedula.grid(row=0, column=0, padx=20, pady=5)
        self.etiqueta_cedula = tk.Label(info_frame, text="Cedula", font=('Roboto', 14),
                                        fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_cedula.grid(row=0, column=0, padx=20, pady=5)
        vcmd = panel_principal.register(validate_input)
        self.cedula = ttk.Entry(info_frame, font=('Roboto', 14), width=12, validate="key",
                                validatecommand=(vcmd, '%P'))
        self.cedula.grid(row=0, column=1, padx=20, pady=5)
        self.boton_buscar = tk.Button(info_frame, text='\uf002', font=font_awesome,
                                      bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white", command=self.buscar_por_id)
        self.boton_buscar.grid(row=0, column=2, pady=5)
        # tabla
        tabla_frame = tk.Frame(panel_principal, bg="white", width=10)
        tabla_frame.pack(fill=tk.BOTH, expand=True)
        tabla_frame.pack_propagate(False)
        tabla_frame.pack(pady=(0, 5))
        tabla_container = tk.Frame(tabla_frame)
        tabla_container.pack(fill=tk.BOTH, expand=False)
        self.tabla = ttk.Treeview(tabla_container, columns=column_names, show="headings")
        column_width = 80
        for col in column_names:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=column_width)
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for dato in datos_empleados:
            self.tabla.insert('', 'end', values=dato)
        tabla_frame_width = len(column_names) * column_width + 4
        tabla_frame_height = len(datos_empleados) * 20
        tabla_frame.config(width=tabla_frame_width, height=tabla_frame_height)
        self.tabla.pack(fill=tk.BOTH, expand=False, pady=10)
        self.tabla.bind("<<TreeviewSelect>>", self.on_treeview_select)
        # descargar
        descarga_frame = tk.Frame(panel_principal, bg="white", width=10)
        descarga_frame.pack(fill=tk.BOTH, expand=True)
        descarga_frame.pack_propagate(False)
        descarga_frame.pack(pady=(0, 5))
        self.boton_descargar = tk.Button(descarga_frame, text='\uf019 Descargar Desprendible de pago',
                                         font=font_awesome,
                                         bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white", command=self.generar_Desprendible)
        self.boton_descargar.pack(padx=10, pady=10, ipadx=20, ipady=10, side=tk.LEFT)
        self.boton_descargar.config(state=tk.DISABLED)

    def buscar_por_id(self):
        self.tabla.selection_set('')
        self.tabla.focus('')
        self.tabla.see('')
        self.encontrado = False
        self.boton_descargar.config(state=tk.DISABLED)
        id_buscar = self.cedula.get()
        for item in self.tabla.get_children():
            if self.tabla.item(item)['values'][0] == int(id_buscar):
                self.cedula_id = id_buscar
                self.tabla.selection_set(item)
                self.tabla.focus(item)
                self.tabla.see(item)
                self.encontrado = True
                self.boton_descargar.config(state=tk.NORMAL)
                self.cedula.delete(0, tk.END)
                break
        if not self.encontrado:
            messagebox.showwarning("Empleado no encontrado", "Verifica los datos ingresados nuevamente....")
            self.cedula.delete(0, tk.END)

    def on_treeview_select(self, event):
        selected_item = self.tabla.focus()
        values = self.tabla.item(selected_item, 'values')
        if values:
            id_seleccionado = values[0]
            self.habilitado = True
            self.boton_descargar.config(state=tk.NORMAL)
            self.cedula_id = id_seleccionado

    def generar_Desprendible(self):
        cedula_empleado = self.cedula_id
        rows, column_names = Desprendible(cedula_empleado)
        if not rows:
            messagebox.showerror("Error al generar Desprendible",
                                 "No se encontraron datos para la cédula " + cedula_empleado)
        else:
            nombre_archivo = 'Desprendible de nomina '+cedula_empleado+'.txt'
            with open(nombre_archivo, 'w') as file:
                file.write('|'.join(column_names) + '\n')
                for row in rows:
                    file.write('|'.join(row) + '\n')
            messagebox.showinfo("Desprendible Generado Exitosamente",
                                "Se ha generado el Desprendible de pago para "+cedula_empleado+" Exitosamente...")