# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import font
from config import (
    COLOR_BARRA_SUPERIOR,
    COLOR_MENU_LATERAL,
    COLOR_MENU_CURSOR_ENCIMA,
    COLOR_CUERPO_PRINCIPAL
)
import util.util_ventana as util_ventana
import util.uitl_imagenes as util_imagen
from formularios.form_informacion import FormInformacion
from formularios.form_construccion import Formulario_construccion
from formularios.form_dashboard import Form_Dashboard
from formularios.Form_empleados import Form_Empleados
from formularios.Form_Registro_empleado import Registrar_empleado
from formularios.Form_nominas import nominas


class FormPrincipal(tk.Tk):

    def __init__(self, conexion, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conexion = conexion
        if self.conexion:
            print("¡Conexión a la base de datos establecida correctamente!")
        else:
            print("¡No se pudo establecer la conexión a la base de datos!")

        self.perfil = util_imagen.leer_imagen("./imagenes/perfil.png", (100, 100))
        self.img_sitio_construccion = util_imagen.leer_imagen("./imagenes/construccion.png", (800, 600))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        self.title('NominApp')
        self.iconbitmap("./imagenes/icono.ico")
        self.config(bg="#FFF")
        w, h = 1450, 768
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=200)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)
        self.label_titulo = tk.Label(self.barra_superior, text="NominApp")
        self.label_titulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.label_titulo.pack(side=tk.LEFT)
        self.boton_menu_lateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                            command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.boton_menu_lateral.pack(side=tk.LEFT)
        self.label_Titulo = tk.Label(
            self.barra_superior, text="2023")
        self.label_Titulo.config(fg="#fff", font=(
            "Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.label_Titulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
        self.label_Perfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.label_Perfil.pack(side=tk.TOP, pady=10)

        self.buttonDashBoard = tk.Button(self.menu_lateral)
        self.buttonPersonal = tk.Button(self.menu_lateral)
        self.buttonNomina = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)
        self.buttonProfile = tk.Button(self.menu_lateral)
        self.buttonSettings = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Dashboard", "\uf109", self.buttonDashBoard, self.abrir_dashboard),
            ("Personal", "\uf03a", self.buttonPersonal, self.abrir_personal),
            ("Nominas", "\uf145", self.buttonNomina, self.abrir_nominasP),
            ("Perfil", "\uf007", self.buttonProfile, self.abrir_panel_construccion),
            ("Settings", "\uf013", self.buttonSettings, self.abrir_panel_construccion),
            ("Info", "\uf129", self.buttonInfo, self.abrir_panel_info)
        ]

        for text, icon, button, comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, comando)

        self.submenu_personal = tk.Menu(self.menu_lateral, tearoff=0, bg=COLOR_MENU_LATERAL, fg="white", bd=0,
                                        font=("Roboto", 20))
        self.submenu_personal.add_command(label="Ver personal", command=self.abrir_personal)
        self.submenu_personal.add_command(label="Agregar Personal", command=self.abrir_registro_empleados)
        self.buttonPersonal.config(command=self.abrir_submenu_personal)

    def abrir_submenu_personal(self):
        # Muestra el submenú "Personal" al hacer clic en el botón
        self.submenu_personal.post(self.buttonPersonal.winfo_rootx(),
                                   self.buttonPersonal.winfo_rooty() + self.buttonPersonal.winfo_height())

    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, text="NominApp",
                         font=("Roboto", 30), bg="#fff")
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                      command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def abrir_panel_info(self):
        FormInformacion()

    def abrir_panel_construccion(self):
        self.limpiar_panel(self.cuerpo_principal)
        Formulario_construccion(self.cuerpo_principal, self.img_sitio_construccion)

    def abrir_dashboard(self):
        self.limpiar_panel(self.cuerpo_principal)
        Form_Dashboard(self.cuerpo_principal)

    def abrir_personal(self):
        self.limpiar_panel(self.cuerpo_principal)
        Form_Empleados(self.cuerpo_principal)

    def abrir_registro_empleados(self):
        self.limpiar_panel(self.cuerpo_principal)
        Registrar_empleado(self.cuerpo_principal)

    def abrir_nominasP(self):
        self.limpiar_panel(self.cuerpo_principal)
        nominas(self.cuerpo_principal)

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
