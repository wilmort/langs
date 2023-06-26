#include <stdio.h>

int main() {

	// declare some primitives
	int i;
	float f;
	double d;
	char c;
	
	// declare some arrays of primitives
	int in_ar[5];
	float fl_ar[5];
	double do_ar[5];
	char ch_ar[5];

	i = 10;
	f = 10.0;
	d = 100100.101010;
	c = 'n';

	printf("Here is your int: %d\n", i);
	printf("Here is your float: %f\n", f);
	printf("Here is your double: %lf\n", d);
	printf("Here is your char: %c\n", c);

	// Fill the int array
	for(int k=0; k<5; k++){
		in_ar[k] = i+k;
	}
	
	// Print the int array.
	printf("Your int array contains: ");

	for (int j=0; j<5; j++){
		printf("%d ", in_ar[j]);
	}
	printf("\n");

	// Fill the float array.
	float plus = 0.45;

	for (int k=0; k<5; k++){
		fl_ar[k] = f+k+plus;
		plus = plus + 0.72;
	}

	// Print the float array.
	printf("Your float array contains: ");
	for (int j=0; j<5; j++) {
		printf("%f ", fl_ar[j]);
	}

	printf("\n");
}
