#include <stdio.h>
#include <stdlib.h>


char* defang(char* address)
{
    char *res = malloc(sizeof(char) * 22);
    int i = 0;
    int j = 0;

    while (address[i])
    {
        if (address[i] == '.')
        {
            res[j++] = '[';
            res[j++] = '.';
            res[j] = ']';
        } else res[j] = address[i];

        i++;
        j++;
    }

    res[j] = 0;

    return res;
}

int main()
{
    char *ip = "143.101.208.184";

    printf("%s\n", defang(ip));

    return 0;
}

