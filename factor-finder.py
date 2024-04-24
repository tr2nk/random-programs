def factors(n):
    o = []
    for i in range(1, n+1):
        if n / i == n // i:
            o.append(i)
    out = []
    for i in range((len(o) + 1) // 2):
        out.append(str((o[i], o[-1 - i])) + " -> " + str(o[i] + o[-1 - i]))
    return str(out)[1:-1].replace("'", "").replace(", (", "\n(")

while True:
    print(factors(int(input("Enter "))))