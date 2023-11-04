#include <stdio.h>
#include <stdlib.h>

int main() {
    char filename[256];

    if (scanf("%255s", filename) != 1) {
        printf("Error: Could not read the log file name.\n");
        return 1; // Exit with an error code
    }

    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error: Could not open file.\n");
        return 1; // Exit with an error code
    }

    char buffer[1024];
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    fclose(fp);

    return 0; // Exit with success
}
