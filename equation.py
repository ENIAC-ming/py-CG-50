def gauss_elimination(a, b):
    n = len(a)
    for i in range(n):
        max_element = abs(a[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(a[k][i]) > max_element:
                max_element = abs(a[k][i])
                max_row = k
        for k in range(i, n):
            tmp = a[max_row][k]
            a[max_row][k] = a[i][k]
            a[i][k] = tmp
        tmp = b[max_row]
        b[max_row] = b[i]
        b[i] = tmp
        for k in range(i + 1, n):
            c = -a[k][i] / a[i][i]
            for j in range(i, n):
                if i == j:
                    a[k][j] = 0
                else:
                    a[k][j] += c * a[i][j]
            b[k] += c * b[i]
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / a[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= a[k][i] * x[i]
    return x

def tostr(a):
    if(a >= 0): return("+"+str(a))
    else: return(str(a))

a = []
b = []
deg = int(input("degree(>=1):"))
for i in range(deg+1):
    print(i+1,"of",deg+1)
    x = float(input("x:"))
    y = float(input("y:"))
    tmp = []
    for j in range(deg,-1,-1):
        tmp.append(x**j)
    a.append(tmp)
    b.append(y)
x = gauss_elimination(a, b)
ans = 'y='
for i in range(deg-1):
    ans+='['+str(x[i])+']x^'+str(deg-i)+'+'
ans+='['+str(x[deg-1])+']x+['+str(x[deg])+']'
print(ans)

if(deg == 2):
    a = x[0]; b = x[1]; c = x[2]
    print("y=(x"+tostr(b/a/2)+")^2"+tostr((4*a*c-b*b)/a/4))