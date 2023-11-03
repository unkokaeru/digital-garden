from PIL import Image

pixelCount = 0

with Image.open("C:\\Users\\wills\\Documents\\GitHub\\digital-garden\\content\\Q4 and Q5 ATTEMPTS\\architecture.jpg") as img:
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if r > 210 and g > 210 and b > 210:
                pixelCount += 1



print(pixelCount)