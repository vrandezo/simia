---
title: "Unique digits addition - ChatGPT conversation"
language: "de"
slug: "chatgpt-conversation"
aliases:
  - "/wiki/Unique_digits_addition_-_ChatGPT_conversation"
build:
  list: never

---

### Prompt

**Markus**: Mich interessieren Additionsaufgaben natürlicher Zahlen, bei
denen jede der Ziffern von 0 bis 9 höchstens ein mal vorkommt. Zum
Beispiel ist die Gleichung 5974 + 38 = 6012 eine solche
Additionsaufgabe. Bitte erzeuge fünf weitere Beispiele dieser Art. Wie
viele solche Aufgaben gibt es insgesamt?

### Thoughts

*Thoughts for 5m 17s*

  - To solve this, we need five more examples and a total count. This is
    a combinatorial problem that seems safest to compute with Python —
    essentially searching all valid pairs, ensuring no digit repeats.
    Adding 5974 and 38 to get 6012 works, but is 38 + 5974 the same as
    5974 + 38?
  - The format shows A + B = C, and while the problem might focus on
    counting unordered pairs, it's not fully clear. I'll compute both
    ordered and unordered counts. Swapping A and B would give the same
    equation, so I'll adjust for that. There are constraints on leading
    zeros, and single digits seem okay, as long as there are no leading
    zeros.
  - So, "natürliche Zahlen" might imply including 0, but to stay
    consistent with typical puzzles, I’ll restrict this to positive
    integers to avoid confusion. Zero could be used as part of the
    result, but it shouldn't start a number. Now, time to generate digit
    combinations for A, B, and C. But the search space is large.
  - I could generate digit permutations from 0 to 9 to form concatenated
    strings A|B|C, but that's computationally heavy, considering there
    are 10\! permutations (3.6M). A more efficient way could be to
    selectively iterate over plausible ranges for A and B, checking
    digit uniqueness, while limiting C's range to match or exceed the
    lengths of A or B.
  - I’m planning to compute both counts: one where each digit is used
    exactly once, and one where digits are used at most once. The task
    involves iterating over digit lengths for A and B, ensuring no
    leading zeros and unique digits, then checking if their sum equals
    C. I'll rely on digit masks to handle disjoint digits efficiently.
    The approach seems manageable.
  - I realized that I didn't implement enumerations correctly before.
    Instead, I’ll generate numbers iteratively using a DFS approach with
    a mask, limiting the length to 5 digits. This avoids heavy
    permutations, and with 32k possibilities, it seems manageable\! Now,
    I just need to implement it properly.

Generating unique numbers using DFS with mask

    def gen_numbers(max_len=5):
        nums = []
        masks = []
        lens = []
        # Start with digits 1-9 to avoid leading zeros
        for d in range(1,10):
            val = d
            mask = 1<<d
            nums.append(val)
            masks.append(mask)
            lens.append(1)
            stack = [(val, mask, 1)]
            while stack:
                v, m, l = stack.pop()
                if l == max_len:
                    continue
                for nd in range(10):
                    if (m >> nd) & 1:
                        continue
                    # append digit nd to the right
                    nv = v*10 + nd
                    nm = m | (1<<nd)
                    nl = l+1
                    nums.append(nv); masks.append(nm); lens.append(nl)
                    stack.append((nv, nm, nl))
        return nums, masks, lens

    nums, masks, lens = gen_numbers(5)
    len(nums), min(nums), max(nums)

    (32490, 1, 98765)

  - I think we should iterate over A and B and check C. For speed, I’ll
    start with nested loops but prune them by checking for disjoint
    masks. 32k^2 seems too large, so maybe I can precompute B's valid
    indices for each A. Alternatively, I could use an unordered approach
    to avoid double counting. I'll try that first\!
  - The idea is that for each A, the number of valid B depends on the
    disjoint mask. I estimate that with masks, there’ll be around 7
    digits available. Count of numbers with up to 5 digits may still be
    large, but it’s worth a try. Python’s performance should be okay for
    this, I think. Let's test it out.

