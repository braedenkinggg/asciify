import cv2
import sys

import pathlib

def to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def scale_img(img, new_width):
    og_height = img.shape[0]
    og_width = img.shape[1]

    aspect_ratio = og_height / float(og_width)
    new_height = int(aspect_ratio * new_width)

    scaled_img = cv2.resize(img, (new_width, new_height))
    return scaled_img

def map_pixels_to_chars(chars):
    pixel_char_map = {}
    char_list = list()

    for i in range(len(chars)):
        char_list.extend((chars[i] * 3))

    for i in range(26):
        for j in range(10):
            pixel_char_map[i * 10 + j] = char_list[i]

    return pixel_char_map

def asciify_img(img_path, new_width=75):
    img = cv2.imread(img_path)

    if img is None:
        sys.exit(f'{img_path} not found')

    img = to_grayscale(img)
    img = scale_img(img, new_width)
    char_map = map_pixels_to_chars('.*o+?>O#@')

    asciified_img = ''
    for i in img:
        temp = []
        for j in i:
            temp.append(char_map[j])
        asciified_img += ' '.join(temp)
        asciified_img += '\n'

    return print(asciified_img)

def main():
    if len(sys.argv) != 2:
        print("""
            ================= ASCIIFY =================

            ASCIIFY is an open-source command line tool 
            used to convert images to ASCII art

            Usage: asciify <path to image> 

            Author: Braeden King
            Version: 1.0.0
        """)
    else:
        asciify_img(sys.argv[1])
        
    sys.exit(0)

if __name__ == '__main__':
    main()