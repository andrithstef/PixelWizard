from PIL import Image
import numpy as np

class ImageLoadingError(Exception):
    pass

def load_image(filename: str) -> np.ndarray:
    """
    Loads an image from a file and returns it as a numpy array.

    Args:
        filename (str): The path to the image file.

    Returns:
        np.ndarray: The image as a numpy array.

    Throws:
        ImageLoadingError: If the image file could not be loaded.
    """
    try:
        image = Image.open(filename)
        return np.array(image)
    except (IOError, FileNotFoundError):
        raise ImageLoadingError(f"Failed to open image file '{filename}'. Make sure file exists.")

def save_image(image: np.ndarray, path: str):
    """
    Saves the image to the given path.

    Args:
        image (np.ndarray): The image to be saved.
        path (str): The path to the save location
    """
    print(f"Saving image to path {path}")
    Image.fromarray(image).save(path, format='png')
