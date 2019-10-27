from tool import imageToBinary
from tool import binaryToImage

filename = 'image.png'
message = "Hello world"

imss = imageToBinary(filename)
binaryToImage(imss, "imageUpdated.png")
