---
title: "Unique digits addition - GPT OSS cleaned"
language: "de"
slug: "gpt-oss-cleaned"
aliases:
  - "/wiki/Unique_digits_addition_-_GPT_OSS_cleaned"
build:
  list: never

---

def ok(a, b, c):
        digits = str(a) + str(b) + str(c)
        return len(set(digits)) == len(digits)

    solutions = set()

    MAX = 10_000
    for a in range(1, MAX):
        for b in range(a, MAX):
            c = a + b
            if ok(a, b, c):
            print(f"{a} + {b} = {c}")
                solutions.add((a, b, c))

    print("Number of solutions:", len(solutions))
