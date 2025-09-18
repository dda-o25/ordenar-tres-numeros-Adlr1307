"""
Andrés Enrique Jaime de la Rosa 763799
18/09/25
"""

# Entradas
primern = int(input("Escriba el primer número "))
segundon = int(input("Escriba el segundo número "))
tercern = int(input("Escriba el tercer número "))

# Proceso
if primern > segundon and primern> tercern:
    if segundon > tercern:
        print("Números ordenados:",primern,segundon,tercern)
    else:
        print("Números ordenados:",primern,tercern,segundon)
elif segundon > primern and segundon> tercern:
    if primern > tercern:
        print("Números ordenados:",segundon,primern,tercern)
    else:
        print("Números ordenados:",segundon,tercern,primern)
elif tercern > segundon and tercern> primern:
    if primern > segundon:
        print("Números ordenados:",tercern,primern,segundon)
    else:
        print("Números ordenados:",tercern,segundon,primern)

