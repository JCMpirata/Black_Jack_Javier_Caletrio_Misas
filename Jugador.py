
from random import choice, sample
print("Las puntuaciones de cada carta son las siguentes", end = ":")
print("\n")
    
baraja_poker = {

        #Picas
        chr(0x1f0a1): 11,
        chr(0x1f0a2): 2,
        chr(0x1f0a3): 3,
        chr(0X1f0a4): 4,
        chr(0x1f0a5): 5,
        chr(0x1f0a6): 6,
        chr(0x1f0a7): 7,
        chr(0x1f0a8): 8,
        chr(0x1f0a9): 9,
        chr(0x1f0a0): 10,
        chr(0x1f0aa): 10,
        chr(0x1f0ab): 10,
        chr(0x1f0ac): 10,

        #Corazones
        chr(0x1f0b1): 11,
        chr(0x1f0b2): 2,
        chr(0x1f0b3): 3,
        chr(0X1f0b4): 4,
        chr(0x1f0b5): 5,
        chr(0x1f0b6): 6,
        chr(0x1f0b7): 7,
        chr(0x1f0b8): 8,
        chr(0x1f0b9): 9,
        chr(0x1f0b0): 10,
        chr(0x1f0ba): 10,
        chr(0x1f0bb): 10,
        chr(0x1f0bc): 10,

        #Treboles
        chr(0x1f0c1): 11,
        chr(0x1f0c2): 2,
        chr(0x1f0c3): 3,
        chr(0X1f0c4): 4,
        chr(0x1f0c5): 5,
        chr(0x1f0c6): 6,
        chr(0x1f0c7): 7,
        chr(0x1f0c8): 8,
        chr(0x1f0c9): 9,
        chr(0x1f0c0): 10,
        chr(0x1f0ca): 10,
        chr(0x1f0cb): 10,
        chr(0x1f0cc): 10,

        # Rombos
        chr(0x1f0d1): 11,
        chr(0x1f0d2): 2,
        chr(0x1f0d3): 3,
        chr(0X1f0d4): 4,
        chr(0x1f0d5): 5,
        chr(0x1f0d6): 6,
        chr(0x1f0d7): 7,
        chr(0x1f0d8): 8,
        chr(0x1f0d9): 9,
        chr(0x1f0d0): 10,
        chr(0x1f0da): 10,
        chr(0x1f0db): 10,
        chr(0x1f0dc): 10
    }
    
for cartas, valores in baraja_poker.items():
    print("La carta {} vale {} puntos".format(cartas, valores))

lista_baraja = list(baraja_poker)

def jugador():
    cartas_jugador = sample(lista_baraja, 2)
    puntuacion_jugador = lista_baraja[cartas_jugador]
    print("Ha sacado las cartas {} {} con una puntuacion de {}".format(cartas_jugador[0], cartas_jugador[1], puntuacion_jugador))
    return cartas_jugador

print(jugador())

def banca():
    cartas_banca = sample(lista_baraja, 2)
    puntuacion_banca = lista_baraja[cartas_banca]
    print("La banca ha sacado las cartas {} {} con una puntuacion de {}".format(cartas_banca[0], cartas_banca[1], puntuacion_banca))
    return cartas_banca

print(banca())



    


        
    



