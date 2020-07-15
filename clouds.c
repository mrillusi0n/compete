#include <stdio.h>

int jump_min(int *clouds, int size)
{
    int step = 0;
    int jumps = 0;

    while (step < size - 1)
    {
        if (clouds[step + 2] == 0)
            step += 2;
        else
            step += 1;

        jumps++;
    }

    return jumps;
}

int main()
{
    int num_clouds = 6;
    int clouds[] = { 0, 0, 0, 0, 1, 0 };

    printf("%d\n", jump_min(clouds, num_clouds));

    return 0;
}

