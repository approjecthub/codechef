#include <stdio.h>

int main(void) {
	// your code goes here
	int t,n,i,v,x=1,a=0;
	scanf("%d",&t);
	for(v=0;v<t;v++){
	    scanf("%d", &n);
	    int arr[n];
	    x=1;
	    for(i=0;i<n;i++){
	        
	            if(i%2==0){
	                a=0;
	                while(a<n){
	                printf("%d ", x++);
	                    
	                    a++;
	                }
	            }
	            else{
	                
	                a=0;
	                while(a<n){
	                    arr[a++] = x++;
	                }
	                for(a=n-1;a>=0;a--){
	                    printf("%d ",arr[a]);
	                }
	            }
	             printf("\n");   
	            }
	            
	        
	    }
	return 0;
}

