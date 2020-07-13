# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    points = []
    for _ in range((4*n)-1):
        x,y = input().split()
        x = int(x)
        y = int(y)
        points.append([x,y])
    ans = [points[0][0],points[0][1]]
    
    for i in range(1,len(points)):
        ans[0] = ans[0]^points[i][0]
        ans[1] = ans[1]^points[i][1]
        
    print(str(ans[0]),str(ans[1]))
