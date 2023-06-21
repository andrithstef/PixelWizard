import numpy as np
from skimage import color
from PIL import Image
from scipy.signal import convolve2d, convolve

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
    print("inverting image")
    return -image 

def gaussian_blur(image: np.ndarray, std_dev: float) -> np.ndarray:
    """
    Applies a Gaussian blur to each channel of the image with the given standard deviation
    """
    print("Blurring image")
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


def adjust_saturation(image:np.ndarray, saturation: float) -> np.ndarray:
    """
    Adjusts the saturation of an RGB image.

    Args:
        image (np.ndarray): The input RGB image.
        saturation (float): The new saturation of the image. 

    Returns:
        np.ndarray: The adjusted RGB image with modified saturation.

    Note:
        - The input image should have shape (height, width, 3).
        - The input image should have values in the range [0, 255].
        - The returned image will have integer values in the range [0, 255].
    """
    print(f"adjusting saturation to {saturation}")
    # Convert image to HSV color space
    hsv_image = color.rgb2hsv(image)

    # Separate the HSV components
    hue = hsv_image[:, :, 0]
    saturation_base = np.ones_like(hsv_image[:, :, 1])
    value = hsv_image[:, :, 2]

    # Modify the saturation component
    modified_saturation = saturation_base*np.clip(saturation, 0, 1)

    # Combine the modified components back into an HSV image
    modified_hsv_image = np.stack((hue, modified_saturation, value), axis=-1)

    # Convert the modified HSV image back to RGB color space
    modified_rgb_image = color.hsv2rgb(modified_hsv_image)

    # Convert the floating-point RGB image to integers
    modified_rgb_image_int = (modified_rgb_image * 255).astype(np.uint8)

    return modified_rgb_image_int

def adjust_hue(image:np.ndarray, hue: float) -> np.ndarray:
    """
    Adjusts the hue of an RGB image.

    Args:
        image (np.ndarray): The input RGB image.
        hue (float): The new hue of the image in degrees. 

    Returns:
        np.ndarray: The adjusted RGB image with modified hue.

    Note:
        - The input image should have shape (height, width, 3).
        - The input image should have values in the range [0, 255].
        - The returned image will have integer values in the range [0, 255].
    """
    print(f"Adjusting hue to {hue}")
    # Convert image to HSV color space
    hsv_image = color.rgb2hsv(image)

    # Separate the HSV components
    hue_base = np.ones_like(hsv_image[:, :, 0])
    saturation = hsv_image[:, :, 1]
    value = hsv_image[:, :, 2]

    # Modify the hue component
    modified_hue = hue_base*(hue%360)

    # Combine the modified components back into an HSV image
    modified_hsv_image = np.stack((modified_hue, saturation, value), axis=-1)

    # Convert the modified HSV image back to RGB color space
    modified_rgb_image = color.hsv2rgb(modified_hsv_image)

    # Convert the floating-point RGB image to integers
    modified_rgb_image_int = (modified_rgb_image * 255).astype(np.uint8)

    return modified_rgb_image_int

def detect_edges(image: np.ndarray, threshold: float) -> np.ndarray:
    """
    Detects edges in the image using an edge detection algorithm.

    Args:
        image (np.ndarray): The input image as a NumPy array.
        threshold (float): The threshold value used to determine edges.
            Higher values result in fewer edges being detected.

    Returns:
        np.ndarray: The edge-detected image as a NumPy array.

    Note:
        This function applies an edge detection algorithm to the image,
        highlighting regions with significant intensity changes. The
        detected edges are determined based on the given threshold value.
    """
    # Convert the image to grayscale
    grayscale = np.mean(image, axis=2)

    # Define the Sobel operator kernels
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Perform convolution with the Sobel kernels
    gradient_x = convolve(grayscale, sobel_x)
    gradient_y = convolve(grayscale, sobel_y)

    # Compute the gradient magnitude
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    # Normalize the gradient magnitude to the range [0, 255]
    gradient_magnitude = (gradient_magnitude / np.max(gradient_magnitude)) * 255

    # Apply thresholding to obtain binary edges
    edges = np.zeros_like(gradient_magnitude)
    edges[gradient_magnitude > threshold] = 255

    return edges.astype(np.uint8)
