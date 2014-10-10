/* Quicksort - by Vikas Yadav
 * Reference - http://www.geeksforgeeks.org/iterative-quick-sort/
 */

#include <stdio.h>
#include <stdlib.h>

//Starting index = start, ending index = end
void swap(int *a, int *b){
  int temp = *a;
  *a = *b;
  *b = temp;
}

int partition(int a[10], int start, int end
  //NOTE: Start and End are absolute index -> starting from 0 ;
  //I took the pivot at end, pivot can be taken at the beginning also with some modification
  //in the code
  if(start<end){
    int pivot = a[end];
    int swap_index = start-1;
    int j = start;
    for(j=start; j<end; j++){
      if(a[j] < pivot){
        swap_index++;
        swap(&a[j], &a[swap_index]);
      }
    }
    swap(&a[end], &a[swap_index+1]);
    return swap_index+1;
  }
  return 0;
}

int quicksort(int a[10], int start, int end){
  if(start<end){
    int p = partition(a, start, end);
    quicksort(a, start, p-1);
    quicksort(a, p+1, end);
  }
}

int main(){
  int i;
  int a[10] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  quicksort(a, 0, 9);
  for(i=0;i<10;i++){
    printf("%d ", a[i]);
  }
}
