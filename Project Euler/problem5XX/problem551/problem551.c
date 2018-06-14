#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	if (argc != 2)
	{
		printf("ERROR -- not enough arguments\n");
		exit(0);
	}

	int n;
	n = atoi(*(argv+1));

}
