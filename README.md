# steganography
# Image Steganography Tool

This Python script implements a simple image steganography tool, allowing users to encode and decode text messages within PNG images.

## Features

* **Message Encoding:** Hides text messages within the blue channel of image pixels.
* **Message Decoding:** Extracts hidden text messages from encoded images.
* **Simple Command-Line Interface:** Easy to use for encoding and decoding operations.
* **Delimiter-Based Extraction:** Uses a newline character (`\n`) to mark the end of the encoded message.

## Requirements

* Python 3.x
* Pillow (PIL) library (`pip install Pillow`)

## Usage

1.  **Clone the repository or download the script.**
2.  **Install the required Pillow library:**
    ```bash
    pip install Pillow
    ```
3.  **Run the script:**
    ```bash
    python your_script_name.py
    ```
4.  **Follow the prompts:**
    * Choose whether to encode or decode.
    * Enter the path to the image file.
    * If encoding, enter the message to hide.

## Example
Do you want to encode or decode? (encode/decode): encode
Enter the path of the image: my_image.png
Enter the message to encode: Secret message!
Message encoded successfully!


Do you want to encode or decode? (encode/decode): decode
Enter the path of the image with the encoded message: encoded_image.png
Decoded message: Secret message!
## Implementation Details

* The script uses the Pillow (PIL) library to manipulate image pixels.
* The message is encoded by storing the ASCII value of each character in the blue component of the image's pixels.
* A newline character is appended to the message before encoding, and is used as a delimeter for decoding.
* The encoded image is saved as `encoded_image.png`.

## Notes

* This is a basic steganography implementation. More advanced techniques offer greater security and capacity.
* Using lossless image formats like PNG is recommended to prevent data loss.
* The capacity of the hidden message is limited by the image's dimensions.
* This method is easily detectable.

## Author

[Ayush/Ayush-0123]
