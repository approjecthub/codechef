# cook your dish here
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list( map(int, input().split()))
    arr.sort()
    ans = 0
    for i in range(n):
        
        if arr[i]<=x:
            ans += 1
            if 2*arr[i]>x:
                x = 2*arr[i]
        else:
            
            while x<=arr[i]:
                ans += 1 
                x = 2*x 
                if x>arr[i] and x<2*arr[i]:
                    x = arr[i]
                    
        
    print(ans)
