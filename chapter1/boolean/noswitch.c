/**
 * Get an answer from the user
 */

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for a character answer
    char answer = get_char("Answer (Y/N): ");

    // Confirming user's input
    if (answer == 'Y')
    {
        printf("You said Yes\n");
    }
    else if (answer == 'N')
    {
        printf("You said No\n");
    }
    else
    {
        printf("Please provide an appropriate response\n");
    }
}