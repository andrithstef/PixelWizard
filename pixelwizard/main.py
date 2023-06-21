import numpy as np

from .image_loader import load_image, save_image, ImageLoadingError
from . import image_processor
from .help import display_help

def process_commands(image: np.ndarray, image_path: str):
    # values correspond to: (function, nr_args, returns_value)
    commands = {
        "help": (display_help, 0, False),
        "show": (image_processor.show_image, 1, False),
        "flip": (image_processor.flip_image, 1, True),
        "mirror": (image_processor.mirror_image, 1, True),
        "rotate": (image_processor.rotate_image, 2, True),
        "invert": (image_processor.invert_image, 1, True),
        "gaussian_blur": (image_processor.gaussian_blur, 2, True),
        "adjust_saturation": (image_processor.adjust_saturation, 2, True),
        "adjust_hue": (image_processor.adjust_hue, 2, True),
        "detect_edges": (image_processor.detect_edges, 2, True),
        "reset": (load_image, 0, True),
        "save": (save_image, 2, False),
        "exit": (None, 0, False)  # Use None as the function for the exit command
    }

    while True:
        user_input = input("Enter a command: (press 'help' for help)\n")

        # input should be on format: function params
        command_parts = user_input.split()


        if command_parts[0] not in commands:
            print("Unknown command. Try again.")
            continue

        command, num_args, returns_value = commands[command_parts[0]]

        if len(command_parts) - 2 != num_args and len(command_parts)-1 != num_args == 0:
            # if there are any arguments, image is going to be one of them
            # if there are no arguments, the length of command_parts will be one (the function name)
            # otherwise it will be >= 2 (the function name and parameters, image will be added automatically)
            print("Invalid number of arguments. Try again.")
            continue

        if command is None:
            # player asked to exit
            break

        if command_parts[0] == "reset":
            print(f"Resetting image to use image {image_path}")
            image = load_image(image_path)
            continue
        
        if command_parts[0] == "save":
            save_image(image, command_parts[1])
            continue

        if num_args == 0:
            if returns_value:
                image = command()
            else:
                command()
            continue

        args = [image] + list(map(float, command_parts[1:]))
        if returns_value:
            image = command(*args)
        else:
            command(*args)

  
def main():
    image_path = input("Enter the path to the image file: ") 
    try:
        image = load_image(image_path)
        print("Image loaded successfully!")
    except ImageLoadingError as e:
        print("Error: ", str(e))
        return

    process_commands(image, image_path)



if __name__ == '__main__':
    main()
