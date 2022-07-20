def f(x, y, k):
    if x == y: return 1
    if x < y or x == 37: return 0
    if k == "-2":
        if x % 2 == 0: return f(x - 3, y, "-3") + f(x // 2, y, "/2")
        else: return f(x - 3, y, "-3")
    if k == "-3":
        if x % 2 == 0: return f(x - 2, y, "-2") + f(x // 2, y, "/2")
        else: return f(x - 2, y, "-2")
    if k == "/2": return f(x - 3, y, "-3") + f(x - 2, y, "-2")
    else:
        if x % 2 == 0: return f(x - 2, y, "-2") + f(x - 3, y, "-3") + f(x // 2, y, "/2")
        else: return f(x - 2, y, "-2") + f(x - 3, y, "-3")

print(f(51, 10, "") * f(10, 3, ""))
