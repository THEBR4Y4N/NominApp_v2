import random
import tkinter as tk
from tkinter import ttk, font, messagebox
from config import COLOR_CUERPO_PRINCIPAL, COLOR_BARRA_SUPERIOR
from tkcalendar import Calendar
from datetime import date
from database import (TipoCuenta, Bancos, Cargo, Departamento, TipoCont, EPS, Fondo_Cesantias, Fondo_Pensiones,
                      insertar_CuentaB_empleado, insertar_empleado, insertar_Cesantias_empleados,
                      insertar_EPS_empleados, insertar_pensiones_empleados, insertar_descuentos, insertar_devengados)


class Registrar_empleado:

    def __init__(self, panel_principal) -> None:
        font_awesome = font.Font(family='FontAwesome', size=12)
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Registro de personal")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True, pady=10)
        self.id_tcuenta = None
        self.id_banco = None
        self.id_tipo_contrato = None
        self.id_cargo = None
        self.id_DPTO = None
        self.id_cesantias = None
        self.ID_EPS = None
        self.id_pensiones = None
        self.valor_Salud = None
        self.valor_Pension = None
        self.valor_Fdo_Sol = None
        self.valor_Bancos = None
        self.valor_Fondo_de_Empleados = None
        self.porcentaje_salud = 0.04
        self.porcentaje_pension = 0.04
        self.Sub_Tpte = 140606
        self.subsitrans = None

        panel_principal1 = tk.Frame(panel_principal, height=50, bd=0, relief=tk.SOLID, bg=COLOR_CUERPO_PRINCIPAL)
        panel_principal1.pack()

        # cedula
        frame_etiqueta_cedula = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_cedula.grid(row=0, column=0, padx=20, pady=5)
        self.etiqueta_cedula = tk.Label(frame_etiqueta_cedula, text="Cedula", font=('Roboto', 14),
                                        fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_cedula.grid(row=0, column=0, padx=20, pady=5)
        vcmd = panel_principal.register(self.validate_input)
        self.cedula = ttk.Entry(frame_etiqueta_cedula, font=('Roboto', 14), width=12, validate="key",
                                validatecommand=(vcmd, '%P'))
        self.cedula.grid(row=0, column=1, padx=20, pady=5)

        # Nombre
        frame_etiqueta_nombre = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_nombre.grid(row=0, column=1, padx=20, pady=5)
        self.etiqueta_nombre = tk.Label(frame_etiqueta_nombre, text="Nombre", font=('Roboto', 14),
                                        fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_nombre.grid(row=0, column=0, padx=20, pady=5)
        self.nombre = ttk.Entry(frame_etiqueta_nombre, font=('Roboto', 14), width=20)
        self.nombre.grid(row=0, column=1, padx=20, pady=5)

        # Apellido
        frame_etiqueta_apellido = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_apellido.grid(row=0, column=2, padx=20, pady=5)
        self.etiqueta_nombre = tk.Label(frame_etiqueta_apellido, text="Apellido", font=('Roboto', 14),
                                        fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_nombre.grid(row=0, column=0, padx=20, pady=5)
        self.apellido = ttk.Entry(frame_etiqueta_apellido, font=('Roboto', 14), width=20)
        self.apellido.grid(row=0, column=1, padx=20, pady=5)

        # segunda Fila
        # Salario
        frame_etiqueta_salario = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_salario.grid(row=1, column=0, padx=20, pady=5)
        self.etiqueta_cedula = tk.Label(frame_etiqueta_salario, text="Salario Neto $", font=('Roboto', 14),
                                        fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_cedula.grid(row=1, column=0, padx=20, pady=5)
        vcmd = panel_principal.register(self.validate_input)
        self.salario = ttk.Entry(frame_etiqueta_salario, font=('Roboto', 14), width=12, validate="key",
                                 validatecommand=(vcmd, '%P'))
        self.salario.grid(row=1, column=1, padx=20, pady=5)

        # Cuenta
        frame_etiqueta_cuenta = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_cuenta.grid(row=1, column=1, padx=20, pady=5)
        self.etiqueta_cuenta = tk.Label(frame_etiqueta_cuenta, text="N° de cuenta", font=('Roboto', 14),
                                        fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_cuenta.grid(row=1, column=0, padx=20, pady=5)
        vcmd = panel_principal.register(self.validate_input)
        self.cuenta = ttk.Entry(frame_etiqueta_cuenta, font=('Roboto', 14), width=15, validate="key",
                                validatecommand=(vcmd, '%P'))
        self.cuenta.grid(row=1, column=1, padx=20, pady=5)

        # tipo cuenta
        frame_etiqueta_tcuenta = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_tcuenta.grid(row=1, column=2, padx=20, pady=5)
        self.etiqueta_tcuenta = tk.Label(frame_etiqueta_tcuenta, text="Tipo de cuenta", font=('Roboto', 14),
                                         fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_tcuenta.grid(row=1, column=0, padx=20, pady=5)

        self.tcuenta = ttk.Combobox(frame_etiqueta_tcuenta, font=('Roboto', 14), width=15)
        self.tcuenta.grid(row=1, column=1, padx=20, pady=5)
        ids_tcuenta = TipoCuenta(self.tcuenta)

        def obtener_id_tcuenta(event):
            tcuenta_seleccionado = self.tcuenta.get()
            if tcuenta_seleccionado in ids_tcuenta:
                self.id_tcuenta = ids_tcuenta[tcuenta_seleccionado]

            return None

        self.tcuenta.bind("<<ComboboxSelected>>", obtener_id_tcuenta)

        # tercera fila
        # Banco
        frame_etiqueta_banco = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_banco.grid(row=2, column=0, padx=20, pady=5)
        self.etiqueta_banco = tk.Label(frame_etiqueta_banco, text="Banco", font=('Roboto', 14),
                                       fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_banco.grid(row=2, column=0, padx=20, pady=5)
        self.bancos = ttk.Combobox(frame_etiqueta_banco, font=('Roboto', 14), width=35)
        self.bancos.grid(row=2, column=1, padx=20, pady=5)
        ids_bancos = Bancos(self.bancos)

        def obtener_id_bancos(event):
            banco_seleccionado = self.bancos.get()
            if banco_seleccionado in ids_bancos:
                self.id_banco = ids_bancos[banco_seleccionado]

        self.bancos.bind("<<ComboboxSelected>>", obtener_id_bancos)

        # Cargo
        frame_etiqueta_cargo = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_cargo.grid(row=2, column=1, padx=20, pady=5)
        self.etiqueta_cargo = tk.Label(frame_etiqueta_cargo, text="Cargo", font=('Roboto', 14),
                                       fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_cargo.grid(row=2, column=0, padx=20, pady=5)
        self.cargos = ttk.Combobox(frame_etiqueta_cargo, font=('Roboto', 14), width=12)
        self.cargos.grid(row=2, column=1, padx=20, pady=5)
        ids_cargo = Cargo(self.cargos)

        def obtener_id_cargo(event):
            cargo_seleccionado = self.cargos.get()
            if cargo_seleccionado in ids_cargo:
                self.id_cargo = ids_cargo[cargo_seleccionado]

        self.cargos.bind("<<ComboboxSelected>>", obtener_id_cargo)

        # Área
        frame_etiqueta_area = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_area.grid(row=2, column=2, padx=20, pady=5)
        self.etiqueta_area = tk.Label(frame_etiqueta_area, text="Área", font=('Roboto', 14),
                                      fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_area.grid(row=2, column=0, padx=20, pady=5)
        self.area = ttk.Combobox(frame_etiqueta_area, font=('Roboto', 14), width=15)
        self.area.grid(row=2, column=1, padx=20, pady=5)
        ids_dpto = Departamento(self.area)

        def obtener_id_dpto(event):
            dpto_seleccionado = self.area.get()
            if dpto_seleccionado in ids_dpto:
                self.id_DPTO = ids_dpto[dpto_seleccionado]

        self.area.bind("<<ComboboxSelected>>", obtener_id_dpto)

        # cuarta fila
        # tipo contrato
        frame_etiqueta_tc = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_tc.grid(row=3, column=0, padx=20, pady=5)
        self.etiqueta_tc = tk.Label(frame_etiqueta_tc, text="Tipo contrato", font=('Roboto', 14),
                                    fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_tc.grid(row=3, column=0, padx=20, pady=5)
        self.tipocontra = ttk.Combobox(frame_etiqueta_tc, font=('Roboto', 14), width=35)
        self.tipocontra.grid(row=3, column=1, padx=20, pady=5)
        ids_tipocont = TipoCont(self.tipocontra)

        def obtener_id_tcontra(event):
            tcontra_seleccionado = self.tipocontra.get()
            if tcontra_seleccionado in ids_tipocont:
                self.id_tipo_contrato = ids_tipocont[tcontra_seleccionado]

        self.tipocontra.bind("<<ComboboxSelected>>", obtener_id_tcontra)

        # eps
        frame_etiqueta_eps = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_eps.grid(row=3, column=1, padx=20, pady=5)
        self.etiqueta_EPS = tk.Label(frame_etiqueta_eps, text="EPS", font=('Roboto', 14),
                                     fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_EPS.grid(row=3, column=0, padx=20, pady=5)
        self.EPS = ttk.Combobox(frame_etiqueta_eps, font=('Roboto', 14), width=35)
        self.EPS.grid(row=3, column=1, padx=10, pady=5)
        ids_eps = EPS(self.EPS)

        def obtener_id_eps(event):
            eps_seleccionado = self.EPS.get()
            if eps_seleccionado in ids_eps:
                self.ID_EPS = ids_eps[eps_seleccionado]

        self.EPS.bind("<<ComboboxSelected>>", obtener_id_eps)

        # Fondo_Cesantias
        frame_etiqueta_cesantias = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_cesantias.grid(row=3, column=2, padx=20, pady=5)
        self.etiqueta_cesantias = tk.Label(frame_etiqueta_cesantias, text="Fondo Cesantias", font=('Roboto', 14),
                                           fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_cesantias.grid(row=3, column=0, padx=20, pady=5)
        self.cesantias = ttk.Combobox(frame_etiqueta_cesantias, font=('Roboto', 14), width=17)
        self.cesantias.grid(row=3, column=1, padx=10, pady=5)
        ids_cesantias = Fondo_Cesantias(self.cesantias)

        def obtener_id_cesantias(event):
            cesantias_seleccionado = self.cesantias.get()
            if cesantias_seleccionado in ids_cesantias:
                self.id_cesantias = ids_cesantias[cesantias_seleccionado]

        self.cesantias.bind("<<ComboboxSelected>>", obtener_id_cesantias)

        # quinta fila
        # Fondo_Pensiones
        frame_etiqueta_pensiones = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_pensiones.grid(row=4, column=0, padx=20, pady=5)
        self.etiqueta_pensiones = tk.Label(frame_etiqueta_pensiones, text="Fondo Pensiones ", font=('Roboto', 14),
                                           fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_pensiones.grid(row=4, column=0, padx=20, pady=5)
        self.pensiones = ttk.Combobox(frame_etiqueta_pensiones, font=('Roboto', 14), width=17)
        self.pensiones.grid(row=4, column=1, padx=10, pady=5)
        ids_pensiones = Fondo_Pensiones(self.pensiones)

        def obtener_id_pensiones(event):
            pensiones_seleccionado = self.pensiones.get()
            if pensiones_seleccionado in ids_pensiones:
                self.id_pensiones = ids_pensiones[pensiones_seleccionado]

        self.pensiones.bind("<<ComboboxSelected>>", obtener_id_pensiones)

        # fecha ingreso
        frame_etiqueta_fi = tk.Frame(panel_principal1, bg=COLOR_CUERPO_PRINCIPAL)
        frame_etiqueta_fi.grid(row=4, column=1, padx=20, pady=5)
        self.etiqueta_fi = tk.Label(frame_etiqueta_fi, text="Fecha ingreso", font=('Roboto', 14),
                                    fg="#222d33", bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        self.etiqueta_fi.grid(row=4, column=0, padx=20, pady=5)
        self.fecha_seleccionada = tk.StringVar()
        self.fecha_seleccionada.set(date.today())
        self.fecha_ingreso = ttk.Entry(frame_etiqueta_fi, font=('Roboto', 14),
                                       textvariable=self.fecha_seleccionada, state='readonly')
        self.fecha_ingreso.grid(row=4, column=1, padx=5, pady=5)
        self.boton_calendario = tk.Button(frame_etiqueta_fi, text='\uf073', font=font_awesome,
                                          command=self.mostrar_ocultar_calendario, bd=0, bg=COLOR_BARRA_SUPERIOR,
                                          fg="white")
        self.boton_calendario.grid(row=4, column=2, pady=5)

        self.selector_fechas = Calendar(frame_etiqueta_fi, font=('Roboto', 10), selectmode='day',
                                        date_pattern='yyyy-mm-dd',
                                        year=date.today().year, month=date.today().month, day=date.today().day,
                                        width=120, height=100)
        self.selector_fechas.grid_remove()
        self.selector_fechas.bind("<<CalendarSelected>>", self.actualizar_fecha)

        # sexta fila
        # boton guardar
        frame_boton_guardar = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        frame_boton_guardar.pack(side=tk.BOTTOM, fill='both', expand=True, pady=10)
        self.boton_guardar = tk.Button(frame_boton_guardar, text="Registrar empleado", bd=0,
                                       command=self.registrar_empleado, borderwidth=4, relief=tk.FLAT,
                                       overrelief=tk.FLAT)
        self.boton_guardar.config(fg="white", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR)
        self.boton_guardar.pack(padx=10, pady=10)

    def validate_input(self, new_value):
        # Verifica si la entrada es un número
        return new_value.isdigit() or new_value == ''

    def mostrar_ocultar_calendario(self):
        # Muestra u oculta el calendario cuando se presiona el botón
        if self.selector_fechas.winfo_ismapped():
            self.selector_fechas.grid_remove()
            self.boton_calendario.config(text='\uf073')
        else:
            self.selector_fechas.grid(row=4, column=2, padx=20, pady=5)
            self.boton_calendario.config(text='\uf073')

    def actualizar_fecha(self, event):
        # Actualiza el campo de texto con la fecha seleccionada en el calendario
        fecha_seleccionada = self.selector_fechas.get_date()
        self.fecha_seleccionada.set(fecha_seleccionada)
        self.selector_fechas.grid_remove()

    def registrar_empleado(self):
        datos_a_guardar = {
            'id_Ctabanco': self.cuenta.get(),
            'ID_banco': self.id_banco,
            'ID_TIPO_CUENTA': self.id_tcuenta
        }
        datos_empleado = {
            'Id_Cedula': self.cedula.get(),
            'Nombres': self.nombre.get(),
            'Apellidos': self.apellido.get(),
            'id_cargo': self.id_cargo,
            'id_dpto': self.id_DPTO,
            'Salario': self.salario.get(),
            'id_TipoCont': self.id_tipo_contrato,
            'id_Ctabanco': self.cuenta.get(),
            'Fecha_Ingreso': self.fecha_ingreso.get()
        }
        datos_cesantias = {
            'ID_Cedula': self.cedula.get(),
            'ID_fondo_C': self.id_cesantias
        }
        datos_eps = {
            'ID_Cedula': self.cedula.get(),
            'ID_EPS': self.ID_EPS
        }
        datos_pensiones = {
            'Id_Cedula': self.cedula.get(),
            'ID_pensiones': self.id_pensiones
        }
        exito = insertar_CuentaB_empleado(datos_a_guardar)
        if exito:
            exito2 = insertar_empleado(datos_empleado)
            if exito2:
                insertar_Cesantias_empleados(datos_cesantias)
                insertar_EPS_empleados(datos_eps)
                insertar_pensiones_empleados(datos_pensiones)
                self.registrar_descuentos()
                self.registrar_devengados()
                messagebox.showinfo("Registro Exitoso", "Empleado registrado correctamente en la base de datos")
                self.cedula.delete(0, tk.END)
                self.nombre.delete(0, tk.END)
                self.apellido.delete(0, tk.END)
                self.salario.delete(0, tk.END)
                self.cuenta.delete(0, tk.END)
                self.fecha_ingreso.delete(0, tk.END)
                self.pensiones.set('')
                self.bancos.set('')
                self.tipocontra.set('')
                self.EPS.set('')
                self.tcuenta.set('')
                self.area.set('')
                self.cesantias.set('')
                self.cargos.set('')
            else:
                messagebox.showerror("Error", "Hubo un problema al intentar registrar el empleado en la base de datos")
        else:
            messagebox.showwarning("Cuenta no registrada", "Cuenta bancaria ya registrada para otro empleado, por favor valida la información")

    def registrar_descuentos(self):
        valorporcentaje = random.randint(0, 10)
        porcentajeFondoE = valorporcentaje / 100

        valorSalario = self.salario.get()
        self.valor_Salud = float(valorSalario) * self.porcentaje_salud
        self.valor_Pension = float(valorSalario) * self.porcentaje_pension

        if int(valorSalario) < 2577400:
            self.valor_Fdo_Sol = 0
        elif int(valorSalario) > 2577400:
            self.valor_Fdo_Sol = float(valorSalario) * 0.01
        elif 17600000 < int(valorSalario) < 18700000:
            self.valor_Fdo_Sol = float(valorSalario) * 0.012
        elif 18700000 < int(valorSalario) < 19800000:
            self.valor_Fdo_Sol = float(valorSalario) * 0.014
        elif 19800000 < int(valorSalario) < 20900000:
            self.valor_Fdo_Sol = float(valorSalario) * 0.016
        elif 20900000 < int(valorSalario) < 22000000:
            self.valor_Fdo_Sol = float(valorSalario) * 0.018
        elif int(valorSalario) > 22000000:
            self.valor_Fdo_Sol = float(valorSalario) * 0.02
        self.valor_Bancos = 0
        self.valor_Fondo_de_Empleados = float(valorSalario) * porcentajeFondoE

        datos_descuentos = {
            'Eps_Salud': self.valor_Salud,
            'Pension': self.valor_Pension,
            'Fdo_Sol': self.valor_Fdo_Sol,
            'Bancos': self.valor_Bancos,
            'Fondo_de_Empleados': self.valor_Fondo_de_Empleados,
            'ID_Personal': self.cedula.get()
        }
        insertar_descuentos(datos_descuentos)

    def registrar_devengados(self):
        salario = self.salario.get()
        if int(salario) < 2200000:
            self.subsitrans = self.Sub_Tpte
        else:
            self.subsitrans = 0
        datos_devengados = {
            'Salario': self.salario.get(),
            'Sub_Tpte': self.subsitrans,
            'Gastos_Rep': 0,
            'Sobresueldo': 0,
            'Viaticos': 0,
            'Comisiones': 0,
            'Primas_Pago_extras': 0,
            'ID_empleado': self.cedula.get()
        }
        insertar_devengados(datos_devengados)


