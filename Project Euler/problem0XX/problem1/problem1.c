#include <stdio.h>

int main(void)
{
	int i, sum;

	i = 0, sum = 0;

	while (i < 1000)
	{
		if (i%3 && i%5);	// true if i isn't divisible by 3 or 5
		else
			sum += i;
		i++;
	}

	printf("%d\n", sum); }
