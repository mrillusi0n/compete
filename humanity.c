#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

void virusIndices(char *p, char *v) {
    int start = 0;
    int vLen = strlen(v);
    int end = vLen - 1;

    int j, k, l, m;

    int errors;

    char flag[] = "No Match!";

    while (end <= strlen(p) - 1) {
        j = start;
        k = end;
        l = 0;
        m = vLen - 1;
        errors = 0;

        while (errors < 2 && j < k) {
            errors += (p[j++] != v[l++]) + (p[k--] != v[m--]);
        }

        if (j == k) errors += p[j] != v[l];

        if (errors < 2) {
            printf("%d ", start);
            flag[0] = '\0';
        }

        ++start;
        ++end;
    }

    printf("%s\n", flag);
}

int main()
{
    char* t_endptr;
    char* t_str = readline();
    int t = strtol(t_str, &t_endptr, 10);

    if (t_endptr == t_str || *t_endptr != '\0') { exit(EXIT_FAILURE); }

    for (int t_itr = 0; t_itr < t; t_itr++) {
        char** pv = split_string(readline());

        char* p = pv[0];

        char* v = pv[1];

        virusIndices(p, v);
    }

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}
