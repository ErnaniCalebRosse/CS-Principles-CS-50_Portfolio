// Calculate the number of pennies someone would have
// If their change doubled every day for a month

#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    // Get starting change in pennies
    int pennies = get_int("Number of pennies to start: ");

    // Get the number of days in the month
    int days = get_int("Number of days in month: ");

    // Double the number of pennies for each of the days
    pennies = pennies * pow(2, days);


    // Print the number of pennies after a month
    printf("You will have %i pennies after one month!\n", pennies);
}