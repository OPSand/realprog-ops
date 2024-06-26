hjemmelag = ["Bodø/Glimt", "Brann", "Fredrikstad", "HamKam", "Haugesund", "KFUM Oslo", "Kristiansund", "Lillestrøm"]
bortelag = ["Molde", "Odd", "Rosenborg", "Sandefjord", "Sarpsborg 08", "Strømsgodset", "Tromsø", "Viking"]
bindestrek = " - "

antall_lag = len(hjemmelag) + len(bortelag)     # antar at listene er like lange
antall_kamper_per_runde = int(antall_lag / 2)   # hver kamp inneholder 2 lag
                                                # (divisjon gir desimaltall, så gjør om til heltall etterpå)
antall_runder = (antall_lag - 1)*2              # Hvert lag møter alle lag (untatt seg selv) 2 ganger (én hjemme, én borte)

# Legg til kamper i rundene (alle endringer du trenger å gjøre vil skje i denne løkken)
runder = [] # ytre liste (alle rundene med kamper)
for r in range(antall_runder):
    runde = [] # indre liste (alle kampene i én runde)
    for k in range(antall_kamper_per_runde):
        kamp = hjemmelag[k] + bindestrek + bortelag[k]
        runde.append(kamp) # legg til kamp i indre liste
    runder.append(runde) # legg til runde i ytre liste

# Legg til kamper i rundene (alle endringer du trenger å gjøre vil skje i denne løkken)
runder = [] # ytre liste (alle rundene med kamper)
for r in range(antall_runder):
    runde = [] # indre liste (alle kampene i én runde)
    for k in range(antall_kamper_per_runde):
        kamp = hjemmelag[k] + bindestrek + bortelag[k]
        runde.append(kamp) # legg til kamp i indre liste
    runder.append(runde) # legg til runde i ytre liste
    # Oppgave 1: Roter listene ved å flytte lag mellom dem (først uten å fjerne)
    første_bortelag = bortelag.pop(0)
    hjemmelag.insert(0, første_bortelag)
    siste_hjemmelag = hjemmelag.pop()
    bortelag.append(siste_hjemmelag)

# Legg til kamper i rundene (alle endringer du trenger å gjøre vil skje i denne løkken)
runder = [] # ytre liste (alle rundene med kamper)
for r in range(antall_runder):
    runde = [] # indre liste (alle kampene i én runde)
    for k in range(antall_kamper_per_runde):
        kamp = hjemmelag[k] + bindestrek + bortelag[k]
        runde.append(kamp) # legg til kamp i indre liste
    runder.append(runde) # legg til runde i ytre liste
    # Oppgave 1: Roter listene ved å flytte lag mellom dem (først uten å fjerne)
    # Oppgave 2: Hold ett lag (Bodø/Glimt) statisk
    første_bortelag = bortelag.pop(0)
    hjemmelag.insert(1, første_bortelag)
    siste_hjemmelag = hjemmelag.pop()
    bortelag.append(siste_hjemmelag)

# Legg til kamper i rundene (alle endringer du trenger å gjøre vil skje i denne løkken)
runder = [] # ytre liste (alle rundene med kamper)
for r in range(antall_runder):
    runde = [] # indre liste (alle kampene i én runde)
    for k in range(antall_kamper_per_runde):
        # Oppgave 3: Bytt om på hjemme og borte i partallsrunder
        if (r + 1) % 2 == 0:
            kamp = bortelag[k] + bindestrek + hjemmelag[k]
        else:
            kamp = hjemmelag[k] + bindestrek + bortelag[k]
        runde.append(kamp) # legg til kamp i indre liste
    runder.append(runde) # legg til runde i ytre liste
    # Oppgave 1: Roter listene ved å flytte lag mellom dem (først uten å fjerne)
    # Oppgave 2: Hold ett lag (Bodø/Glimt) statisk
    første_bortelag = bortelag.pop(0)
    hjemmelag.insert(1, første_bortelag)
    siste_hjemmelag = hjemmelag.pop()
    bortelag.append(siste_hjemmelag)
    
# Skriv ut terminlisten når den er ferdig
for r in range(antall_runder):
    print()
    print("Runde", (r + 1), ":")
    print()
    for k in range(antall_kamper_per_runde):
        print(runder[r][k]) # (første indeks er ytre liste, andre indeks er indre liste)
print()

# Tell hvor mange ganger lagene møtte hverandre
alle_lag = hjemmelag + bortelag
kampteller = []
for hi in range(antall_lag):
    kampteller.append([])
    for bi in range(antall_lag):
        kampteller[hi].append(0)

for r in range(antall_runder):
    for k in range(antall_kamper_per_runde):
        kamp = runder[r][k]
        hjemmelag, bortelag = kamp.split(bindestrek)
        hi = alle_lag.index(hjemmelag)
        bi = alle_lag.index(bortelag)
        kampteller[hi][bi] += 1 # øk med 1

# Skriv ut hvor mange ganger lagene møtte hverandre
print("Antall kamper - rader er hjemmelag og kolonner bortelag.")
print("Målet er å til slutt få 0 på diagonalen og 1 overalt ellers:")
print()
for hi in range(antall_lag):
    print(kampteller[hi])
print()