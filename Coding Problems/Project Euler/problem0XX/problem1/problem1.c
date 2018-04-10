#include <stdio.h>

int main(void)
{
	int i, sum = 0;

	for (i = 0; i < 1000; i ++)
	{
		if (i%3 && i%5);	// True if i isn't divisible by 3 or 5
		else
			sum += i;
	}

	printf("%d\n", sum); 
}
