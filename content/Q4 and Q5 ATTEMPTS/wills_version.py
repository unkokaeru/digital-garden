from pathlib import Path
from PIL import Image

def count_pixels(image_path: str) -> int:
    # Open the image file and convert it to RGB format
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        width, height = img.size

        # Calculate the total number of pixels in the image
        num_pixels = width * height

        return num_pixels

def count_white_pixels(image_path: str) -> int:
    # Open the image file and convert it to RGB format
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        pixelMap = img.load()

        # Loop through each pixel in the image
        num_white_pixels = 0
        for row in range(img.size[0]):
            for col in range(img.size[1]):
                # Check if the pixel is white
                r, g, b = pixelMap[row, col]
                if r > 210 and g > 210 and b > 210:
                    # If the pixel is white, increment the count
                    num_white_pixels += 1

        return num_white_pixels

input_file = Path("C:\\Users\\wills\\Documents\\GitHub\\digital-garden\\content\\Q4 and Q5 ATTEMPTS\\architecture.jpg")

pixelCount = count_pixels(input_file)
whitePixelCount = count_white_pixels(input_file)

print(f'Number of pixels: {pixelCount}, number of white pixels: {whitePixelCount}.')