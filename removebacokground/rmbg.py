from rembg import remove
from PIL import Image

input_part = "input.jpg"
output_part = "output.png"

input = Image.open(input_part)
output = remove(input)
output.save(output_part)