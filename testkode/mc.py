## Oppgave 1

# Nivå 1: Forklare

# random() lager en tilfeldig desimalverdi mellom 0 og 1
from random import random

antall_piler = 10000

på_sirkelen = 0
utenfor_sirkelen = 0

for pil in range(antall_piler):
    # for å få tilfeldige verdier mellom -1 og 1:
    x = 2*random() - 1
    y = 2*random() - 1

    if (x**2 + y**2) <= 1**2:
        på_sirkelen += 1
    else:
        utenfor_sirkelen += 1

andel_på_sirkelen = på_sirkelen / (på_sirkelen + utenfor_sirkelen)

areal_kvadrat = 2 * 2
areal_sirkel = andel_på_sirkelen * areal_kvadrat

print(f"Areal av sirkelen: {areal_sirkel} kvadratmeter")

# Nivå 2: Puslespill

# TODO: Nettsiden virker ikke lenger? Videresendes til noe helt annet?

# Nivå 3: Feilsøking

# random() lager en tilfeldig desimalverdi mellom 0 og 1
from random import random

antall_piler = 10000

på_sirkelen = 0
utenfor_sirkelen = 0

for pil in range(antall_piler):
    # for å få tilfeldige verdier mellom -1 og 1:
    x = 2*random() - 1
    y = 2*random() - 1

    if x + y <= 1:
        på_sirkelen += 1
    else:
        utenfor_sirkelen += 1

andel_på_sirkelen = på_sirkelen / utenfor_sirkelen

areal_kvadrat = 2 * 2
areal_sirkel = areal_kvadrat / andel_på_sirkelen

print("Areal av sirkelen:", areal_sirkel, "kvadratmeter")

# Nivå 4: Fyll inn

# random() lager en tilfeldig desimalverdi mellom 0 og 1
from random import random

antall_piler = 10000

på_sirkelen = # fyll inn
utenfor_sirkelen = # fyll inn

for pil in range(antall_piler):
    # for å få tilfeldige verdier mellom -1 og 1:
    x = # fyll inn
    y = # fyll inn

    if # fyll inn
        på_sirkelen += 1
    else:
        utenfor_sirkelen += 1

andel_på_sirkelen = på_sirkelen / (på_sirkelen + utenfor_sirkelen)

areal_kvadrat = 2 * 2
areal_sirkel = # fyll inn

print("Areal av sirkelen:", areal_sirkel, "kvadratmeter")