/************************************\
**	Find the nth smaller number in	**
**	O(n).							**
**									**
**	Author: @theteachr (Nikhil CSB)	**
\************************************/

#include <stdio.h>

void print_arr(int nums[], int size) {
	for (int i = 0; i < size; ++i)
		printf("%d ", nums[i]);
	printf("\n");
}

void swap(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int n_order_stat(int n, int nums[], int size) {
	// Insert a number at `n` such that
	// nums[i] <= nums[n] for i < n and
	// nums[j] > nums[n] for j > n

	int *smaller = nums + 0;
	int *greater = nums + size - 1;
	int *pivot = nums + n;

	while (smaller < greater) {
		print_arr(nums, size);
		printf("smaller = %d\n", *smaller);
		printf("greater = %d\n", *greater);
		printf("pivot = %d\n", *pivot);

		if (*smaller > *greater) {
			printf("Swapping %d with %d\n", *smaller, *greater);
			swap(smaller, greater);
			print_arr(nums, size);
		}

		if (*pivot > *smaller) {
			printf("Swapping %d with %d\n", *smaller, *pivot);
			swap(pivot, smaller);
			print_arr(nums, size);
		}

		++smaller;
		--greater;
	}

	return nums[n];
}

int main(int argc, char const *argv[])
{
	int nums[] = { 19, 0, 12, 4, 6, 7 };

	n_order_stat(2, nums, 6);
	print_arr(nums, 6);

	return 0;
}



