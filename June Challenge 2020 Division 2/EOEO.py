# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    ans = 0
    if n%2!=0:
        
        ans = (n-1)//2 
    else:

        
        while n%2==0:
            n //=2
            
        ans = (n-1)//2
    print(ans)
