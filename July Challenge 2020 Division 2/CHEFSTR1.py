# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]
    total = 0
    for i in range(n-1):
        total += abs(arr[i]-arr[i+1])-1
        
    print(total)
