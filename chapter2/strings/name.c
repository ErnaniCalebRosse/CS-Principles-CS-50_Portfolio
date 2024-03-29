// Implement our own version of strlen

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("Full name: ");

    // Initialize a counter
    int counter = 0;

    // Increasing the counter until we see the null terminator
    while(s[counter] != '_')
    {
        counter++;
    }

    printf("Length of first name: %i\n", counter);
}