#include <stdio.h>

void check_chaos(int size, int* q)
{
    int bribes = 0;

    for (int i = 0; i < size; i++)
    {
        int diff = q[i] - (i + 1);

        // printf("%d\n", diff);

        if (diff > 2)
        {
            printf("Too chaotic");
            return;
        }

        if (diff > 0)
            bribes += diff;
        else if (diff < 0)
            bribes += -(diff) / 2;
    }

    printf("%d ", bribes);
}

int main()
{
    int num_people = 8;
    int q[] = { 1, 2, 5, 3, 7, 8, 6, 4 };
    

    check_chaos(num_people, q);
    
    return 0;
}

