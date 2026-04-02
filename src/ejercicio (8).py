msg = input ("Ingrese un mensaje: ")
desp = int(input ("Ingrese el desplazamiento: "))

import string
minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase

msg_encriptado = ""
for letra in msg:
    if minusculas.__contains__(letra):
        i = minusculas.find(letra)
        i += desp
        if i >= len(minusculas):
            i -= len(minusculas)
        elif i < 0:
            i += len(minusculas)
        msg_encriptado += minusculas[i]
    elif mayusculas.__contains__(letra):
        i = mayusculas.find(letra)
        i += desp
        if i >= len(mayusculas):
            i -= len(mayusculas)
        msg_encriptado += mayusculas[i]
    else: msg_encriptado += letra

print (f"Mensaje cifrado: {msg_encriptado}")

msg_resuelto = ""
for letra in msg_encriptado:
    if minusculas.__contains__(letra):
        i = minusculas.find(letra)
        i -= desp
        if i >= len(minusculas):
            i -= len(minusculas)
        elif i < 0:
            i += len(minusculas)
        msg_resuelto += minusculas[i]
    elif mayusculas.__contains__(letra):
        i = mayusculas.find(letra)
        i -= desp
        if i >= len(mayusculas):
            i -= len(mayusculas)
        msg_resuelto += mayusculas[i]
    else: msg_resuelto += letra

print (f"Mensaje descifrado: {msg_resuelto}")