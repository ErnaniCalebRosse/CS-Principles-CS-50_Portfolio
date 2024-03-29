// Helps a user decide which homework to do first
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    // Prompt the user for the number of courses that they have homework in
    int n = get_int("How many courses do you have homework in? ");

    // Declare an array of courses with the correct number of elements
    int course[n];

    // Prompt the user for their course names and store it in the array
    string courses[n];
    for (int i = 0; i < n; i++)
    {
        courses[i] = get_string("Course: ");
    }

    // Initialize random number generator
    time_t t;
    srand((unsigned) time(&t));

    // Find a random number
    int r = rand() % n;

    // Print out a random course number with index r
    printf("%s, I choose you!\n", courses[r]);

}