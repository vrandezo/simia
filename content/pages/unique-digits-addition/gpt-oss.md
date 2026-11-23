---
title: "Unique digits addition - GPT OSS"
language: "de"
slug: "gpt-oss"
aliases:
  - "/wiki/Unique_digits_addition_-_GPT_OSS"
build:
  list: never

---

    # ------------------------------------------------------------
    # Python‑3‑Programm, das die 45 gültigen Gleichungen erzeugt
    # ------------------------------------------------------------
    import itertools
    def digits_used(n):
        """liefert die Menge der Ziffern von n als Tupel (ohne führende Nullen)"""
        return tuple(str(n))
    def ok(a, b, c):
        # keine führende Null
        if str(a)[0] == '0' or str(b)[0] == '0' or str(c)[0] == '0':
            return False
        # Summe muss passen
        if a + b != c:
            return False
        # alle Ziffern höchstens einmal
        all_digits = digits_used(a) + digits_used(b) + digits_used(c)
        return len(set(all_digits)) == len(all_digits)
    solutions = set()
    # Wir probieren alle Aufteilungen der Ziffern 0‑9 in drei (nicht‑leere) Mengen.
    # Das ist äquivalent dazu, alle Tripel (a,b,c) im Bereich 1 … 9999 zu testen.
    for a in range(1, 10000):
        for b in range(a, 10000):          # b ≥ a → keine Doppelzählung von a↔b
            c = a + b
            if c > 9999:        # 5‑stellige Ergebnisse sind erlaubt (z. B. 246+789=1035)
                continue
            if ok(a, b, c):
                # Wir speichern die Gleichung in kanonischer Form (kleineres Addend zuerst)
                solutions.add((a, b, c))
    # Ausgabe
    solutions = sorted(solutions, key=lambda t: t[2])   # nach c sortieren
    print(f"Anzahl gültiger (ungeordneter) Aufgaben: {len(solutions)}")
    for a, b, c in solutions:
        print(f"{a} + {b} = {c}")
