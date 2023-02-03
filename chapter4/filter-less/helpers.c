#include "bmp.h"
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avrg = 1;
    int greyRounding = 1;
    int sepiaRed = 1;
    int sepiaGreen = 1;
    int sepiaBlue = 1;

    // Loop over every pixel Hint** look at yesterday's filter file helpers.c
    // For each row
    for (int i = 0; i < height; i++)
    {
        // For each column
         for (int j = 0; j < width; j++)
         {
            // Find the "average" of the pixel
            avrg = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed);
            avrg = (avrg / 3.0);

            // Update Red, Green, and Blue so that it is grey Rounding
            greyRounding = image[i][j].rgbtBlue;
            greyRounding = image[i][j].rgbtGreen;
            greyRounding = image[i][j].rgbtRed;

         }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // For each row
    for (int i = 0; i < height; i++)
    {
        //For each column
        for (int j = 0; j < width; j++)
        {
            // Calculate new color value using the Sepia formula
            sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;

            // Ensure the result is an integer between 0 and 255, inclusive

            // Update the color values

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // For each row
        // For 1/2 the width
        // Swap pixels on horizontally opposite sides
        // Note* image [i][j] swaps with image [i][width - 1 - j]
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // For each row
        // For each collumn
            // Creating a temp image
            // RGBTRIPLE temp_image[height][width];
            //
    return;
}