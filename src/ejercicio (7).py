import random

amigos_string = input ("Ingrese los nombres (separados por coma): ")
print ()

for char in amigos_string:
    if char == " ":
        amigos_string = amigos_string.replace(char, "")

amigos = amigos_string.lower().split(",")

if len(amigos) < 3:
    print ("ERROR: Debe haber al menos 3 participantes.")
else:
    dupe = False
    for amigo in amigos:
        if amigos.count(amigo) > 1:
            print ("ERROR: No debe haber nombres duplicados.")
            dupe = True
            break
    if not dupe:
        amigos = random.sample(amigos, len(amigos))
        asignaciones = []
        i = 0

        for i in range(len(amigos) - 2):
            asignaciones.append([amigos[i], amigos[i+1]])
        asignaciones.append([amigos[-1], amigos[0]])

        asignaciones_string = []
        for asignacion in asignaciones:
            asignaciones_string.append(f"{asignacion[0].capitalize()} -> {asignacion[1].capitalize()}")
        
        # Desordena la lista de asignaciones para que parezca mas mesclado
        # asignaciones_string = random.sample (asignaciones_string, len(asignaciones_string)) 

        print ("Sorteo de amigo invisible")
        for asignacion in asignaciones_string:
            print (asignacion)
        