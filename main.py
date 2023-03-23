import sys
import cv2
import numpy as np


class ArtConverter:
    def __init__(self, path):
        self.path = path
        self.image = self.get_image()
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]

        self.ASCII_CHARS = ' .",:;!~+-xmo*#W&8@'
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)

    def compose_converted_image(self):
        #TODO: сделать так, чтобы на выход подавалась картинка, а не txt-файл
        ascii_txt = open(r"C:\Users\karak\Desktop\ascii.txt", 'w', encoding='utf8', errors='ignore')

        char_indices = self.image // self.ASCII_COEFF
        for i in range(0, self.image.shape[0]):
            for j in range(0, self.image.shape[1]):
                char_index = char_indices[i, j]
                if char_index:
                    ascii_txt.write(self.ASCII_CHARS[char_index])
                else:
                    ascii_txt.write(" ")
            ascii_txt.write("\n")

        # cv2.imwrite(r"C:\Users\karak\Desktop\converted.jpg", ascii_txt)

    def get_image(self):
        try:
            self.cv2_image = cv2.imread(self.path)
        except TypeError:
            print("ERROR: path not found or not assigned. Please type path to the picture in argv")
            sys.exit()

        gray_image = cv2.cvtColor(self.cv2_image, cv2.COLOR_BGR2GRAY)
        return gray_image


if __name__ == '__main__':
    try:
        test = ArtConverter(sys.argv[1])
    except IndexError:
        print("ERROR: path not found or not assigned. Please type path to the picture in argv")
        sys.exit()

    test.compose_converted_image()
