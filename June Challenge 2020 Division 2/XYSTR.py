# cook your dish here
n = int(input())
for _ in range(n):
    s = input()
    ans1 = s.count('xy')
    s = s.replace('xy','')
    ans2 = s.count('yx')
    ans = ans1+ans2
    print(ans)
