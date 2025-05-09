import pyodbc

# Configuración de conexión
conexion = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=cristhian\\SQLEXPRESS;"
    "DATABASE=Banda_Musical;"
    "UID=andrea_valentina;"
    "PWD=andreavalentina1701"
)
cursor = conexion.cursor()

# Funciones del sistema

def mostrar_integrantes():
    cursor.execute("SELECT * FROM integrantes")
    for i in cursor.fetchall():
        print(f"\nID: {i.id}\nNombre: {i.nombre}\nInstrumento: {i.instrumento}\nSeguidores: {i.seguidores}\nConciertos: {i.conciertoss}\nGanancias: ${i.ganancias_totales:.2f}")


def agregar_seguidores():
    id = input("ID del integrante: ")
    cantidad = int(input("Cantidad a agregar: "))
    cursor.execute("UPDATE integrantes SET seguidores = seguidores + ? WHERE id = ?", (cantidad, id))
    conexion.commit()
    print("✅ Seguidores agregados.")

def quitar_seguidores():
    id = input("ID del integrante: ")
    cantidad = int(input("Cantidad a quitar: "))
    cursor.execute("UPDATE integrantes SET seguidores = CASE WHEN seguidores >= ? THEN seguidores - ? ELSE 0 END WHERE id = ?", (cantidad, cantidad, id))
    conexion.commit()
    print("✅ Seguidores quitados.")

def reiniciar_conciertos_y_ganancias():
    id = input("ID del integrante: ")
    cursor.execute("UPDATE integrantes SET conciertoss = 0, ganancias_totales = 0 WHERE id = ?", (id,))
    conexion.commit()
    print("✅ Datos reiniciados.")

def registrar_concierto():
    ganancia_total = float(input("Ganancia total del concierto: "))
    cursor.execute("SELECT COUNT(*) FROM integrantes")
    total_integrantes = cursor.fetchone()[0]
    ganancia_por_integrante = ganancia_total / total_integrantes
    cursor.execute("UPDATE integrantes SET conciertoss = conciertoss + 1, ganancias_totales = ganancias_totales + ?", (ganancia_por_integrante,))
    conexion.commit()
    print(f"✅ Concierto registrado. Cada integrante recibió ${ganancia_por_integrante:.2f}")

def total_seguidores():
    cursor.execute("SELECT SUM(seguidores) FROM integrantes")
    total = cursor.fetchone()[0]
    print(f"📊 Total de seguidores de la banda: {total}")

def promedio_ganancias():
    cursor.execute("SELECT AVG(ganancias_totales) FROM integrantes")
    promedio = cursor.fetchone()[0]
    print(f"📊 Promedio de ganancias por integrante: ${promedio:.2f}")

# Menú interactivo
while True:
    print("\n🎶 Menú del Sistema - Banda Musical")
    print("1. Ver integrantes")
    print("2. Agregar seguidores")
    print("3. Quitar seguidores")
    print("4. Reiniciar conciertos y ganancias")
    print("5. Registrar concierto")
    print("6. Consultar total de seguidores")
    print("7. Consultar promedio de ganancias")
    print("8. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        mostrar_integrantes()
    elif opcion == '2':
        agregar_seguidores()
    elif opcion == '3':
        quitar_seguidores()
    elif opcion == '4':
        reiniciar_conciertos_y_ganancias()
    elif opcion == '5':
        registrar_concierto()
    elif opcion == '6':
        total_seguidores()
    elif opcion == '7':
        promedio_ganancias()
    elif opcion == '8':
        break
    else:
        print("❌ Opción inválida, intenta nuevamente.")

# Cierre
cursor.close()
conexion.close()
print("🔌 Conexión cerrada.")
