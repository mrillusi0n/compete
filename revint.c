#include <stdio.h>
#include <math.h>

int rev(int x)
{
    int res = 0;
    int n_digits = 0;
    int dup = x;

    while (x)
    {
        res = res * 10 + x % 10;
        x /= 10;
    }

    return res;
}

int main()
{
    printf("%d\n", rev(573213);
}









