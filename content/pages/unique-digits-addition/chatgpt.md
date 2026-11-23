---
title: "Unique digits addition - ChatGPT"
language: "de"
slug: "chatgpt"
aliases:
  - "/wiki/Unique_digits_addition_-_ChatGPT"
build:
  list: never

---

    def all_solutions_at_most_once():
        sols = set()
        from functools import lru_cache
        for la in range(1,6):
            for lb in range(1,6):
                for lc in [max(la,lb), max(la,lb)+1]:
                    if lc<1 or lc>5: continue
                    if la+lb+lc > 10: continue
                    @lru_cache(None)
                    def dfs(k, carry, used_mask, a_digits_tuple, b_digits_tuple, c_digits_tuple):
                        if k == lc:
                            if carry == 0 and len(a_digits_tuple)==la and len(b_digits_tuple)==lb and len(c_digits_tuple)==lc:
                                A = int(''.join(str(d) for d in reversed(a_digits_tuple)))
                                B = int(''.join(str(d) for d in reversed(b_digits_tuple)))
                                C = int(''.join(str(d) for d in reversed(c_digits_tuple)))
                                sols.add((A,B,C))
                                return 1
                            return 0
                        a_has = 1 if k<la else 0
                        b_has = 1 if k<lb else 0
                        a_iter = range(1,10) if a_has and k==la-1 else (range(10) if a_has else [-1])
                        b_iter = range(1,10) if b_has and k==lb-1 else (range(10) if b_has else [-1])
                        total = 0
                        for a_d in a_iter:
                            if a_d != -1 and ((used_mask>>a_d)&1):
                                continue
                            for b_d in b_iter:
                                if b_d != -1:
                                    if ((used_mask>>b_d)&1) or b_d==a_d:
                                        continue
                                s = carry + (0 if a_d==-1 else a_d) + (0 if b_d==-1 else b_d)
                                c_d = s % 10
                                c_carry = s // 10
                                if (used_mask>>c_d)&1 or c_d==a_d or c_d==b_d:
                                    continue
                                if k==lc-1 and c_d==0:
                                    continue
                                new_mask = used_mask | ((0 if a_d==-1 else (1<<a_d)) | (0 if b_d==-1 else (1<<b_d)) | (1<<c_d))
                                total += dfs(k+1, c_carry, new_mask, a_digits_tuple + (() if a_d==-1 else (a_d,)), b_digits_tuple + (() if b_d==-1 else (b_d,)), c_digits_tuple + (c_d,))
                        return total
                    dfs(0,0,0, tuple(), tuple(), tuple())
        return sols

    sols_at_most = all_solutions_at_most_once()
    print(len(sols_at_most))
