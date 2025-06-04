movimientos = ["piedra", "papel", "tijeras"]
jugador = input("Elige tu movimiento (piedra, papel o tijeras): ")
import random
computadora = random.choice(movimientos)
print("La computadora eligió:", computadora)
if jugador == computadora:
    print("¡Empate!")
elif jugador == "piedra":
    if computadora == "tijeras":
        print("¡Ganaste!")
    else:
        print("Perdiste :(")
elif jugador == "papel":
    if computadora == "piedra":
        print("¡Ganaste!")
    else:
        print("Perdiste :(")
elif jugador == "tijeras":
    if computadora == "papel":
        print("¡Ganaste!")
    else:
        print("Perdiste :(")
else:
    print("Movimiento no válido.")