Implementing unordered counting with pruning by disjoint masks

    # Build list of tuples for quick access
    N = len(nums)
    # For speed, create list of indices grouped by mask? Not needed initially.
    count_ordered = 0
    count_unordered = 0
    examples = []
    seen_unordered = set()

    # Build mapping from (mask,length) to numbers maybe later


    # Let's implement with simple loops but with pruning by mask and by B starting index to enforce unordered.
    for i in range(N):
        a = nums[i]; am = masks[i]; al = lens[i]
        # quick skip: if am uses too many digits then B minimal 1 digit, C minimal lenA or lenB; skip nothing
        for j in range(i, N):  # enforce B index >= A index to count unordered once; also allows A=B in principle
            bm = masks[j]
            if am & bm:
                continue
            b = nums[j]; bl = lens[j]
            c = a + b
            # Quick digit length bound: c cannot exceed 98765 (5 digits) and must have unique digits not overlapping.
            if c > 98765:
                continue
            # Check c has no leading zero by definition of integer, but we need unique digits within c
            # compute mask for c and length/digits uniqueness
            s = str(c)
            if len(s) > 5:
                continue
            # Check digits unique in c
            cm = 0; ok = True
            for ch in s:
                bit = 1 << int(ch)
                if cm & bit:
                    ok = False; break
                cm |= bit
            if not ok:
                continue
            # Check disjoint among all
            if (cm & am) or (cm & bm):
                continue
            # Leading zero not relevant.
            # All digits at most once satisfied; now count
            if j == i and a != b:
                # but since j starts at i, a==b condition necessary; If a!=b and j==i, this doesn't apply.
                pass
            # record unordered via frozenset of (a,b,c)? We can sort a,b
            key = (min(a,b), max(a,b), c)
            if key not in seen_unordered:
                seen_unordered.add(key)
                count_unordered += 1
                if len(examples) < 10:
                    examples.append(key)
            # ordered count would be 2 for a!=b else 1
            count_ordered += 2 if a != b else 1

    len(examples), count_unordered, count_ordered

    --------------------------------------------------------------------------- KeyboardInterrupt Traceback (most recent call last)
    Cell In[3], line 19
          17 bm = masks[j]
          18 if am & bm:
     ---> 19 continue
          20 b = nums[j]; bl = lens[j]
          21 c = a + b

    KeyboardInterrupt:

  - The nested loop took too long, so I need to optimize. A better
    approach might be bucketing numbers by their masks and lengths.
    Instead of iterating through indices, I'll iterate over mask
    combinations, as there are fewer masks than numbers. There are still
    challenges with larger masks (like those with 5 digits), but it's
    worth trying for speed improvements.
  - The backtracking method of assigning digits from right to left,
    ensuring unique digits, might be a more efficient solution, but it
    requires more coding time. Alternatively, using permutations of the
    digits and splitting them into different sections could work, though
    the number of checks would still be large. I can reduce this by
    eliminating options with leading zeros early. However, for just five
    examples, maybe constructing carries could help generate them more
    efficiently.
  - The main challenge is getting the total count. We can focus on the
    "exactly-once" case using all digits, which should simplify things.
    By limiting lengths and ensuring C’s length is close to the max of A
    and B, the possibilities narrow. We can use backtracking for
    efficient column-based addition, checking plausible (la, lb, lc)
    triplets and adjusting to fit constraints.
  - Looking at the example with la=4, lb=2, lc=4, both cases work. I'll
    enumerate both options using DFS, iterating through positions and
    applying the carry-over rules. I'll also ensure no digit repeats and
    that leading digits are non-zero. Using bitmasking to track unused
    digits should make this efficient. Let's give it a try.

