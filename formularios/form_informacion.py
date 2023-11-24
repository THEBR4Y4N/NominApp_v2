import tkinter as tk
import util.util_ventana as util_ventana


class FormInformacion(tk.Toplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        self.title('NominApp')
        self.iconbitmap("./imagenes/icono.ico")
        w, h = 400, 50
        util_ventana.centrar_ventana(self, w, h)

    def contruirWidget(self):
        self.label_Version = tk.Label(self, text="Version : 1.0.2")
        self.label_Version.config(fg="#000000", font=("Roboto", 15), pady=10, width=20)
        self.label_Version.pack()
