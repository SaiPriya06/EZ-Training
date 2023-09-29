#include<stdio.h>
main()
{
	int i,j,r,c,a[10][10],a1[10][10];
	scanf("%d %d",&r,&c);
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	for(j=0;j<c;j++)
	{
		for(i=0;i<r;i++)
		{
			a1[i][j]=a[i][j];
		}
	}
	for(i=0;i<r/2;i++)
	{
		for(j=0;j<c;j++)
		{
			int temp=a1[i][j];
			a1[i][j]=a1[r-i-1][j];
			a1[r-i-1][j]=temp;
		}
	}
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			printf("%d ",a1[i][j]);
		}
	}
}