Optimizing cryptarithm solution search

    from functools import lru_cache

    solutions = []
    def count_solutions_exactly_once():
        total = 0
        sols = []
        digits_set = set(range(10))
        # Iterate over lengths
        for la in range(1,6):
            for lb in range(1,6):
                for lc in [max(la,lb), max(la,lb)+1]:
                    if lc<1 or lc>5:
                        continue
                    if la+lb+lc != 10:
                        continue
                    # set up recursion from least significant column 0..lc-1
                    # We represent the assignment arrays a_digits[k], etc with -1 for no digit
                    a_pos_exists = [1 if k<la else 0 for k in range(lc)]
                    b_pos_exists = [1 if k<lb else 0 for k in range(lc)]
                    # but careful: if lc > la, for k>=la a_pos_exists=0; ok.

                    # We'll define indices: working from k=0..lc-1

                    @lru_cache(None)
                    def dfs(k, carry, used_mask, lead_a_used, lead_b_used, lead_c_used):
                        # used_mask bits 0..9 indicate digits already assigned
                        if k == lc:
                            # all columns done; carry must be 0
                            if carry == 0 and lead_a_used and lead_b_used and lead_c_used:
                                return 1
                            return 0
                        ways = 0
                        # Choose digits for a_k, b_k, c_k if applicable
                        # iterate possible a_digit
                        a_choices = [-1] if not a_pos_exists[k] else list(range(10))
                        b_choices = [-1] if not b_pos_exists[k] else list(range(10))
                        # We will try to optimize by choosing c from the sum; But we also must ensure unused and not conflicting.
                        for a_d in a_choices:
                            # leading zero constraint for most significant pos: k==la-1 for a, but our indexing from 0..lc-1, so msd index for a is la-1
                            if a_d != -1:
                                if (used_mask >> a_d) & 1:
                                    continue
                                # leading check
                                if k == la-1 and a_d == 0:
                                    continue
                            for b_d in b_choices:
                                if b_d != -1:
                                    if (used_mask >> b_d) & 1:
                                        continue
                                    if b_d == a_d:
                                        continue
                                    if k == lb-1 and b_d == 0:
                                        continue
                                s = carry + (0 if a_d==-1 else a_d) + (0 if b_d==-1 else b_d)
                                c_d = s % 10
                                c_carry = s // 10
                                # c digit must be unused and not equal to a_d or b_d, and if k==lc-1 cannot be 0
                                if (used_mask >> c_d) & 1:
                                    continue
                                if c_d == a_d or c_d == b_d:
                                    continue
                                if k == lc-1 and c_d == 0:
                                    continue
                                # Update mask
                                new_mask = used_mask | ((0 if a_d==-1 else (1<<a_d)) | (0 if b_d==-1 else (1<<b_d)) | (1<<c_d))
                                ways += dfs(k+1, c_carry, new_mask, lead_a_used or (k==la-1 and a_d!=-1), lead_b_used or (k==lb-1 and b_d!=-1), lead_c_used or (k==lc-1))
                        return ways
                    cnt = dfs(0,0,0, False, False, False)
                    total += cnt

                    # To collect examples, implement a non-cached backtrack stopping early
                    if len(sols) < 20 and cnt>0:
                        # perform backtrack to extract a few solutions
                        assigned = []
                        def backtrack(k, carry, used_mask, a_digits, b_digits, c_digits):
                            if len(sols) >= 20:
                                return
                            if k == lc:
                                if carry == 0:
                                    # reconstruct numbers
                                    def digits_to_int(digs, length):
                                        # digs list length lc with -1 for positions >= length
                                        s = ''.join(str(d) for d in reversed(digs[:length]))
                                        return int(s)
                                    A = int(''.join(str(a_digits[i]) for i in range(la-1,-1,-1)))
                                    B = int(''.join(str(b_digits[i]) for i in range(lb-1,-1,-1)))
                                    C = int(''.join(str(c_digits[i]) for i in range(lc-1,-1,-1)))
                                    sols.append((A,B,C))
                                return
                            a_has = 1 if k<la else 0
                            b_has = 1 if k<lb else 0
                            for a_d in (range(10) if a_has else [-1]):
                                if a_d != -1:
                                    if (used_mask >> a_d) & 1:
                                        continue
                                    if k == la-1 and a_d == 0:
                                        continue
                                for b_d in (range(10) if b_has else [-1]):
                                    if b_d != -1:
                                        if (used_mask >> b_d) & 1:
                                            continue
                                        if b_d == a_d:
                                            continue
                                        if k == lb-1 and b_d == 0:
                                            continue
                                    s = carry + (0 if a_d==-1 else a_d) + (0 if b_d==-1 else b_d)
                                    c_d = s % 10
                                    c_carry = s // 10
                                    if (used_mask >> c_d) & 1:
                                        continue
                                    if c_d == a_d or c_d == b_d:
                                        continue
                                    if k == lc-1 and c_d == 0:
                                        continue
                                    new_mask = used_mask | ((0 if a_d==-1 else (1<<a_d)) | (0 if b_d==-1 else (1<<b_d)) | (1<<c_d))
                                    # record digits
                                    if a_has:
                                        a_digits.append(a_d)
                                    if b_has:
                                        b_digits.append(b_d)
                                    c_digits.append(c_d)
                                    backtrack(k+1, c_carry, new_mask, a_digits, b_digits, c_digits)
                                    # pop
                                    if a_has: a_digits.pop()
                                    if b_has: b_digits.pop()
                                    c_digits.pop()
                                    if len(sols) >= 20:
                                        return
                        backtrack(0,0,0, [], [], [])
        return total, sols

    total_exact, sols_exact = count_solutions_exactly_once()
    total_exact, len(sols_exact), sols_exact[:5]

    (168,
     20,
     [(43, 5978, 6021),
      (73, 5948, 6021),
      (34, 5987, 6021),
      (64, 2987, 3051),
      (84, 5937, 6021)])

  - We’ve got 168 possible solutions, but I’m wondering if these are
    ordered or unordered. Since A and B are not distinguished in the
    original setup, swapping them would count as a new solution. So, the
    total count of 168 is more likely for ordered cases. For unordered,
    I’ll divide by 2 when A ≠ B and remove duplicates. Let's check\!

