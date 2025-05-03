How it works:

Encodes messages into the least significant bit of pixel color values of a PNG image to hide text (encoding). It can also decode hidden messages by reading these bits. A delimiter marks the end of the message.

How to use:

To encode a message:

python steganography_tool.py encode input.png output.png

You will be prompted to enter the message to hide.

To decode a message:

python steganography_tool.py decode input.png

The hidden message will be printed.
