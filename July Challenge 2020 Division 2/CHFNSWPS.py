# cook your dish here
def findCommon(ar1, ar2): 
       
    i, j= 0, 0,
        
    while (i < len(ar1) and j < len(ar2)): 
        
        if (ar1[i] == ar2[j] ): 
            return ar1[i]
          
        elif ar1[i] < ar2[j]: 
            i += 1
            
        else: 
            j += 1
 
    return max(max(ar1), max(ar2))
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    dica = {}
    dicb = {}
    
    for x in a:
        if x not in dica:
            dica[x]=1
        else:
            dica[x]+=1
            
    for x in b:
        if x not in dicb:
            dicb[x]=1
        else:
            dicb[x]+=1
            
    needb = {}
    needa = {}
    
    for k in dicb:
        if k not in dica:
            needa[k]= dicb[k]
        else:
            if dicb[k]>dica[k]:
                needa[k] = dicb[k]-dica[k] 
                
    for k in dica:
        if k not in dicb:
            needb[k]= dica[k]
        else:
            if dica[k]>dicb[k]:
                needb[k] = dica[k]-dicb[k] 
                
    label = False
    if len(needa)==0:
        print(0)
        label = True
    else:
        for x in needa:
            if needa[x]%2!=0:
                print(-1)
                label = True
                break
        if label == False:
            for x in needb:
                if needb[x]%2!=0:
                    print(-1)
                    label = True
                    break
    if label==False:
        
        lia = []
        lib = []
    
        for x in needa:
            lia += [x]*(needa[x]//2)
    
        for x in needb:
            lib += [x]*(needb[x]//2)
        ans2 = 0 
        i=0
        lia.sort()
        lib.sort(reverse=True)
        x = min(min(a), min(b))
        while i <len(lia):
            val = min(lia[i],lib[i],2*x)
            
            i+=1
            ans2 += val
            
        print(ans2)