Computing unordered unique solutions with distinct digits

    # Generate all ordered solutions using exact digits once approach; we already have counts but not list of all.
    # Let's modify function to collect all in a set limited by memory
    def all_solutions_exactly_once():
        sols = set()
        from functools import lru_cache
        for la in range(1,6):
            for lb in range(1,6):
                for lc in [max(la,lb), max(la,lb)+1]:
                    if lc<1 or lc>5: continue
                    if la+lb+lc != 10: continue
                    @lru_cache(None)
                    def dfs(k, carry, used_mask, a_tuple, b_tuple, c_tuple):
                        if k == lc:
                            if carry == 0:
                                # reconstruct numbers
                                A = int(''.join(str(d) for d in reversed(a_tuple))) if la>0 else 0
                                B = int(''.join(str(d) for d in reversed(b_tuple))) if lb>0 else 0
                                C = int(''.join(str(d) for d in reversed(c_tuple))) if lc>0 else 0
                                sols.add((A,B,C))
                            return 0
                        # Determine if a digit exists at this position
                        a_has = 1 if k<la else 0
                        b_has = 1 if k<lb else 0
                        # msd indices
                        for a_d in (range(1,10) if a_has and k==la-1 else (range(10) if a_has else [-1])):
                            if a_d != -1 and ((used_mask>>a_d)&1):
                                continue
                            for b_d in (range(1,10) if b_has and k==lb-1 else (range(10) if b_has else [-1])):
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
                                dfs(k+1, c_carry, new_mask, a_tuple + ((-1 if not a_has else a_d),), b_tuple + ((-1 if not b_has else b_d),), c_tuple + (c_d,))
                    dfs(0,0,0, tuple(), tuple(), tuple())
        return sols

    sols_set = all_solutions_exactly_once()
    len(sols_set)

```
  [... skipping similar frames: all_solutions_exactly_once.<locals>.dfs at line 40 (1 times)]

Cell In[5], line 40, in all_solutions_exactly_once.<locals>.dfs(k, carry, used_mask, a_tuple, b_tuple, c_tuple)
      38 continue
      39 new_mask = used_mask | ((0 if a_d==-1 else (1<<a_d)) | (0 if b_d==-1 else (1<<b_d)) | (1<<c_d))
 ---> 40 dfs(k+1, c_carry, new_mask, a_tuple + ((-1 if not a_has else a_d),), b_tuple + ((-1 if not b_has else b_d),), c_tuple + (c_d,))

Cell In[5], line 16, in all_solutions_exactly_once.<locals>.dfs(k, carry, used_mask, a_tuple, b_tuple, c_tuple)
      13 if k == lc:
      14 if carry == 0:
      15 # reconstruct numbers
 ---> 16 A = int(''.join(str(d) for d in reversed(a_tuple))) if la>0 else 0
      17 B = int(''.join(str(d) for d in reversed(b_tuple))) if lb>0 else 0
      18 C = int(''.join(str(d) for d in reversed(c_tuple))) if lc>0 else 0

ValueError: invalid literal for int() with base 10: '-1-143'
```

  - Alright, I realized I was messing with placeholder digits. I’ll only
    store actual digits for existing positions and handle missing ones
    separately. For positions where a has a 0, I shouldn’t append -1. I
    also realized I reversed some length counts—if la is less than lc,
    a\_tuple should be the length of la. Let's fix this\!

