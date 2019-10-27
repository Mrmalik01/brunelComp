from stegano import lsb

#secret = lsb.hide("image.png", "Hello World")
#secret.save("ssss.png")

clear_message = lsb.reveal("encodedImage.png")
print(clear_message)