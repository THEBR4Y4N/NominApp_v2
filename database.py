import pyodbc
from datetime import datetime


def estartableconnexion():
    server = 'root1201.database.windows.net'
    database = 'ProyectoFinal'
    username = 'admin1201'
    password = '@dmin1201'
    driver = '{ODBC Driver 17 for SQL Server}'
    conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        conn = pyodbc.connect(conn_str)
        return conn

    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None


def Reporte_personal_basico():
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = '''SELECT 
            Personal.Id_Cedula,Personal.Apellidos,Personal.Nombres,
            Cargo.Nombre AS Cargo,
            Departamento.Nombre as Area,
            TipoCont.Nombre as "Tipo Contrato",
            FORMAT(Personal.Salario, 'C0', 'es-CO') AS "Salario neto",
            Bancos.Banco,
            TipoCuenta.TIPO_CUENTA as "Tipo cuenta",
            Personal.id_Ctabanco as "Cuenta bancaria",
            EPS.Nombre_Eps AS EPS,
            Fondo_Cesantias.Nombre_Fondo_C as "Fondo Cesantias",
            Fondo_Pensiones.Nombre_Fondo as "Fondo Pensiones",
            FORMAT(Personal.Fecha_Ingreso, 'dd-MM-yyyy') AS "Fecha Ingreso"
            FROM 
            Personal
            INNER JOIN 
                Cargo ON Personal.id_cargo = Cargo.ID_cargo
            Inner join 
                Departamento on Departamento.Id_dpto = Personal.id_dpto
            Inner join 
                TipoCont on TipoCont.Id_TipoCont = Personal.id_TipoCont
            INNER JOIN 
                Ctabanco ON Personal.id_Ctabanco = Ctabanco.id_Ctabanco
            INNER JOIN 
                Bancos ON Ctabanco.ID_Banco = Bancos.ID_banco
            INNER JOIN 
                TipoCuenta ON Ctabanco.ID_Tipo_cuenta = TipoCuenta.ID_TIPO_CUENTA
            INNER JOIN 
                EPS_empleados ON EPS_empleados.ID_Cedula = Personal.Id_Cedula
            INNER JOIN 
                EPS ON EPS.ID_EPS = EPS_empleados.ID_EPS
            INNER JOIN 
                Cesantias_empleados ON Cesantias_empleados.ID_Cedula = Personal.Id_Cedula
            INNER JOIN 
                Fondo_Cesantias on Fondo_Cesantias.ID_fondo_C = Cesantias_empleados.ID_fondo_C
            INNER JOIN 
                Pensiones_empleado ON Pensiones_empleado.Id_Cedula = Personal.Id_Cedula
            INNER JOIN
                Fondo_Pensiones on Fondo_Pensiones.ID_fondo = Pensiones_empleado.ID_pensiones '''

        cursor.execute(query)
        rows = cursor.fetchall()
        rows = [list(map(str, row)) for row in rows]
        column_names = [column[0] for column in cursor.description]
        return rows, column_names
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return [], []


def Personal():
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from Personal"
        cursor.execute(query)
        rows = cursor.fetchall()
        rows = [list(map(str, row)) for row in rows]
        column_names = [column[0] for column in cursor.description]
        return rows, column_names
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return [], []


def TipoCuenta(combo):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from TipoCuenta"
        cursor.execute(query)
        valores_db = cursor.fetchall()
        opciones = [valor[1] for valor in valores_db]
        ids_tcuenta = {valor[1]: valor[0] for valor in valores_db}
        combo['values'] = opciones
        return ids_tcuenta
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return {}


def Bancos(combo):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from Bancos"
        cursor.execute(query)
        valores_db = cursor.fetchall()
        opciones = [valor[1] for valor in valores_db]
        ids_bancos = {valor[1]: valor[0] for valor in valores_db}
        combo['values'] = opciones
        return ids_bancos
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return {}


def Cargo(combo):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from Cargo"
        cursor.execute(query)
        valores_db = cursor.fetchall()
        opciones = [valor[1] for valor in valores_db]
        ids_cargo = {valor[1]: valor[0] for valor in valores_db}
        combo['values'] = opciones
        return ids_cargo
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return {}


def Departamento(combo):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from Departamento"
        cursor.execute(query)
        valores_db = cursor.fetchall()
        opciones = [valor[1] for valor in valores_db]
        ids_dpto = {valor[1]: valor[0] for valor in valores_db}
        combo['values'] = opciones
        return ids_dpto
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return {}


