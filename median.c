#include <stdio.h>
#include <stdlib.h>

void print_arr(int* a, int s)
{
    for (int i = 0; i < s; ++i)
        printf("%d ", a[i]);
    printf("\n");
}

double median_sort(int* aa, int sa, int* ba, int sb)
{
    int i = 0;
    int j = 0;
    int k = 0;

    int* res = (int*) malloc(sizeof(int) * (sa + sb));

    while (i < sa && j < sb)
    {
        if (aa[i] < ba[j])
            res[k++] = aa[i++];
        else
            res[k++] = ba[j++];
    }

    while (i < sa)
        res[k++] = aa[i++];

    while (j < sb)
        res[k++] = ba[j++];

    double median = res[k / 2];

    if (k % 2 == 0)
        median = (median + res[k / 2 - 1]) / 2;

    print_arr(res, k);

    return median;
}

int main()
{
    int a[] = { 1, 2 };
    int b[] = { 0, 1, 3, 4 };

    printf("%.2f\n", median_sort(a, 2, b, 4));
}