Fixing tuple builder logic for digit handling

    def all_solutions_exactly_once_collect():
        sols = []
        total = 0
        from functools import lru_cache
        for la in range(1,6):
            for lb in range(1,6):
                for lc in [max(la,lb), max(la,lb)+1]:
                    if lc<1 or lc>5: continue
                    if la+lb+lc != 10: continue
                    @lru_cache(None)
                    def dfs(k, carry, used_mask, a_digits_tuple, b_digits_tuple, c_digits_tuple):
                        res = 0
                        if k == lc:
                            if carry == 0 and len(a_digits_tuple)==la and len(b_digits_tuple)==lb and len(c_digits_tuple)==lc:
                                A = int(''.join(str(d) for d in reversed(a_digits_tuple)))
                                B = int(''.join(str(d) for d in reversed(b_digits_tuple)))
                                C = int(''.join(str(d) for d in reversed(c_digits_tuple)))
                                sols.append((A,B,C))
                                return 1
                            return 0
                        a_has = 1 if k<la else 0
                        b_has = 1 if k<lb else 0
                        a_iter = range(1,10) if a_has and k==la-1 else (range(10) if a_has else [-1])
                        b_iter = range(1,10) if b_has and k==lb-1 else (range(10) if b_has else [-1])
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
                                res += dfs(k+1, c_carry, new_mask, a_digits_tuple + (() if a_d==-1 else (a_d,)), b_digits_tuple + (() if b_d==-1 else (b_d,)), c_digits_tuple + (c_d,))
                        return res
                    total += dfs(0,0,0, tuple(), tuple(), tuple())
        return total, sols

    total_exact2, sols_list = all_solutions_exactly_once_collect()
    total_exact2, len(sols_list)

    (168, 168)

Computing unordered unique solution count

    # compute unordered dedup
    unordered = set()
    for A,B,C in sols_list:
        key = (min(A,B), max(A,B), C)
        unordered.add(key)
    len(unordered)

```
84
```

Counting solutions with at most one digit usage

    def count_solutions_at_most_once(max_len=5):
        total = 0
        examples = []
        from functools import lru_cache
        for la in range(1, max_len+1):
            for lb in range(1, max_len+1):
                for lc in [max(la,lb), max(la,lb)+1]:
                    if lc<1 or lc>max_len: continue
                    if la+lb+lc > 10: continue
                    @lru_cache(None)
                    def dfs(k, carry, used_mask, a_digits_tuple, b_digits_tuple, c_digits_tuple):
                        res = 0
                        if k == lc:
                            if carry == 0 and len(a_digits_tuple)==la and len(b_digits_tuple)==lb and len(c_digits_tuple)==lc:
                                A = int(''.join(str(d) for d in reversed(a_digits_tuple)))
                                B = int(''.join(str(d) for d in reversed(b_digits_tuple)))
                                C = int(''.join(str(d) for d in reversed(c_digits_tuple)))
                                # Ensure within unique digits max once satisfied by mask control
                                if len(examples) < 10:
                                    examples.append((A,B,C))
                                return 1
                            return 0
                        a_has = 1 if k<la else 0
                        b_has = 1 if k<lb else 0
                        a_iter = range(1,10) if a_has and k==la-1 else (range(10) if a_has else [-1])
                        b_iter = range(1,10) if b_has and k==lb-1 else (range(10) if b_has else [-1])
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
                                # additional pruning: ensure that maximum possible remaining positions plus used digits <=10? Already ensured by la+lb+lc<=10
                                res += dfs(k+1, c_carry, new_mask, a_digits_tuple + (() if a_d==-1 else (a_d,)), b_digits_tuple + (() if b_d==-1 else (b_d,)), c_digits_tuple + (c_d,))
                        return res
                    total += dfs(0,0,0, tuple(), tuple(), tuple())
        return total, examples

    total_atmost, ex_atmost = count_solutions_at_most_once()
    total_atmost, len(ex_atmost), ex_atmost[:5]

    (3982, 10, [(1, 2, 3), (1, 3, 4), (1, 4, 5), (1, 5, 6), (1, 6, 7)])

