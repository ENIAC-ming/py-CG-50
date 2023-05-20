def nxyz(fi):
    xd = list()
    if fi <= 3:
        xd.append(fi)
    if fi >= 4:
        x = 2
        while fi >= x ** 2:
            if fi % x != 0:
                x += 1
            if fi % x == 0:
                xd.append(str(x))
                fi = int(fi / x)
        xd.append(str(fi))
    if len(xd) == 1 and fi != 1:
        print(fi)
    if fi == 1:
        print("ERROR")
    if len(xd) > 1:
        ff = "*".join(xd)
        print(ff)

print("--Prime Factorization--")
while True:
    fi = eval(input("input:\n"))
    nxyz(fi)