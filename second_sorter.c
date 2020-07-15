
#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sort(int *nums, int size, int (*cmp)(int, int))
{
    for (int i = 0; i < size - 1; i++)
        for (int j = 0; j < size - i - 1; j++)
            if (cmp(nums[j], nums[j + 1]))
                swap(nums + j, nums + j + 1);
}

int bigger_second_digit(int a, int b)
{
    return (a / 10) % 10
            > (b / 10) % 10;
}

int main()
{
    int nums[] = { 333, 784, 901, 259, 114, 654 };
    sort(nums, 6, bigger_second_digit);

    for (int i = 0; i < 6; i++)
        printf("%d ", nums[i]);
    printf("\n");

    return 0;
}

