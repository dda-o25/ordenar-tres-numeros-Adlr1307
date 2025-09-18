"""
Andrés Enrique Jaime de la Rosa 763799
18/09/25
"""

# Entradas
primern = int(input("Escriba el primer número "))
segundon = int(input("Escriba el segundo número"))
tercern = int(input("Escriba el tercer número "))

# Proceso
if primern >= segundon and primern>= tercern:
    if segundon >= tercern:
        print(primern,".*",segundon,".*",tercern,)
    else:
        print(primern,".*",tercern,".*",segundon)
elif segundon >= primern and segundon>= tercern:
    if primern >= tercern:
        print(segundon,".*",primern,".*",tercern)
    else:
        print(segundon,".*",tercern,".*",primern)
elif tercern >= segundon and tercern>= primern:
    if primern >= segundon:
        print(tercern,".*",primern,".*",segundon)
    else:
        print(tercern,".*",segundon,".*",primern)

