# cook your dish here
t = int(input())
for _ in range(t):
    k = int(input())
    mat = []
    for _ in range(8):
        mat.append(['.']*8)
        
    if k<8 :
        mat[0][0]='O'
        j=1 
        for i in range(1,k):
            mat[0][i] = '.'
            j+=1
        mat[0][j] = 'X'
        for i in range(j+1):
            mat[1][i] = 'X'
            
    else:
        if k!=64:
            row = k//8 
            for i in range(row):
                for j in range(8):
                    mat[i][j] = '.'
                    
            rem = k%8 
            if rem==0 and k<64:
                for i in range(8):
                    mat[row][i] = 'X'
            else:
                for i in range(rem,8):
                    mat[row][i] = 'X'
                if k<56 :
                    for i in range(rem+1):
                        mat[row+1][i] = 'X'
                        
    mat[0][0] = 'O'
            
    for i in range(8):
        print(''.join(mat[i]))
