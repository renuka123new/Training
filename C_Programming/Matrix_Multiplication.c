// C program to multiply two square matrices.
#include <stdio.h>
#define N 4

void multiply(int mat1[][N], int mat2[][N], int res[][N])
{
	int i, j, k;
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			res[i][j] = 0;
			for (k = 0; k < N; k++)
				res[i][j] += mat1[i][k] * mat2[k][j];
		}
	}
}

int main()
{
	int r1,c1,r2,c2;
	printf("Please enter the 4x4 matrix \n");
	printf("Enter dimention of first matrix\n");
	scanf("%d %d",&r1,&c1);
	printf("Enter dimention of second matrix\n");
	scanf("%d %d",&r2,&c2);
	
	if(r1==c2){
    	int mat1[r1][c1];
    	printf("Enter %d x %d elements in first matrix",r1,c1);
    	for (int i=0;i<r1;i++){
    	    for (int j=0;j<c1;j++){
    	        scanf("%d",&mat1[i][j]);
    	    }
    	}
    	
    	int mat2[r2][c2];
    	printf("Enter %d x %d elements in second matrix",r2,c2);
    	for (int i=0;i<r2;i++){
    	    for (int j=0;j<c2;j++){
    	        scanf("%d",&mat2[i][j]);
    	    }
    	}
    
    
    	int res[r1][c1]; // To store result
    	int i, j;
    	multiply(mat1, mat2, res);
    
    	printf("Result matrix is \n");
    	for (i = 0; i < r1; i++) {
    		for (j = 0; j < c1; j++)
    			printf("%d ", res[i][j]);
    		printf("\n");
    	}
	}

	return 0;
}
