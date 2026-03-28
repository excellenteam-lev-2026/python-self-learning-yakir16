import math
from PIL import Image

def remeber_remember(path):
    img = Image.open(path).convert("RGB")
    pixels = img.load()
    width, height = img.size
    message = ""
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if r < 10 and g < 10 and b < 10:
                message += chr(y)
                break
    return message

if __name__ == "__main__":
    remeber_remember()


#The messege is:
#Place gunpowder beneath the House of Lords. 11/05/1605