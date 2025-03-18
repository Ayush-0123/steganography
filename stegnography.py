from PIL import Image

# Function to encode a message into an image
def encode_message(img_path, message):
    img = Image.open(img_path)
    pixels = img.load()
    width, height = img.size
    message += "\n"  # Adding a delimiter to mark the end of the message

    char_index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if char_index < len(message):
                char = message[char_index]
                char_val = ord(char)
                pixels[x, y] = (r, g, char_val)
                char_index += 1
            else:
                img.save("encoded_image.png")
                return "Message encoded successfully!"

# Function to decode a message from an image
def decode_message(img_path):
    img = Image.open(img_path)
    pixels = img.load()
    width, height = img.size

    decoded_message = ""
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if b != 0:  # Non-zero blue component indicates encoded message
                decoded_message += chr(b)

    return decoded_message

# Example usage
def main():
    choice = input("Do you want to encode or decode? (encode/decode): ")

    if choice.lower() == "encode":
        img_path = input("Enter the path of the image: ")
        message = input("Enter the message to encode: ")
        print(encode_message(img_path, message))
    elif choice.lower() == "decode":
        img_path = input("Enter the path of the image with the encoded message: ")
        print("Decoded message:", decode_message(img_path))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
