---
title: "Unique digits addition - Markus"
language: "de"
slug: "markus"
aliases:
  - "/wiki/Unique_digits_addition_-_Markus"
build:
  list: never

---

    zeichen = "0123456789"

    import itertools
    i=0

    loesungen = set()

    for len1 in range(1,5):
        for len2 in range(1,5):
            for perm1 in itertools.permutations(list(zeichen),len1):
                rest = list(set(zeichen) - set(perm1))
                for perm2 in itertools.permutations(rest,len2):
                    #zahl1 = int(perm1[0] + perm1[1] + perm1[2])
                    zahl1 = int(''.join(perm1))
                    zahl2 = int(''.join(perm2))
                    #zahl2 = int(perm2[0] + perm2[1] + perm2[2])
                    ergebnis = zahl1 + zahl2
                    rest2 = set(rest) - set(perm2)
                    if len(set(f"{ergebnis}"))==len(f"{ergebnis}") and set(f"{ergebnis}").isdisjoint(set(perm1)) and set(f"{ergebnis}").isdisjoint(set(perm2)):
                        if not (zahl1,zahl2) in loesungen:
                            loesungen.add((zahl1,zahl2))
                            print(f"{zahl1} + {zahl2} = {ergebnis}")
                            i+=1

    print(i)
