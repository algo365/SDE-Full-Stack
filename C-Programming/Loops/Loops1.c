#include <stdio.h>

int main()
{
    printf("\n forward gear from print 0 t0 10");
    for (int index=0; index<= 10 ; index++)
    {
        printf("\n %d", index);
    }

    printf("\n reverse gear from print 10 t0 0");
    for (int index=10; index >=0 ; index--)
    {
        printf("\n %d", index);
    }
}