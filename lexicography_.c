
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(char* a, char* b) {
    char* temp = (char*) calloc(sizeof(char), strlen(a) + 1);

    strcpy(temp, a);
    strcpy(a, b);
    strcpy(b, temp);
}

int get_distinct_letter_count(const char* a) {
    char* letters = (char*) calloc(sizeof(char), 26);

    int dcount = 0;
    int i;

    for (i = 0; a[i] != '\0'; ++i)
        letters[a[i] - 'a']++;

    for (int i = 0; i < 26; ++i)
        if (letters[i] > 1) dcount++;

    return dcount;
}

int lexicographic_sort(const char* a, const char* b) {
    int flag = -1;
    int i;

    for(i = 0;a[i] != '\0' && b[i] != '\0';++i){
        if (a[i] != b[i]) {
            if (a[i] > b[i]) { flag = 1; break; }
            else { flag = 0; break; }
        }
    }

    if (flag == -1)
        flag = (a[i] == '\0') ? 0 : 1;
    
    return flag;
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    int flag = -1;
    int i;

    for(i = 0;a[i] != '\0' && b[i] != '\0';++i){
        if (a[i] != b[i]) {
            if (a[i] < b[i]) { flag = 1; break; }
            else { flag = 0; break; }
        }
    }

    if (flag == -1)
        flag = a[i] == '\0';
    
    return flag;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int count_a = get_distinct_letter_count(a);
    int count_b = get_distinct_letter_count(b);

    if (count_a > count_b) return 1;
    else if (count_a < count_b) return 0;
    else return strlen(a) > strlen(b);
}

int sort_by_length(const char* a, const char* b) {
    return strlen(a) > strlen(b);
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)) {
    for (int i = 0; i < len; ++i)
        for (int j = 0; j < len - i - 1; ++j)
            if (cmp_func(arr[i], arr[i+1])) swap(arr[i], arr[i+1]);
}


int main() 
{
    printf("%d\n", lexicographic_sort_reverse("sbv", "fekls"));
}