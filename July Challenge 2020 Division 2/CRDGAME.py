# cook your dish here
def total(ar):
    res = 0
    for x in ar:
        res += int(x)
    return res
t = int(input())
for _ in range(t):
    c = 0
    m = 0
    n = int(input())
    for _ in range(n):
        cards = input().split()
        sum1 = total(cards[0])
        sum2 = total(cards[1])
        if sum1>sum2:
            c += 1 
        elif sum1<sum2:
            m += 1 
        else:
            c += 1 
            m += 1 
    if c>m:
        print(0,c)
    elif c==m:
        print(2,c)
    else:
        print(1,m)
        
