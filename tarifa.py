# Victor Silva @ 11:56 PM 02/24/2020

X = int(input()) #Monthly limit
N = int(input()) #Months

megabytesUsed = 0

for i in range(N):
    userInput = int(input())
    megabytesUsed += userInput

finalBalance = X*(N+1) - megabytesUsed
print(finalBalance)
