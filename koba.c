#include <stdio.h>

int main() {
    char ones = '0';
    char tens = '0';

    for (int j = 1; j < 10; j++)
    {
        for (int i = '0'; i <= '9'; ++i)
            printf("%c%c\n", tens, ones++);

        ones = '0';
        tens++;
    }

    printf("%c%c\n", tens, ones++);
}

