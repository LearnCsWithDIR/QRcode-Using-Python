# pip install pillow
from PIL import Image  # image save for use pillow library


from pyzbar import pyzbar # read BarCode or QRcode to use pyzbar

image = Image.open("Qr1.png")

output = pyzbar.decode(image)
print(output[0][0].decode('utf-8'))
