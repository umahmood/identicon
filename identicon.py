#!/usr/bin/env python3
import sys
import os
import argparse
import hashlib

from PIL import Image, ImageDraw

def hex_to_rgb(hex_color):
    """
    Converts a 6 digit hex number to RGB.

    @param: hex_color - A 6 digit string with values in the range [a-fA-F0-9].

    @return: a tuple containing 3 integers.
    """
    if not isinstance(hex_color, str):
        raise TypeError("'hex_color' must be of type 'str'.")
    if len(hex_color) != 6:
        raise ValueError("'hex_color' must 6 characters in length (excluding '#') e.g. FF1919.")

    r = int(hex_color[0:2], base=16) 
    g = int(hex_color[2:4], base=16)
    b = int(hex_color[4:6], base=16)

    return (r,g,b)

def draw_image(matrix, hex_color, symmetrical):
    """
    Renders an image were certain pixels are turned colored.

    @param: matrix      - A list of lists containing bools i.e. [[True, False, False, ...], [...], ...]
    @param: hex_color   - The color of each pixel.
    @param: symmetrical - whether the image should be symmetrical.
    
    @return: PIL.Image.Image object.
    """
    SQUARE    = 50 
    size      = (5 * SQUARE, 5 * SQUARE)  
    bg_color  = (214,214,214)
    pixel_on  = hex_to_rgb(hex_color)
    
    if symmetrical:
        for i in range(5):
            matrix[i][4] = matrix[i][0]
            matrix[i][3] = matrix[i][1]
        
    image = Image.new("RGB", size, bg_color)
    draw  = ImageDraw.Draw(image)

    for x in range(5):
        for y in range(5):
            if matrix[x][y]:
                bounding_box = [y * SQUARE, x * SQUARE, y * SQUARE + SQUARE, x * SQUARE + SQUARE]
                draw.rectangle(bounding_box, fill=pixel_on)
    del(draw)
    return image
    
def main():
    usage = """
    python identicon.py -text="hello world"
    python identicon.py -text="Thy bones are marrowless, thy blood is cold."
    python identicon.py -text="bill.gates@microsoft.com" -dir="path/to/folder"
    """
    parser = argparse.ArgumentParser(description="Generate Identicon", usage=usage)
    parser.add_argument("-text", type=str, required=True, help="The text to generate identicon from.")
    parser.add_argument("-dir", type=str, default="out", help="The directory were to save the image.")
  
    args = parser.parse_args()

    if not len(args.text):
        print("error: text must not be empty string.\n")
        parser.print_help()
        sys.exit(1)

    text = args.text
    md5hash = hashlib.md5(text.encode('utf8')).hexdigest()
    color = md5hash[:6]
    matrix = list()
    grid_size = 5
    for i in range(grid_size):
        array = list()
        for j in range(grid_size):
            c = i * grid_size + j + 6
            b = int(md5hash[c], base=16) % 2 == 0
            array.append(b)
        matrix.append(array)

    identicon = draw_image(matrix, color, True)
        
    if not os.path.exists(args.dir):
        os.mkdir(args.dir)

    file_name = text.replace(' ', '-') + ".png"
    file_path = "{0}{1}{2}".format(args.dir, os.sep, file_name)
  
    try:
        identicon.save(file_path, "PNG")
        print("file saved @ {0}".format(file_path))
    except KeyError as e:
        print(e)
    except IOError as e:
        print(e)

if __name__ == '__main__':
    sys.exit(main())
