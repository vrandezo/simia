---
title: "Unique digits addition - Denny"
language: "de"
slug: "denny"
aliases:
  - "/wiki/Unique_digits_addition_-_Denny"
build:
  list: never

---

    # iteriere ueber alle moeglichkeiten
    chrs = "1234567890+="

    loesungen = set()

    import itertools
    for i in itertools.permutations(list(chrs)):
        k = ''.join(i)
        for laenge in range(5, 13):
            kandidat = k[0:laenge]
            gleich = kandidat.find('=')
            if gleich == -1: continue
            plus = kandidat.find('+')
            if plus == -1: continue
            if plus > gleich: continue
            if (plus +1) == gleich: continue
            if plus == 0: continue
            if gleich == laenge-1: continue
            if kandidat[0] == '0': continue
            if kandidat[plus+1] == '0': continue
            if kandidat[gleich+1] == '0': continue
            zahl1 = int(kandidat[0:plus])
            zahl2 = int(kandidat[plus:gleich])
            zahl3 = int(kandidat[gleich+1:])
            if zahl1 + zahl2 != zahl3: continue
            loesungen.add(kandidat)
            # print(kandidat)
    print(len(loesungen))