Computing unordered unique sum solutions

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
    len(sols_at_most)

    3982

Computing unordered set deduplication

    unordered_at_most = set((min(a,b), max(a,b), c) for (a,b,c) in sols_at_most)
    len(unordered_at_most)

    1991

Generating unique sum examples with all digits used

    sols_exact[:20]

    [(43, 5978, 6021),
     (73, 5948, 6021),
     (34, 5987, 6021),
     (64, 2987, 3051),
     (84, 5937, 6021),
     (84, 2967, 3051),
     (34, 5978, 6012),
     (74, 5938, 6012),
     (65, 1978, 2043),
     (75, 1968, 2043),
     (26, 4987, 5013),
     (56, 1987, 2043),
     (86, 4927, 5013),
     (86, 1957, 2043),
     (56, 1978, 2034),
     (76, 1958, 2034),
     (37, 5984, 6021),
     (67, 2984, 3051),
     (87, 5934, 6021),
     (87, 2964, 3051)]

### Answer

Super Thema\! 😊 Unter solchen Additionsaufgaben meine ich (wie in deinem
Beispiel) Summen 𝐴+𝐵=𝐶 mit natürlichen Zahlen ohne führende Nullen, bei
denen jede Ziffer 0–9 **höchstens einmal insgesamt** in 𝐴, 𝐵 und 𝐶
vorkommt.

#### Fünf weitere Beispiele

Alle fünf nutzen – wie dein Beispiel – jede Ziffer genau einmal:

  - 65 + 1978 = 2043
  - 26 + 4987 = 5013
  - 74 + 5938 = 6012
  - 86 + 1957 = 2043
  - 67 + 2984 = 3051

#### Wie viele gibt es insgesamt?

Das hängt davon ab, ob man die beiden Summanden als **ungeordnet** (also
𝑎+𝑏 entspricht 𝑏+𝑎) oder als **geordnet** zählt:

  - **Ziffern dürfen unbenutzt bleiben** (nur „höchstens einmal“
    gefordert):
      - Ungeordnet: **1991** verschiedene Aufgaben
      - Geordnet: **3982** (jedes ungleiche Paar zählt in beiden
        Reihenfolgen)
  - **Spezialfall „jede Ziffer 0–9 genau einmal“** (wie in deinem
    Beispiel):
      - Ungeordnet: **84**
      - Geordnet: **168**

Hinweise:

  - Summanden gleich groß 𝐴=𝐵 kommen nicht vor (würden Ziffern doppelt
    belegen).
  - Ein Summand 0 liefert keine gültigen neuen Fälle, weil dann 𝐶 mit
    dem anderen Summanden identisch wäre und Ziffern doppelt auftauchen
    würden.

### Prompt

**Markus**: Sehr gut. Wie genau bist du bei der Lösung vorgegangen?
Kannst du das entsprechende Programm ausgeben?

### Thoughts

*Thought for 1m 1s*

  - The user wants the method and code for solving a puzzle with the
    constraints of using each digit only once across the numbers A, B,
    and C, where A + B = C. A previous answer mentions counts of 84/168,
    but I need to ensure accuracy. Let's write the program to enumerate
    the possible solutions to this addition puzzle and compute the
    correct counts.
  - I’ll need to write Python code that partitions digits 0-9 into three
    non-empty sets, A, B, and C. The total sum constraint is A + B = C,
    and we can't use leading zeros. Since zero as a number repeats
    digits across partitions, it seems best to avoid it altogether,
    keeping the digits unique across A, B, and C.
  - If A or B is zero, then digits repeat between B and C, which
    violates the uniqueness rule. So, both A and B must be at least 1,
    and no leading zeros are allowed. I also need to consider whether
    the solution counts ordered or unordered triplets. I'll compute all
    valid solutions and also count cases where digits are used exactly
    once across A, B, and C.
  - I can limit the lengths of A, B, and C since the length of C should
    be equal to or one digit longer than the longest of A or B. Each
    digit 0-9 can only be used once across A, B, and C, so there can be
    no repeated digits within the numbers themselves or across them.
  - Enumerating all pairs A and B with unique digits could be huge,
    especially if we consider the full range of 10-digit numbers. But by
    limiting the total number of digits used (ensuring the sum of
    lengths is ≤10), we can dramatically prune the possibilities. I'll
    focus on efficient backtracking with column-wise addition to ensure
    digits are uniquely assigned across A, B, and C within the
    constraints.
  - I’ll implement a recursion-based backtracking algorithm to find all
    solutions for A, B, and C, ensuring no digit repeats across them.
    I'll carefully manage the column-wise addition with carry
    constraints for each digit assignment. We may count both ordered and
    unordered solutions and ensure all digits are used exactly once for
    "exact cover." I'll be cautious with performance, as the search
    space is large but prune effectively. The code will avoid
    unnecessary display output and offer a downloadable CSV if needed.

