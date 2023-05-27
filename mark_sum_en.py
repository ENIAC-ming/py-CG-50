k = [1.0, 1.0, 1.0, 0.6, 0.75, 0.9, 0.7, 1.0, 1.0, 1.0]
m = [0] * 10
m[0] = float(input("Chinese:"))
m[1] = float(input("Mathematics:"))
m[2] = float(input("English:"))
m[3] = float(input("Politics:"))
m[4] = float(input("History:"))
m[5] = float(input("Physics:"))
m[6] = float(input("Chemistry:"))
m[7] = float(input("Biology:"))
m[8] = float(input("Geography:"))
m[9] = float(input("PE:"))

if m[7] > 40:
    m[7] *= 0.4
if m[8] > 40:
    m[8] *= 0.4

n = [0] * 10
for i in range(10):
    n[i] = round(k[i] * m[i])

print("Total score of 3 subjects:\n", sum(m[:3]))
print("Total score of 3 subjects:\n", sum(m[:7]))
print("Discounted score of 7 subjects:\n", sum(n[:7]))
print("Discounted score of 10 subjects:\n", sum(n))