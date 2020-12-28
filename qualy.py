#Victor Silva @ 02/25/2020

N = int(input())
qaly = 0
for i in range(N):
    q , y = input().split()
    q = round(float(q),4)
    y = round(float(y),4)
    k = q * y
    k = round(k,4)
    qaly += k
print("{:.3f}".format(qaly))
