# cook your dish here
t = int(input())
for _ in range(t):
    n,k = input().split()
    n=int(n)
    k=int(k)
    arr = input().split()
    arr = [int(x) for x in arr]
    total = sum(arr)
    total_red = 0
    for i in range(len(arr)):
        if arr[i]>k:
            total_red += k 
        else:
            total_red += arr[i]
    print(total-total_red)
