def display_help():
    print("""Available commands:
- help: 
    Display the available commands.

- show:
    Display the image in a new window.

- mirror:
    Flips the image horizontally.

- flip:
    Flips the image vertically.

- rotate n:
    Rotates the image by n * 90 degrees clockwise.
    (Example usage: rotate 1)

- gaussian blur n:
    Blurs the image using Gaussian blur with standard deviation n.
    (Example usage: gaussian blur 2)

- exit:
    Exit the program.
    (Note: This does not save the image.)
""")
