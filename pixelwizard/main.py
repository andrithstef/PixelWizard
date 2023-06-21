import numpy as np

from .image_loader import load_image, ImageLoadingError
from .image_processor import gaussian_blur, rotate_image, show_image, flip_image, mirror_image, invert_image
from .help import display_help


def process_commands(image: np.ndarray) -> np.ndarray:
    # values coorespond to: (function, nr_args, returns_value)
    commands = {
        "help": (display_help, 0, False),
        "show": (show_image, 1, False),
        "flip": (flip_image, 1, True),
        "mirror": (mirror_image, 1, True),
        "rotate": (rotate_image, 2, True),
        "invert": (invert_image, 1, True),
        "gaussian_blur": (gaussian_blur, 2, True),
        "exit": (None, 0, False)  # Use None as the function for the exit command
    }

    while True:
        user_input = input("Enter a command: (press 'help' for help)\n")
        command_parts = user_input.split()

        if command_parts[0] not in commands:
            print("Unknown command. Try again.")
            continue

        command, num_args, returns_value = commands[command_parts[0]]

        if len(command_parts) - 2 != num_args and len(command_parts)-1 != num_args == 0:
            print("Invalid number of arguments. Try again.")
            continue

        if command is None:
            break

        if num_args == 0:
            if returns_value:
                image = command()
            else:
                command()
        elif num_args == 1:
            if returns_value:
                image = command(image)
            else:
                command(image)
        else:
            arguments = map(float, command_parts[1:])
            image = command(image, *arguments)

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
