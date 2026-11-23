---
title: "Unique digits addition - GPT OSS v2"
language: "de"
slug: "gpt-oss-v2"
aliases:
  - "/wiki/Unique_digits_addition_-_GPT_OSS_v2"
build:
  list: never

---

    # --------------------------------------------------------------
    #  Alle gültigen Gleichungen a + b = c  (a ≤ b, jedes Zeichen ≤1‑mal)
    # --------------------------------------------------------------
    import itertools
    def ok(a, b, c):
        # keine führende Null
        if str(a)[0] == '0' or str(b)[0] == '0' or str(c)[0] == '0':
            return False
        # richtige Summe
        if a + b != c:
            return False
        # alle Ziffern höchstens einmal
        digits = str(a) + str(b) + str(c)
        return len(set(digits)) == len(digits)
    solutions = set()
    # Obergrenze: 10 Ziffern → höchstens 5‑stellige Zahlen.
    # Wir gehen deshalb bis 99999 (5 Stellen) – das ist mehr als genug.
    MAX = 100_000
    for a in range(1, MAX):
        for b in range(a, MAX):          # b ≥ a → keine Doppelzählung
            c = a + b
            if c >= MAX:                 # c würde 6 Stellen brauchen → >10 Ziffern
                break
            if ok(a, b, c):
                solutions.add((a, b, c))
    print("Anzahl (ungeordnete) Lösungen :", len(solutions))
