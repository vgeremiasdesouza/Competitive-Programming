#Victor Silva @ 09/18/2020

N = input()
temps = input().split()
count = 0
for i in range(int(N)):
    if int(temps[i]) < 0:
        count += 1 
print(count)
