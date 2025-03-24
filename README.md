# Ziv-Lempel BMP Image Compression

This project implements the **Ziv-Lempel compression algorithm** on a BMP (Bitmap) image. It reads a BMP image, compresses its pixel data using the Ziv-Lempel algorithm, and outputs a new compressed BMP image.

---

## 📌 Features

- **Read BMP Image:**  
  Reads RGB values from a BMP image pixel by pixel and converts them into binary.

- **Binary String Conversion:**  
  Constructs a binary string starting with an initial value of `10`, then appends the binary representation of each RGB value from the image.

- **Compression (Ziv-Lempel):**  
  Applies the Ziv-Lempel compression algorithm to the constructed binary string.

- **BMP Image Reconstruction:**  
  Converts the compressed binary back to RGB values and reconstructs the BMP image using these values.

- **Output:**  
  The output BMP visually demonstrates the effects of compression. If the compressed data is insufficient to fill all pixels, only a portion of the image will be modified.

---

## 🔧 How It Works

### Input:
- A BMP image file provided by the user.

### Process:
1. Read the RGB values of each pixel in the BMP image.
2. Convert each RGB value to binary.
3. Concatenate all binary values into a single string (starting with `"10"`).
4. Compress the binary string using the Ziv-Lempel algorithm.
5. Convert compressed binary data back into RGB values.
6. Replace the original RGB values in the image with the compressed RGB values.
7. Save the modified image as a new BMP file.

### Output:
- A new BMP image with pixel values representing the compressed data.

---

## 🛠️ Requirements

- Python 3.x
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/) library for image processing.

Install Pillow with:

```bash
pip install pillow
