from PIL import Image

# 'darkest' to 'brightest'
ascii_gradient = ['@', '%', '#', '*', '+', '=', '-', ':', '.', ' ']
# 'brightest' to 'darkest' (useful when text is brighter than background color!)
ascii_gradient_inverted = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']


# Convert image to grayscale and convert to desired size
def grayscale_and_resize(image, new_width):
    width, height = image.size
    height_width_ratio = height / width
    new_height = int(new_width * height_width_ratio)
    image = image.resize((new_width, new_height))
    return image.convert("L")

# Find image from file path
def find_image(file_path):
    return Image.open(file_path)

# Convert image to ASCII
def convert_image_to_ascii(file_path, inverted=False, width=100):
    
    print(f"Processing {file_path}...")
    
    image = find_image(file_path)
    image = grayscale_and_resize(image=image, new_width=width)
    
    # build unformatted string of pixel data (brightness)
    ascii_string = ""
    pixel_data = image.getdata()
    for pixel in pixel_data:
        if inverted:
            ascii_string += ascii_gradient_inverted[min(9, (pixel // 25))]
        else:
            ascii_string += ascii_gradient[min(9, (pixel // 25))]
    
    # add line breaks
    width = image.width
    ascii_image = ""
    for i in range(len(ascii_string)):
        if(i % width == 0):
            ascii_image += "\n" 
        ascii_image += ascii_string[i]
            
    print(ascii_image)


# Example usage
convert_image_to_ascii("C:/Users/rmhop/Desktop/blue.jpg", inverted=False, width=100)