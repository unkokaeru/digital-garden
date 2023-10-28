"""Simple script to count pixels in a file."""
from pathlib import Path
from PIL import Image


def count_pixels(image_path: Path | str) -> int:
    """Count the number of pixels in an image.

    Args:
        image_path (Path | str): Path to the image file.

    Returns:
        int: The number of pixels in the image.
    """
    with Image.open(image_path) as image_raw:
        return len(image_raw.convert("RGB").getdata())


def count_white_pixels(image_path: Path | str, white_threshold: int = 210) -> int:
    """Count the number of pixels that have all 3 channels greater than `white_threshold`.

    Args:
        image_path (Path | str): Path to the image file.
        white_threshold (int): Threshold for what is considered a white pixel.

    Returns:
        int: The number of light pixels.
    """
    white_pixel_count = 0

    with Image.open(image_path) as image_raw:
        image = image_raw.convert("RGB")

        for pixel in image.getdata():
            if all(channel_value > white_threshold for channel_value in pixel):
                white_pixel_count += 1

    return white_pixel_count


def main():
    input_file = Path("C:\\Users\\wills\\OneDrive\\Desktop\\Q4 and Q5 ATTEMPTS\\architecture.jpg")
    pixel_count = count_pixels(input_file)
    white_pixel_count = count_white_pixels(input_file)

    print(
        f"Number of pixels: {pixel_count}, number of white pixels: {white_pixel_count}."
    )


if __name__ == "__main__":
    main()
