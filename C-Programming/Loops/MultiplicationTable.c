#include <stdio.h>

int main()
{
    printf("\n multiplication table");

    for (int table=2; table<=1000; table++) //outer loop - controller
    {
        for (int num=table; num <= table*10; num=num + table) // inner loop - work      
        {
            printf("\n %d" , num);
        }
        printf("\n -----------------");
    }
}