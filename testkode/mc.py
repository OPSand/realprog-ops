## Oppgave 1

# Nivå 1: Forklare

from random import random

antall_piler = 10000

på_sirkelen = 0
utenfor_sirkelen = 0

for pil in range(antall_piler):
    # random lager en tilfeldig desimalverdi mellom 0 og 1
    x = 2*random()
    y = 2*random()

    if (x**2 + y**2) <= 1**2:
        pass # TODO: fullfør