empleados = [                        
        ["Juan Pérez", 8, 8, 8, 8, 8],
        ["Luis López", 12, 8, 9, 8, 9],
        ["Andrés Rojas", 8, 6, 6, 9, 7],
        ["Marcos Piñeros", 12, 12, 12, 12, 12]
    ]

def suma_horas(empleado):
    total = empleado[1] + empleado[2] + empleado[3] + empleado[4] + empleado[5]
    return total

def clasificar_jornada(total):
    if total <= 40:    
        return("Jornada estándar")
    else:
        return("Sobretiempo")
    
for empleado in empleados:
    total = suma_horas(empleado)
    jornada = clasificar_jornada(total)
    nombre = empleado[0]
    print(nombre, "trabajó", total, " horas esta semana. Su jornada fue: ", jornada)