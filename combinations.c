

#include <stdio.h>

void swap(char *a, char *b) {
	char temp = *a;
	*a = *b;
	*b = temp;
}

void print_string(char string[]) {
	for (int i = 0; string[i] != 0; ++i)
		printf("%c", string[i]);
	printf("\n");
}

void print_combs(char letters[], int start) {
	
}

int main(int argc, char const *argv[])
{
	char letters[] = "abc";
	print_combs(letters, 0);
	return 0;
}