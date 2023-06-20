# main.py
from PIL import Image
from typing import Optional
import numpy as np

def load_image(filename: str) -> Optional[np.ndarray]:
    """
    Loads an image from a file and returns it as a numpy array.

    Args:
        filename (str): The path to the image file.

    Returns:
        Optional[np.ndarray]: The image as a numpy array, or None if the image could not be loaded.
    """
    try:
        image = Image.open(filename)
        return np.array(image)
    except (IOError, FileNotFoundError):
        print(f"Error: Failed to open image file '{filename}'. Please make sure the file exists.")
        return None

def main():
    image_path = input("Enter the path to the image file: ")
    image = load_image(image_path)

    if image is None:
        return

    width, height,_ = image.shape
    print("Image loaded successfully!")
    print("Dimensions: {} x {}". format(width, height))
    print("PIxel array shape: {} x {}".format(len(image), len(image[0])))

    img = Image.fromarray(image)
    img.show()

if __name__ == '__main__':
    main()