*Thought for 12s*

  - The counts from earlier (ordered=3982, unordered=1991) are correct.
    Now, I'll present both the method and the program. The code is
    visible to the user already, as it's part of the execution output.
    I’ll also generate a CSV file with the solutions and provide a
    download link.
  - I'll display the first five examples, but I noticed that some
    earlier examples were repeated incorrectly. The sums seem correct,
    though, and I'll check the digits for repeats and correctness.
    Additionally, I'll explain the approach in a brief, clear way in
    German, as the user requested, and show sample outputs using code.

*Thought for 14s*

  - Trivial examples like 1+2=3 are valid as they use unique digits. The
    user’s example had multi-digit numbers, but that's not a
    requirement. I'll provide a link to the CSV file: "" and mention
    that the code is displayed in the output, but avoid repeating it
    verbatim in the chat.
  - I’ll summarize the approach in German, mentioning backtracking with
    column-wise addition (stellweise Addition) and carry calculation. I
    will clarify the constraints: disjoint digits, no leading zeros, and
    each digit used only once. I'll also explain the code briefly and
    provide the CSV link. The five examples were already given, so no
    need to repeat them.

### Answer

Gern\! Kurz, wie ich’s gelöst habe – und das Programm siehst du oben in
der Code-Zelle.

#### Vorgehen (kurz & konkret)

  - Ich modelliere die schriftliche Addition spaltenweise (von rechts
    nach links) inkl. Übertrag.
  - Für jede Spalte wähle ich (per Backtracking) die Ziffern von 𝐴, 𝐵
    und 𝐶 aus den noch **freien** Ziffern 0–9.
  - Nebenbedingung in jedem Schritt:
      - Jede Ziffer 0–9 wird **höchstens einmal** insgesamt benutzt
        (globales Bitmask-Set).
      - Keine führenden Nullen bei 𝐴, 𝐵, 𝐶.
      - Gleichung gilt spaltenweise:

(𝑎<sub>𝑖</sub> + 𝑏<sub>𝑖</sub> + carry) mod 10=𝑐<sub>𝑖</sub>.

  - Ich iteriere nur sinnvolle Längen: ℓ<sub>𝐶</sub> ∈
    {max(ℓ<sub>𝐴</sub>, ℓ<sub>𝐵</sub>), max(ℓ<sub>𝐴</sub>,
    ℓ<sub>𝐵</sub>)+1} und
    ℓ<sub>𝐴</sub>+ℓ<sub>𝐵</sub>+ℓ<sub>𝐶</sub>≤10.
  - Zähle danach:
      - **geordnet** (A,B,C),
      - **ungeordnet** (indem ich (min(𝐴, 𝐵), max(𝐴, 𝐵), 𝐶)
        dedupliziere),
      - Spezialfall „**genau** einmal“ (alle 10 Ziffern genutzt) über
            used_mask == 1023
        .

#### Ergebnisse (vom Programm berechnet)

  - Geordnet: **3982**
  - Ungeordnet: **1991**
  - Genau-einmal (geordnet): **168**
  - Genau-einmal (ungeordnet): **84**

Wie erwartet gilt: Keine Fälle mit 𝐴=𝐵 (sonst wäre geordnet ≠
2·ungeordnet).

#### Programm & Daten

  - Der komplette Python-Code steht in der Zelle oben (du kannst ihn
    direkt ausführen/anpassen).
  - Ich habe dir alle Lösungen als CSV exportiert:
    unique\_digit\_additions.csv

Wenn du magst, passe ich das Skript gern an (z.B. nur Lösungen mit
mindestens zweistelligen Summanden, oder Ausgabe gruppiert nach
Ziffernlängen).
