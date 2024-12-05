# Ziv-Lempel-algorithm-

This project implements the Ziv-Lempel algorithm on a BMP (Bitmap) image. The program reads the BMP file provided by the user, performs the Ziv-Lempel compression algorithm on its contents, and outputs a new compressed BMP image.

Features

Read BMP Image:
The program reads RGB values from a BMP image pixel by pixel.
Converts each RGB value into binary.

String Conversion:
Constructs a binary string starting with an initial value of 10.
Appends the binary representation of RGB values of the image to this string.
Compression with Ziv-Lempel:

Applies the Ziv-Lempel compression algorithm to the generated binary string.
BMP Image Reconstruction:

Converts the compressed binary data back to RGB values.
Replaces the original pixels with the compressed RGB values in the BMP image.
Saves the new BMP image with the compressed content.

Output:
The output BMP visually shows the impact of compression.
How It Works
Input:
A BMP image file provided by the user.
Process:
Read RGB values of each pixel in the BMP image.
Convert RGB values to binary and concatenate them to a single string.
Compress the binary string using the Ziv-Lempel algorithm.
Replace original RGB values in the image with compressed RGB values.
Save the modified image.
Output:
A new BMP image showing the compressed data. If the compressed data is insufficient to fill all pixels, only a portion of the image will display the compression.

Requirements
Python 3.x
Pillow library (PIL) for image processing.
