"""
count - Itertools
"""

from itertools import count

contador = count(start=5, step=5)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break

    