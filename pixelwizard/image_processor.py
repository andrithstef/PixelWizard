import numpy as np
from PIL import Image
from scipy.signal import convolve2d

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
    return image[:, ::-1] # keep columns untouched, but reverse all rows

def flip_image(image:np.ndarray) -> np.ndarray:
    """
    Flips an image vertically.

    Args:
        image: A numpy array representing an image

    Returns:
        A numpy array representing an image which has been flipped vertically
    """
    print("Flipping image")
    return image[::-1, :] # reverse order of columns, while keeping rows untouched

def rotate_image(image:np.ndarray, nr_times:int) -> np.ndarray:
    """
    Rotates an image by 90 degrees counterclockwise.

    Args:
        image: A numpy array representing an image

    Returns:
        A numpy array representing the original image rotated by 90 degrees
    """
    print(f"Rotating image by {nr_times*90} degrees")
    return np.rot90(image, nr_times)

def invert_image(image:np.ndarray) -> np.ndarray:
    """
    Inverts the rgb values of an image

    Args:
        image: A numpy array representing an image

    Returns:
        A numpy array represenging the original image inverted.
    """
    return -image 

def gaussian_blur(image: np.ndarray, std_dev: float) -> np.ndarray:
    """
    Applies a Gaussian blur to each channel of the image with the given standard deviation
    """
    size = int(2 * np.ceil(2 * std_dev) + 1)  # Calculate the kernel size based on the standard deviation
    kernel = _gaussian_kernel(size, std_dev)  # Generate the Gaussian kernel
    
    blurred_image = np.empty_like(image)
    
    for channel in range(image.shape[2]):
        blurred_image[:, :, channel] = convolve2d(image[:, :, channel], kernel, mode='same')
    
    return blurred_image.astype(np.uint8) 

def _gaussian_kernel(size: int, std_dev: float) -> np.ndarray:
    """
    Generates a Gaussian kernel of the specified size and standard deviation
    """
    kernel = np.fromfunction(lambda x, y: _gaussian_distribution(x, y, std_dev), (size, size))
    kernel /= np.sum(kernel)  # Normalize the kernel to ensure it sums up to 1

    return kernel

def _gaussian_distribution(x: int, y: int, std_dev: float) -> float:
    """
    Calculates the Gaussian value for the given x, y coordinate and standard deviation
    """
    coefficient = 1 / (2 * np.pi * std_dev**2)
    exponent = -(x**2 + y**2) / (2 * std_dev**2)

    return coefficient * np.exp(exponent)
