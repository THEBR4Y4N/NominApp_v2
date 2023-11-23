from formularios.form_principal import FormPrincipal
from database import estartableconnexion

conexion = estartableconnexion()
app = FormPrincipal(conexion)
app.mainloop()
