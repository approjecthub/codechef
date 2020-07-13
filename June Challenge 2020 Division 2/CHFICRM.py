# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]

    ans='YES'
    sum5 = 0
    sum10 = 0 
    sum15 = 0
    for i in range(n):
        val = arr[i]-5
        if val==5:
            if sum5>=1:
                sum5 -=1 
                sum10 += 1 
            else:
                ans = 'NO'
                break
        elif val==10:
            if sum10>=1:
                sum10 -= 1
                sum15 += 1 
            elif sum5>=2:
                sum5 -= 2 
                sum15 += 1 
            else:
                ans = 'NO'
                break
        else:
            sum5 += 1
    print(ans)
            
