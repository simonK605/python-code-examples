from PIL import Image


def create_empty_png(n, m, output_filename='empty_image.png'):
    """
    Create an empty PNG image with the specified dimensions.

    Args:
    n (int): Width of the image in pixels.
    m (int): Height of the image in pixels.
    output_filename (str, optional): Name of the output file. Default is 'empty_image.png'.

    Returns:
    None
    """
    # Create a new blank image
    image = Image.new('RGBA', (n, m), (255, 255, 255, 0))

    # Save the image to a file
    image.save(output_filename)


# Example usage:
create_empty_png(300, 200, 'empty_image.png')