---
title: "Unique digits addition - Markus v2"
language: "de"
slug: "markus-v2"
aliases:
  - "/wiki/Unique_digits_addition_-_Markus_v2"
build:
  list: never

---

    ## Create valid solutions by composing triples of two-digit additions,
    ## as they occur vertically in written addition. Distinguish cases by
    ## whether or not an incoming carry 1 is added, and whether the output
    ## produces such a carry for the next step.
    ##
    ## To print solutions, activated all commented-out print()'s below.

    triples_n_n = [] # no carry in, no carry out
    triples_n_c = [] # no carry in, carry out
    triples_c_n = [] # carry in, no carry out
    triples_c_c = [] # carry in, carry out
    for d1 in range(0,10):
        for d2 in range(0,10):
            if d1==d2: continue
            mask = (1<<d1) | (1<<d2)
            dsum = d1+d2
            if dsum >= 10:  # no carry in, carry out
                triples_n_c.append((mask | (1 << dsum-10), d1, d2))
            elif d1 != 0 and d2 != 0:  # no carry in, no carry out
                triples_n_n.append((mask | (1 << dsum), d1, d2))

            if dsum <= 8:  # carry in, no carry out
                triples_c_n.append((mask | (1 << dsum+1), d1, d2))
            elif d1 != 9 and d2 != 9: # carry in, carry out
                triples_c_c.append((mask | (1 << dsum-9), d1, d2))

    # Depth-first search composing triples from right to left.
    # Used-up digits are stored in agg_mask, carry is boolean, factor is a decimal shift factor (1, 10, 100, 1000).
    #
    # As triples are added to both numbers sychronously, they always have the same length. Other results (such as
    # 1965 + 78 = 2043) are created from shorter additions with leading carry (here 65 + 78 = 143) by pre-pending more
    # digits (here 19). This can only work if there is a leading carry, so this case is a bit lengthy.
    def dfs(agg_mask, carry, num1, num2, factor):
        solutions = 0

        if carry:
            if factor >= 10: # at least one digit picked
                if (agg_mask & 2) == 0: # valid result as is (0 not written, carry yields 1)
                    # print(f"{num1} + {num2} = {num1+num2}")
                    solutions += 1
                for i in range(1,9):
                    if (agg_mask & (3<<i)) == 0: # add leading digit 1..8 (check that result digit+1 is no dup)
                        # print(f"{num1+factor*i} + {num2} = {num1+num2+factor*i}")
                        # print(f"{num1} + {num2+factor*i} = {num1+num2+factor*i}")
                        solutions += 2
                if (agg_mask & (1|(1<<9))) == 0: # add leading digit 9 or leading x9 (check that 0 is no dup)
                    if (agg_mask & 2)==0: # add leading digit 9 (check that result 1 is no dup)
                        # print(f"{num1+factor*9} + {num2} = {num1+num2+factor*9}")
                        # print(f"{num1} + {num2+factor*9} = {num1+num2+factor*9}")
                        solutions += 2
                    for i in range(1,8): # add leading digit i9 (check that i and result i+1 is no dup), leading 8 is excluded since we already have 9
                        if (agg_mask & (3<<i)) == 0:
                            # print(f"{num1+factor*9+(factor*10)*i} + {num2} = {num1+num2+factor*9+(factor*10)*i}")
                            # print(f"{num1} + {num2+factor*9+(factor*10)*i} = {num1+num2+factor*9+(factor*10)*i}")
                            solutions += 2

            if factor >= 1000: return solutions # don't explore over 3-digit pairs

            next_factor = factor * 10
            for rec in triples_c_n:
                if rec[0] & agg_mask == 0:
                    solutions += dfs(rec[0]|agg_mask, False, num1 + rec[1] * factor, num2 + rec[2] * factor, next_factor)
            for rec in triples_c_c:
                if rec[0] & agg_mask == 0:
                    solutions += dfs(rec[0]|agg_mask, True, num1 + rec[1] * factor, num2 + rec[2] * factor, next_factor)
        else:
            if factor >= 10 and num1 >= factor//10 and num2 >= factor//10: # at least one digit picke AND there are no leading zeros
                # print(f"{num1} + {num2} = {num1+num2}")
                solutions += 1

            if factor >= 1000: return solutions # don't explore over 3-digit pairs

            next_factor = factor * 10
            for rec in triples_n_n:
                if rec[0] & agg_mask == 0:
                    solutions += dfs(rec[0]|agg_mask, False, num1 + rec[1] * factor, num2 + rec[2] * factor, next_factor)
            for rec in triples_n_c:
                if rec[0] & agg_mask == 0:
                    solutions += dfs(rec[0]|agg_mask, True, num1 + rec[1] * factor, num2 + rec[2] * factor, next_factor)
        return solutions


    print(dfs(0, False, 0, 0, 1))
