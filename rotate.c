
#include <stdio.h>

int SIZE = 3;

void rotate(int **m)
{
    // TODO: consider the corner elements
}

void print_matrix(int **m)
{
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE; j++)
            printf("%d ", **m);
        printf("\n");
    }
}

int main()
{
    int image[SIZE][SIZE];
    int start = 1;

    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++)
            image[i][j] = start++;

    rotate((int **) image);
    print_matrix((int **) &image);

    return 0;
}

