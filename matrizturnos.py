turnos = [
    ["libre", "ocupado", "libre"],  # el de las 10am
    ["ocupado", "libre", "libre"],  # el de las 12pm
    ["libre", "libre", "ocupado"]   # el de las 14pm
]

servicios =[
    ["", "Kapping", ""],
    ["Semi", "", ""],
    ["", "", "SoftGel"]
]

horarios = ["10:00", "12:00", "14:00"]
profesionales= ["Lucrecia", "Camila", "Juana"]
tipos_servicios = ["SoftGel", "Kapping", "Semi"]


print("agenda de turnos:")
print("Hora  | Lucrecia | Camila  |Juana ")
for i in range(len(turnos)):
    linea = ""
    for j in range(len(turnos[i])):
        if turnos[i][j] == "ocupado":
            linea += f"{turnos[i][j]} ({servicios[i][j]:7}) | "
        else:
             linea += f"{turnos[i][j]:14} | "
    print(f"{horarios[i]} |  {linea}")
    
print("\nElige un horario:")
for idx, h in enumerate(horarios):
    print(f"{idx} - {h}")
fila = int(input("Número de fila (0,1,2): "))

print("\nElige un profesional:")
for idx, p in enumerate(profesionales):
    print(f"{idx} - {p}")
columna = int(input("Número de columna (0,1,2): "))

if turnos[fila][columna] == "libre":
    print("\nTipos de servicio disponibles:")
    for s in tipos_servicios:
        print("-", s)
    servicio = input("Ingresa SoftGel, Kapping o Semi: ")
    if servicio in tipos_servicios:
        turnos[fila][columna] = "ocupado"
        servicios[fila][columna] = servicio
        print(f"\n✔ Turno reservado con {profesionales[columna]} a las {horarios[fila]} para {servicio}")
    else:
        print("\n✘ Servicio no válido. No se reservó.")
else:
    print("\n✘ Este turno ya está ocupado.")
    
print("\nAgenda actualizada:")
print("Hora  |  Lucrecia       |  Camila         |  Juana")
for i in range(len(turnos)):
    linea = ""
    for j in range(len(turnos[i])):
        if turnos[i][j] == "ocupado":
            linea += f"{turnos[i][j]} ({servicios[i][j]:7}) | "
        else:
            linea += f"{turnos[i][j]:14} | "
    print(f"{horarios[i]} |  {linea}")
    