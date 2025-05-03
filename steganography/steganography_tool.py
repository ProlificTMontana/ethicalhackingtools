from PIL import Image

import sys


def to_bin(data):

    """Convert data (str or bytes) to a binary string"""

    if isinstance(data, str):

        return ''.join([format(ord(i), '08b') for i in data])

    elif isinstance(data, bytes) or isinstance(data, bytearray):

        return ''.join([format(i, '08b') for i in data])

    else:

        raise TypeError("Input must be string or bytes")


def encode(image_path, output_path, message):

    img = Image.open(image_path)

    binary_msg = to_bin(message) + '1111111111111110'  # delimiter

    _, width = img.size

    pixels = list(img.getdata())


    new_pixels = []

    msg_index = 0

    for pixel in pixels:

        if msg_index < len(binary_msg):

            new_pixel = []

            for color in pixel[:3]:

                if msg_index < len(binary_msg):

                    color_bin = format(color, '08b')

                    new_color = int(color_bin[:-1] + binary_msg[msg_index], 2)

                    new_pixel.append(new_color)

                    msg_index += 1

                else:

                    new_pixel.append(color)

            if len(pixel) == 4:

                new_pixel.append(pixel[3])

            new_pixels.append(tuple(new_pixel))

        else:

            new_pixels.append(pixel)


    img.putdata(new_pixels)

    img.save(output_path)

    print(f"Message encoded and saved to {output_path}")


def decode(image_path):

    img = Image.open(image_path)

    pixels = list(img.getdata())


    binary_data = ""

    for pixel in pixels:

        for color in pixel[:3]:

            binary_data += bin(color)[-1]


    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]

    message = ""

    for byte in all_bytes:

        if byte == '11111110':  # delimiter found

            break

        message += chr(int(byte, 2))

    print("Decoded message:")

    print(message)



def main():

    if len(sys.argv) < 3:

        print("Usage:")

        print("  Encode: python steganography_tool.py encode <input_image.png> <output_image.png>")

        print("  Decode: python steganography_tool.py decode <input_image.png>")

        return


    op = sys.argv[1].lower()

    if op == "encode":

        if len(sys.argv) < 4:

            print("Provide input and output image filenames.")

            return

        message = input("Enter the message to hide: ")

        encode(sys.argv[2], sys.argv[3], message)

    elif op == "decode":

        decode(sys.argv[2])

    else:

        print("Unknown operation. Use encode or decode.")


if __name__ == "__main__":

    main()
