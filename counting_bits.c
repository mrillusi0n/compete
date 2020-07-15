/********************************\
 * Count the number of 1's      *
 * in a given integer's         *
 * Binary Representation.       *
 *                              *
 *                              *
 * Author: @theateahcr          *
\********************************/

#include <stdio.h>

int count_bits(int num)
{
    int ones = 0;

    while (num)
    {
        ones += num & 1;
        num = num >> 1;
    }

    return ones;
}

int main()
{
    int nums[] = { 9, 15, 4, 0, 16 };

    for (int i = 0; i < 5; i++)
        printf("%d has %d 1's.\n", nums[i], count_bits(nums[i]));

    return 0;
}

