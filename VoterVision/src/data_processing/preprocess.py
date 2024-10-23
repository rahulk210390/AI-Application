from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder, image_format='png', dpi=300):
    """
    Convert each page of a PDF into an image.

    Parameters:
    - pdf_path (str): The path to the PDF file.
    - output_folder (str): The directory where the images will be saved.
    - image_format (str): The format of the output images (default is 'png').
    - dpi (int): The resolution of the images (default is 300 DPI).
    
    Returns:
    - List of image file paths.
    """
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF pages to images
    images = convert_from_path(pdf_path, dpi=dpi)

    image_paths = []
    for i, image in enumerate(images):
        image_file_name = f'page_{i+1}.{image_format}'
        image_path = os.path.join(output_folder, image_file_name)
        image.save(image_path, image_format.upper())
        image_paths.append(image_path)

        print(f'Saved {image_file_name}')

    return image_paths

# Example usage
pdf_path = 'data/raw/voterlist.pdf'
output_folder = 'data/processed/images'
image_paths = pdf_to_images(pdf_path, output_folder)

print(f"Images saved in: {output_folder}")