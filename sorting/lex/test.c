#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* helpers */

void string_swap(char** a, char** b) {
	char *temp = *a;
	*a = *b;
	*b = temp;
}

int get_dist_chars(const char* string) {
	int *letter_frequency = calloc(26, sizeof(int));
	int dist_char_count = 0;

	for (int i = 0; string[i] != 0; i++) {
		letter_frequency[string[i] - 'a']++;
	}

	for (int i = 0; i < 26; i++)
		if (letter_frequency[i] > 0)
			dist_char_count++;

	return dist_char_count;
}

/* comparators */

int lexicographic_sort(const char* a, const char* b) {
	return strcmp(a, b) > 0;
}

int lexicographic_sort_reverse(const char* a, const char* b) {
	return strcmp(a, b) < 0;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
	int dist_chars_a = get_dist_chars(a);
	int dist_chars_b = get_dist_chars(b);

	if (dist_chars_a == dist_chars_b)
		return lexicographic_sort(a, b);
	return dist_chars_a > dist_chars_b;
}

int sort_by_length(const char* a, const char* b) {
	int len_a = strlen(a);
	int len_b = strlen(b);

	if (len_a == len_b)
		return lexicographic_sort(a, b);
	return len_a > len_b;
}

void string_sort(char** strings, int len, int (*cmp)(const char* a, const char* b)) {
	for (int i = 0; i < len; i++)
		for (int j = 1; j < len - i; j++)
			if (cmp(strings[j-1], strings[j]))
				string_swap(strings + j - 1, strings + j);
}

void print_strings(char** strings, int len) {
	for (int i = 0; i < len; i++)
		printf("%s\n", strings[i]);
	printf("\n");
}

int main(void) {
	char *names[] = {
		"qoi",
		"sbv",
		"wkue",
		"fekls"
	};

	string_sort(names, 4, lexicographic_sort);
	print_strings(names, 4);

	string_sort(names, 4, lexicographic_sort_reverse);
	print_strings(names, 4);

	string_sort(names, 4, sort_by_number_of_distinct_characters);
	print_strings(names, 4);

	string_sort(names, 4, sort_by_length);
	print_strings(names, 4);

	return 0;
}
