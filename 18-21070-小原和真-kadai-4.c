#include <stdio.h>



typedef struct {
	int int_arr = 0;
	char chr_arr[11] = "Hello";
	double dbl_arr = 2;
	long lon_arr = 100;
}NUM;


int main(void) {
	
	NUM a, b, c, d, e;
	NUM num_arr[5] = {a, b, c, d, e};

	int array[5][4][3][2];
	int num = 1;

	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 3; k++) {
				for (int l = 0; l < 2; l++) {
					array[i][j][k][l] = num;
					printf("[%d][%d][%d][%d] : %d\n", i, j, k, l, array[i][j][k][l]); 
					num++;
				}
			}
		}
	}

	return 0;
}
