from PIL import Image, ImageFilter
image = Image.open(r"image/test3.png")
image = image.filter(ImageFilter.GaussianBlur)
image.show()