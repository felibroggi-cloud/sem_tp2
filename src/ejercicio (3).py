review = """La película sigue a un grupo de astronautas que viajan a Marte en una misión de rescate. 
El capitán Torres lidera al equipo a través de tormentas solares y fallos en el sistema de navegación. 
Al llegar a Marte descubren que la base está abandonada y los suministros destruidos. 
Torres decide sacrificar la nave nodriza para salvar al equipo y logran volver a la Tierra en una cápsula de emergencia.
El final revela que Torres sobrevivió gracias a un pasaje secreto."""


entrada = input ("Ingrese las palabras spoiler (separadas por coma): ")
temp = ""
for letter in entrada:
    if letter != ",":
        temp += letter
    else:
        temp += " "

palabras_spoiler = temp.split()


new_review = ""
for palabra in review.split():
    cond = False
    for i in range(len(palabras_spoiler)):
        if palabra.lower() == palabras_spoiler[i].lower():
            cond = True
            break
    if cond:
        entrada = ""
        for i in range(len(palabra)):
            entrada += "*"
    else:
        entrada = palabra
    new_review += entrada + " "

print (new_review)