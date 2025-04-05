import pyodbc

# Configuración de la conexión
SERVER = "cristhian\\SQLEXPRESS"  # Cambia si usas un servidor diferente
DATABASE = "banda_musical"
USER = "andrea_valentina"  # Si usas autenticación de SQL Server
PASSWORD = "andreavalentina1701"  # Asegúrate de poner tu contraseña
DRIVER = "{SQL Server}"  # Para Windows
# DRIVER = "{ODBC Driver 17 for SQL Server}"  # Para versiones modernas

# Conectar a la base de datos
try:
    conexion = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USER};PWD={PASSWORD}")
    print("✅ Conexión exitosa a SQL Server")
except Exception as e:
    print(f"❌ Error conectando a SQL Server: {e}")
    exit()

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Consultar la información de los integrantes
consulta_sql = "SELECT * FROM integrantes;"
cursor.execute(consulta_sql)

# Obtener los resultados
integrantes = cursor.fetchall()

# Mostrar los resultados
print("\n🎶 Lista de Integrantes de la Banda:")
for integrante in integrantes:
    print(f"ID: {integrante.id}, Nombre: {integrante.nombre}, Instrumento: {integrante.instrumento}, "
          f"Seguidores: {integrante.seguidores}, Conciertoss: {integrante.conciertoss}, "
          f"Ganancias Totales: ${integrante.ganancias_totales}")

# Cerrar la conexión
cursor.close()
conexion.close()
print("\n🔌 Conexión cerrada.")

