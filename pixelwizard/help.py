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

- gaussian_blur n:
    Blurs the image using Gaussian blur with standard deviation n.
    (Example usage: gaussian blur 2)

- adjust_saturation n:
    Sets the saturation of the image to the value n.
    n is a value between 0 and 1.
    (Example usage: adjust_saturation 0.5)

- adjust_hue n:
    Sets the hue of the image to the value n.
    n is a value between 0 and 1.
    (Example usage: adjust_hue 0.2)


- detect_edges n:
    Detects edges in the image using an edge detection algorithm.
    The 'n' parameter is the threshold used to determine edges.
    A higher value of 'n' will result in fewer edges being detected.
    (Example usage: detect_edges 50)

- exit:
    Exit the program.
    (Note: This does not save the image.)
""")
