import numpy as np
from PIL import Image

def show_image(image: np.ndarray): 
    """
    Shows an image in a new window
    
    Args:
        image: A numpy array representing an image

    Returns:
        None
    """
    print("Showing image")
    Image.fromarray(image).show()


def mirror_image(image:np.ndarray) -> np.ndarray:
    """
    Mirrors an image.
    
    Args:
        image: A numpy array representing an image

    Returns:
        A numpy array representing an image which has been flipped horizontally
    """
    print("Mirroring image")
    return np.fliplr(image)

def flip_image(image:np.ndarray) -> np.ndarray:
    """
    Flips an image vertically.

    Args:
        image: A numpy array representing an image

    Returns:
        A numpy array representing an image which has been flipped vertically
    """
    print("Flipping image")
    return np.flipud(image)
