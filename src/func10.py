def print_table (players):
    print (f"{'Cocinero':15}{'Puntaje':11}{'Rondas ganadas':18}{'Mejor ronda':14}Promedio")
    print (f"{"-" * 66}")
    for player in sorted(players, key=lambda x: x["Puntaje"], reverse = True):
        impresion = f"{player["Nombre"]:15}"
        expresion = f"{str(player["Puntaje"])}({str(player["Ronda actual"])})"
        impresion += f"{expresion:11}"
        impresion += f"{str(player["Rondas ganadas"]):18}"
        impresion += f"{str(player["Mejor ronda"]):14}"
        impresion += str(player["Promedio"])
        print (impresion)

def update_players (players, rj, jueces):
    for player in players:
        nombre = player["Nombre"]
        puntos = 0
        for juez in jueces[nombre]: puntos += jueces[nombre][juez]
        player["Puntaje"] += puntos
        player["Ronda actual"] = puntos
        if player["Mejor ronda"] < puntos: player["Mejor ronda"] = puntos
        player["Promedio"] = round(player["Puntaje"] / rj, 1)

def print_winner (players):
    max = -1
    for player in players:
        curr = player["Ronda actual"]
        if curr > max:
            max = curr
            winner = player
    winner ["Rondas ganadas"] += 1
    print (f"  Ganador/a: {winner["Nombre"]}({max} pts)")
    print ()