#include <stdio.h>

int steps_to_zero(int num)
{
    int steps = 0;

    while (num)
    {
        if (num % 2)
            num--;
        else
            num = num >> 1;
    }

    return steps;
}

int main()
{
    printf("%d\n", 3547);
}

