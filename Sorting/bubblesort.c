//Name : T.Kaushik
//Sorting : Bubble Sort
//Roll no : IMT2013054
#include <stdio.h>
int main()
{
	long long int  array[200000] , number_of_elements, i, j,temp,count=0;
	for(i=0;i<200000;i++)
	{
		array[i]=rand();
		count++;
	}
	number_of_elements=count;
	
		for (i = 0 ; i <  number_of_elements-1  ; i++)
		{
			for (j = 0 ; j < number_of_elements - i-1 ; j++)
			{
			if (array[j] > array[j+1])
			{
				/* Swapping */
				temp = array[j];
				array[j] = array[j+1];
				array[j+1] = temp;
			}		
			}	
		}	
		 printf("Sorted list in ascending order:\n");
        for ( i = 0 ; i < number_of_elements ; i++ )
	{
                printf("%llu\n", array[i]);
	}	
}

