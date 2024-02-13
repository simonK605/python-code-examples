from PIL import Image, ImageOps


def normalize_image(input_path, output_path=None, show_images=False):
    """
    Normalize the input image using autocontrast and optionally display or save it.

    Parameters:
    - input_path (str): The path to the input image.
    - output_path (str, optional): The path to save the normalized image. If not provided, the image won't be saved.
    - show_images (bool, optional): If True, the original and normalized images will be displayed. Default is False.
    """
    # Open the image using Pillow
    image = Image.open(input_path)

    # Normalize the image using autocontrast
    normalized_image = ImageOps.autocontrast(image)

    # Display the original and normalized images (optional)
    if show_images:
        image.show(title='Original Image')
        normalized_image.show(title='Normalized Image')

    # Save the normalized image (optional)
    if output_path:
        normalized_image.save(output_path)


# Replace 'your_image.jpg' and 'normalized_image.jpg' with your actual paths
image_path = 'your_image.jpg'
output_path = 'normalized_image.jpg'

# Call the function with documentation parameters
normalize_image(input_path=image_path, output_path=output_path, show_images=True)
