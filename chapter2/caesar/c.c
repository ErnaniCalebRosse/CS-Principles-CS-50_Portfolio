// Cipher a message by how many characters the user wants

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // TODO: Program was run with just one command-line argument DO LAST

    // TODO: Every character in argv[1] is a digit DO VERY LAST

    // TODO: Convert argv[1] from a `string` to an `int`
    //int key =

    // TODO: Prompt user for plaintext
        // Check to see if the requirements have been met
    // Essentially ensure "./exit <message>"
    if (argc != 2)
    {
        // Print a usage error
        printf("Usage: ./caesar <message>\n");

        // Return an int for main, program stops running
        return 1;
    }

    // TODO: For each character in the plaintext:
        if (argc > 1)
    {
        //
        printf("1");

        // Loop through each command line argument
        for (int i = 1; i < argc; i++)
        {
        printf("%c.", toupper(argv[i][0]));
        }
    }

        // TODO: Rotate the character if it's a letter

        // TODO: Print ciphered message
        printf("nice\n");


    return 0;
}