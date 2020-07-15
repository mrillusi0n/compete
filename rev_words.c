/************************************\
**	Reverse the order of words in	**
**	in a given sentence.			**
**	(Naive Approach)				**
**									**
**	Author: @theteachr (Nikhil CSB)	**
\************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap_strings(char **s, char **t) {
	char *temp = *s;
	*s = *t;
	*t = temp;
}

void rev_words(char *sentence, int size) {
	char *rev = malloc(sizeof(char) * size);

	char *fword = sentence;
	char *lword;

	while ((fword = strchr(++fword, ' ')))
		lword = ++fword;

	printf("%s\n", lword);
}

int main(int argc, char const *argv[])
{
	char s[] = { 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' };
	
	rev_words(s, 22);
	printf("%s\n", s);
	return 0;
}