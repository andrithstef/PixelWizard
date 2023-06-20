# main.py
from PIL import Image
from typing import Optional

def load_image(filename: str) -> Optional[Image.Image]:
    try:
        image = Image.open(filename)
        return image
    except (IOError, FileNotFoundError):
        print(f"Error: Failed to open image file '{filename}'. Please make sure the file exists.")
        return None

def main():
    image_path = input("Enter the path to the image file: ")
    image = load_image(image_path)

    if image is None:
        return

    pixels = list(image.getdata())
    width, height = image.size
    pixel_array = [pixels[i:i+width] for i in range(0, len(pixels), width)]
    print("Image loaded successfully!")
    print("Dimensions: {} x {}". format(width, height))
    print("PIxel array shape: {} x {}".format(len(pixel_array), len(pixel_array[0])))

if __name__ == '__main__':
    main()
