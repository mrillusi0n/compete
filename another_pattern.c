/************************************\
 * Print the following pattern.     * 
 *                                  * 
 * 5       1                        * 
 *   4   2                          * 
 *     3                            * 
 *   2   4                          * 
 * 1       5                        * 
 *                                  * 
 * Author: @theteachr (Nikhil CSB)  * 
\************************************/

#include <stdio.h>

void print_spaces(int times) {
	for (int i = 0; i < times; i++)
		printf(" ");
}

int main(int argc, char const *argv[])
{
	int lnumber = 4;
	int rnumber = 1;
	int lspace = 0;

	while (lnumber != rnumber) {
		print_spaces(lspace++);
		printf("%d", lnumber);
		print_spaces(lnumber - rnumber - 1);
		printf("%d\n", rnumber);
		--lnumber;
		rnumber++;
	}

	print_spaces(lspace);
	printf("%d\n", lnumber);

	--lnumber;
	rnumber++;

	while (lnumber > 0) {
		print_spaces(--lspace);
		printf("%d", lnumber);
		print_spaces(rnumber- lnumber - 1);
		printf("%d\n", rnumber);
		--lnumber;
		rnumber++;
	}

	return 0;
}
