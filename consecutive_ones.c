/********************************\
 * Given an array of 0's and    *
 * 1's, find the maximum        *
 * consecutive 1's.             *
 *                              *
 *                              *
 * Author: @theteachr           *
\********************************/

#include <stdio.h>

int max_consec_ones(int *seq, int size)
{
    int max_count = 0;
    int running_count = 0;

    for (int i = 0; i < size; i++)
    {
        if (seq[i] == 1)
            running_count++;
        else
            running_count = 0;

        if (running_count > max_count)
            max_count = running_count;
    }

    return max_count;
}

int main()
{
    int bits[] = { 1, 1, 0, 0, 1, 1, 0, 1, 1, 1 };
    printf("%d\n", max_consec_ones(bits, 12));
    return 0;
}


