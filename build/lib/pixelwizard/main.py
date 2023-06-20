# main.py
from PIL import Image

def load_image(filename: str) -> Image.Image:
    image = Image.open(filename)
    return image

def main():
    image_path = input("Enter the path to the image file: ")
    image = load_image(image_path)
    pixels = list(image.getdata())
    width, height = image.size
    pixel_array = [pixels[i:i+width] for i in range(0, len(pixels), width)]
    print("Image loaded successfully!")
    print("Dimensions: {} x {}". format(width, height))
    print("PIxel array shape: {} x {}".format(len(pixel_array), len(pixel_array[0])))

if __name__ == '__main__':
    main()
