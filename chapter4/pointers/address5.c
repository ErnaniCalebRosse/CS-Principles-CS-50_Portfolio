// Store and print an integers address
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%c\n", &s[0]);
    printf("%c\n", &s[1]);
    printf("%c\n", &s[2]);
    printf("%c\n", &s[3]);
    printf("%c\n", &s[4]);
}