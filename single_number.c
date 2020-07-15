
#include <stdio.h>

int single_num(int *nums, int size)
{
    int res = 0;
    int num;

    for (int i = 0; i < size; i++)
        res ^= nums[i];

    return res;
}

int main()
{
    int nums[] = { 4, 1, 2, 1, 2 };
    int size = 5;

    printf("%d\n", single_num(nums, size));
    return 0;
}

