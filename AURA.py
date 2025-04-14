import json

# Cargar las reservas desde el archivo JSON (si existe)
def cargar_reservas():
    try:
        with open('reservas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Guardar las reservas en el archivo JSON
def guardar_reservas(reservas):
    with open('reservas.json', 'w') as file:
        json.dump(reservas, file, indent=4)

# Mostrar la disponibilidad para un día específico
def mostrar_disponibilidad(reservas, fecha):
    horarios = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']
    disponibles = [hora for hora in horarios if hora not in reservas.get(fecha, {})]
    return disponibles

# Realizar una reserva
def reservar_turno(reservas, fecha, hora, cliente, profesional):
    if fecha not in reservas:
        reservas[fecha] = {}
    
    if hora in reservas[fecha]:
        print(f"El turno a las {hora} ya está reservado.")
    else:
        reservas[fecha][hora] = {'cliente': cliente, 'profesional': profesional}
        print(f"Reserva realizada con éxito para {cliente} con {profesional} a las {hora} el {fecha}.")

# Buscar una reserva por cliente, fecha o profesional
def buscar_reserva(reservas, busqueda):
    encontrados = []
    for fecha, horarios in reservas.items():
        for hora, datos in horarios.items():
            if busqueda.lower() in datos['cliente'].lower() or busqueda.lower() in datos['profesional'].lower() or busqueda == fecha:
                encontrados.append(f"{busqueda} - {datos['cliente']} con {datos['profesional']} a las {hora} el {fecha}")
    return encontrados

# Menú interactivo
def menu():
    reservas = cargar_reservas()
    
    while True:
        print("\nSistema de Reservas - Estudio de Uñas")
        print("1. Ver disponibilidad de turnos")
        print("2. Realizar una reserva")
        print("3. Buscar reserva")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ")

        if opcion == '1':
            fecha = input("Ingresa la fecha (formato YYYY-MM-DD): ")
            disponibles = mostrar_disponibilidad(reservas, fecha)
            if disponibles:
                print(f"Horarios disponibles en {fecha}: {', '.join(disponibles)}")
            else:
                print(f"No hay horarios disponibles para el {fecha}.")
        
        elif opcion == '2':
            fecha = input("Ingresa la fecha (formato YYYY-MM-DD): ")
            hora = input("Ingresa la hora (formato HH:00): ")
            cliente = input("Nombre del cliente: ")
            profesional = input("Nombre del profesional: ")
            reservar_turno(reservas, fecha, hora, cliente, profesional)
            guardar_reservas(reservas)
        
        elif opcion == '3':
            busqueda = input("Buscar por cliente, fecha o profesional: ")
            resultados = buscar_reserva(reservas, busqueda)
            if resultados:
                print("Resultados encontrados:")
                for reserva in resultados:
                    print(reserva)
            else:
                print("No se encontraron reservas.")
        
        elif opcion == '4':
            print("¡Gracias por usar el sistema de reservas!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
