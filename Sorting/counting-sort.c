/*
 * Counting Sort
 * Reference :-
 * Counting sort uses a lot of memory but lets you gain speed. A sorting algorithm can be
 * made O(n) using Counting Sort. To reduce the memory requirements of counting sort
 * Radix and bucket sort are used.
 */

#include <stdio.h>
#include <stdlib.h>
#define RANGE 255

int main(){
    int hash[RANGE]; //Assuming that the input ranges from 0 to 255
    int inputs, i, y;
    for(i=0;i<RANGE;i++) hash[i]=0; //Initializing the array to prevent garbage values in the hash
    printf("Enter the number of values:");
    scanf("%d", &inputs);
    printf("Enter values one after separated by a space:");
    for(i=0;i<inputs;i++){
        int temp;
        scanf("%d", &temp);
        hash[temp]+=1; //Incrementing the hash value (This is a simple implementationo f counting sort)
    }

    //hash is already sorted, now printing the values;

    for(i=0;i<RANGE; i++){
        if(hash[i]!=NULL){
          for(y=0;y<hash[i];y++){
            printf("%d ", i);
          }
        }
    }
}
