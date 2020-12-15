#include <stdio.h>
#include <stdlib.h>

int NUM_LINES;
int CHARS_PER_LINE;

char **read_input() {
	char **lines;

	scanf("%d %d", &NUM_LINES, &CHARS_PER_LINE);

	lines = malloc(sizeof(char *) * NUM_LINES + 1);

	for (int i = 0; i < NUM_LINES; ++i) {
		lines[i] = malloc(sizeof(char) * CHARS_PER_LINE + 1);
		scanf("%s", lines[i]);
	}

	return lines;
}

int solve(char **landscape) {
	int trees = 0;
	int idx = 3;

	for (int i = 1; i < NUM_LINES; i++)
		trees += landscape[i][i*idx % CHARS_PER_LINE] == '#';

	return trees;
}

int main() {
	char **lines = read_input();

	printf("%d\n", solve(lines));

	return 0;
}
