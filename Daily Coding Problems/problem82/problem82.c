#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

char *read7(int fd)
{
    char *s = (char*) malloc(sizeof(char) * 7);
    int size = read(fd, s, 7);

    return s;
}

char *readN(int fd, int n)
{
    int r, q, i;       // remainder quotient
    r = n % 7;
    q = n / 7;

    char *s, *cursor, *ret;
    s = (char*) malloc(sizeof(char) * (n + 1));
    cursor = s;
    ret = NULL;

    // Copy 7 bytes at a time for q number of times
    for (i = 0; i <= q; i++) {
        // Read 7 bytes, then copy it into the cursor
        ret = read7(fd);
        strcpy(cursor, ret);

        // Free the return value
        free(ret);
        ret = NULL;
        cursor += 7;
    }

    cursor -= 7;

    // Handle adding a null character to the end
    *(cursor + r) = 0;

    return s;
}

int main(int argc, char **argv)
{
    // Handle the case of not enough arguments
    if (argc != 3) {
        printf("Error : program requires 3 arguments\n");
        return 0;
    }

    char *filename, *out;
    filename = argv[1];
    int n, r, q;

    n = atoi(argv[2]);

    // Attempt to open the file
    int fd = open(filename, O_RDONLY);

    if (fd < 0) {
        printf("Error : file doesn't exist\n");
        return 0;
    } else if (n <= 0) {
        printf("Error : n must be positive\n");
        return 0;
    }

    out = readN(fd, n);
    printf("%s\n", out);

    // Close f
    close(fd);
    return 0;
}