def TipoCont(combo):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from TipoCont"
        cursor.execute(query)
        valores_db = cursor.fetchall()
        opciones = [valor[1] for valor in valores_db]
        ids_tipocont = {valor[1]: valor[0] for valor in valores_db}
        combo['values'] = opciones
        return ids_tipocont
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return {}


def EPS(combo):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from EPS"
        cursor.execute(query)
        valores_db = cursor.fetchall()
        opciones = [valor[1] for valor in valores_db]
        ids_eps = {valor[1]: valor[0] for valor in valores_db}
        combo['values'] = opciones
        return ids_eps
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return {}


def Fondo_Cesantias(combo):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from Fondo_Cesantias"
        cursor.execute(query)
        valores_db = cursor.fetchall()
        opciones = [valor[1] for valor in valores_db]
        ids_cesantias = {valor[1]: valor[0] for valor in valores_db}
        combo['values'] = opciones
        return ids_cesantias
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return {}


def Fondo_Empleados(combo):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from Fondo_Cesantias"
        cursor.execute(query)
        valores_db = cursor.fetchall()
        opciones = [valor[1] for valor in valores_db]
        ids_f_empleados = {valor[1]: valor[0] for valor in valores_db}
        combo['values'] = opciones
        return ids_f_empleados
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return {}


def Fondo_Pensiones(combo):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from Fondo_Pensiones"
        cursor.execute(query)
        valores_db = cursor.fetchall()
        opciones = [valor[1] for valor in valores_db]
        ids_pensiones = {valor[1]: valor[0] for valor in valores_db}
        combo['values'] = opciones
        return ids_pensiones
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
        return {}


def Ctabanco():
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "select * from Ctabanco"
        cursor.execute(query)
        rows = cursor.fetchall()
        rows = [list(map(str, row)) for row in rows]
        column_names = [column[0] for column in cursor.description]
        return rows, column_names
    except Exception as e:
        print("Error al obtener datos desde la base de datos:", e)
    return [], []


def insertar_CuentaB_empleado(datos_cuenta):
    exito = False
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "INSERT INTO CtaBanco (id_Ctabanco, ID_banco, ID_TIPO_CUENTA) VALUES (%s, %s, %s)"
        valores = (datos_cuenta['id_Ctabanco'], datos_cuenta['ID_banco'], datos_cuenta['ID_TIPO_CUENTA'])
        queryi = query % valores
        cursor.execute(queryi)
        conn.commit()
        exito = True
    except Exception as error:
        print("Error al insertar cuenta:", error)
    return exito


def insertar_empleado(datos_empleado):
    exito2 = False
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = """INSERT INTO Personal (Id_Cedula, Nombres, Apellidos, id_cargo, id_dpto, Salario, id_TipoCont, id_Ctabanco, Fecha_Ingreso) VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, '%s')"""
        valores = (
            datos_empleado['Id_Cedula'], datos_empleado["Nombres"], datos_empleado["Apellidos"],
            datos_empleado['id_cargo'],
            datos_empleado['id_dpto'], datos_empleado['Salario'], datos_empleado['id_TipoCont'],
            datos_empleado['id_Ctabanco'], datos_empleado['Fecha_Ingreso'])
        queryi = query % valores
        cursor.execute(queryi)
        conn.commit()
        exito2 = True
    except Exception as error:
        print("Error al insertar cuenta:", error)
    return exito2


def insertar_Cesantias_empleados(datos_empleado):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "INSERT INTO Cesantias_empleados (ID_Cedula,ID_fondo_C) values (%s, %s)"
        valores = (datos_empleado['ID_Cedula'], datos_empleado['ID_fondo_C'])
        queryi = query % valores
        cursor.execute(queryi)
        conn.commit()
    except Exception as error:
        print("Error al insertar información en la tabla Cesantias_empleados:", error)


def insertar_EPS_empleados(datos_empleado):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "INSERT INTO EPS_empleados (ID_Cedula,ID_EPS) values (%s, %s)"
        valores = (datos_empleado['ID_Cedula'], datos_empleado['ID_EPS'])
        queryi = query % valores
        cursor.execute(queryi)
        conn.commit()
    except Exception as error:
        print("Error al insertar información en la tabla EPS_empleados:", error)


def insertar_pensiones_empleados(datos_empleado):
    try:
        conn = estartableconnexion()
        cursor = conn.cursor()
        query = "INSERT INTO Pensiones_empleado (Id_Cedula,ID_pensiones) values (%s, %s)"
        valores = (datos_empleado['Id_Cedula'], datos_empleado['ID_pensiones'])
        queryi = query % valores
        cursor.execute(queryi)
        conn.commit()
    except Exception as error:
        print("Error al insertar información en la tabla Pensiones_empleado:", error)
