function = lambda n: print(*map(lambda n, perm: ''.join(["1"] + [{"0": "", "1": " + ", "2": " - "}[perm[index]] + str(range(2, 10)[index]) for index in range(len(perm))] + [f" = {n}"]), [n] * 3 ** 8, map(lambda digit: digit.rjust(8).replace(" ", "0"), map(lambda func, n: "" if n == 0 else func(func, n // 3) + str(n % 3), [lambda func, n: "" if n == 0 else func(func, n // 3) + str(n % 3)] * 3 ** 8, filter(lambda perm: perm != None, [index if perm == n else None for index, perm in enumerate(map(sum, map(lambda func, perm: [int(perm[0])] if len(perm) == 1 else func(func, perm[:-2]) + [int({"1": "+", "2": "-"}[perm[-2]] + str(perm[-1]))], [lambda func, perm: [int(perm[0])] if len(perm) == 1 else func(func, perm[:-2]) + [int({"1": "+", "2": "-"}[perm[-2]] + str(perm[-1]))]] * 3 ** 8, map(lambda func, perm, ls = ["1"]: ls if perm == "" else func(func, perm[1:], ls[:-1] + [ls[-1] + str(range(2, 10)[8 - len(perm)])]) if perm[0] == "0" else func(func, perm[1:], ls + [perm[0]] + [str(range(2, 10)[8 - len(perm)])]), [lambda func, perm, ls = ["1"]: ls if perm == "" else func(func, perm[1:], ls[:-1] + [ls[-1] + str(range(2, 10)[8 - len(perm)])]) if perm[0] == "0" else func(func, perm[1:], ls + [perm[0]] + [str(range(2, 10)[8 - len(perm)])])] * 3 ** 8, map(lambda digit: digit.rjust(8).replace(" ", "0"), map(lambda func, n: "" if n == 0 else func(func, n // 3) + str(n % 3), [lambda func, n: "" if n == 0 else func(func, n // 3) + str(n % 3)] * 3 ** 8, range(3 ** 8)))))))])))), sep="\n")
