/*
 * Insertion Sort :-
 * You can see how the array is modifying in each iteration.
 * 1. Insertion Sort is slow but it's faster than selection sort and bubble sort.
 * 2. There's no additional memory requirement in insertion sort.
 * Worst Case O(n^2)
 * Best Case O(n)
 * Average Case O(n^2)
 */
#include <stdio.h>
#include <stdlib.h>

void insertionSort(int ar_size, int ar[100]){
	int i;
	int j;
	int temp;
	int new;

	for(i=1;i<ar_size;i++){
		j=i;
		while(j>0 && ar[j-1]>ar[j]){
			//till i array is sorted (because of the way insertion sort works)
			//We will keep shifting elements to the right till the new element fits
			//inside the sorted list
			temp = ar[j-1];
			ar[j-1] = ar[j];
			ar[j] = temp;
			j--;
		}
		for(new=0;new<ar_size;new++){
			printf("%d", ar[new]);
			if(new!=ar_size-1){
				printf(" ");
			}
			else{
				printf("\n");
			}
		}
	}

}



int main(void) {

	int _ar_size;
	scanf("%d", &_ar_size);
	int _ar[_ar_size], _ar_i;
	for(_ar_i = 0; _ar_i < _ar_size; _ar_i++) {
		scanf("%d", &_ar[_ar_i]);
	}
	insertionSort(_ar_size, _ar);
	return 0;
}
