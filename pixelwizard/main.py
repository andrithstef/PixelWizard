import numpy as np

from .image_loader import load_image, ImageLoadingError
from .image_processor import show_image, flip_image, mirror_image
from .help import display_help


def process_commands(image: np.ndarray)->np.ndarray:
    while True:
        command = input("Enter a command: (press 'help' for help)\n")
        if command == "help":
            display_help()
        elif command == "show":
            show_image(image)
        elif command == "flip":
            image = flip_image(image)
        elif command == "mirror":
            image = mirror_image(image)
        elif command == "exit":
            break
        else:
            print("Unknown command. Try again.")
    return image

def main():
    image_path = input("Enter the path to the image file: ") 
    try:
        image = load_image(image_path)
        print("Image loaded successfully!")
    except ImageLoadingError as e:
        print("Error: ", str(e))
        return

    image = process_commands(image)



if __name__ == '__main__':
    main()
