import tkinter as tk
import util.util_ventana as util_ventana


class FormInformacion(tk.Toplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config_window()
        self.contruirWidget()
        self.titulo = None
        self.sub = None
        self.label_Version = None
        self.label_autores = None
        self.label_autor1 = None
        self.label_autor2 = None
        self.label_autor3 = None

    def config_window(self):
        self.title('NominApp')
        self.iconbitmap("./imagenes/icono.ico")
        w, h = 400, 300
        util_ventana.centrar_ventana(self, w, h)

    def contruirWidget(self):
        self.titulo = self.titulo = tk.Label(self, text='NominApp')
        self.titulo.config(fg="#000000", font=("Roboto", 15), pady=10, width=20)
        self.titulo.pack()
        self.label_Version = tk.Label(self, text="Version : 1.0.5")
        self.label_Version.config(fg="#000000", font=("Roboto", 15), pady=10, width=20)
        self.label_Version.pack()
        self.sub = self.titulo = tk.Label(self, text='Autores:')
        self.sub.config(fg="#000000", font=("Roboto", 15), pady=10, width=20)
        self.sub.pack()
        self.label_autor1 = tk.Label(self, text="MARIA LUCIA GARCIA ")
        self.label_autor1.config(fg="#000000", font=("Roboto", 15), pady=10, width=20)
        self.label_autor1.pack()
        self.label_autor2 = tk.Label(self, text="ESTEFANIA MUÑOZ ")
        self.label_autor2.config(fg="#000000", font=("Roboto", 15), pady=10, width=20)
        self.label_autor2.pack()
        self.label_autor3 = tk.Label(self, text="BRAYAN GARZON")
        self.label_autor3.config(fg="#000000", font=("Roboto", 15), pady=10, width=20)
        self.label_autor3.pack()