/*
 * Bucket Sort
 * Vikas Yadav
 * Reference - http://www.geeksforgeeks.org/bucket-sort-2/
 * 1) Create n empty buckets (Or lists).
 * 2) Do following for every array element arr[i]
 *    a) Insert arr[i] into bucket[n*array[i]]
 * 3) Sort individual buckets using insertion sort.
 * 4) Concatenate all sorted buckets.
 */

#include <stdio.h>
#include <stdlib.h>


struct node{
	int value;
	struct node * next;
};

void insertionSort(int ar_size, int ar[100]){
	int i, j, temp, new;
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


int bucket_sort(node * arr[1000], int n){
	/* arr is the array of elements which you want to sort, and n is the number of elements in it
	 * This function divides the inputs into brackets and sorts them using insertion sort
	 * approach - do the mod of all the inputs to divide them into buckets
	 * After doing the mod, it should also be appended into the respective bucket, buckets
	 * can be represented by linked list,
	 * How do you merge them? Doing insertion sort on them in C is altogether a different problem
	 */

}
int main(){
	int input[100] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
	//Started
}
