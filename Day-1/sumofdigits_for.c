/*using for loop*/
#include<stdio.h>
int main()
{
	int n,x,sum=0;
	printf("enter num\n");
	scanf("%d",&n);
	for ( ; n!= 0; n=n/ 10) 
	{
        x = n % 10;   
        sum=sum+x;       
    }
    printf("%d",sum);
}
