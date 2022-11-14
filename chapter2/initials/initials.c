// Implement our own version of strlen

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get string (Full name) from user
    string s = get_string("Full name: ");

    // Prints first initial
    printf("%c", toupper(s[0]));

    // Print the character inside the locker after a space as a capital.
    for (int i = 1; i < strlen(s); i++)
    {
        if (s[i] == ' ')
        {
            printf("%c", toupper(s[i + 1]));
        }
    }

    // Prints a new line
    printf("\n");
}