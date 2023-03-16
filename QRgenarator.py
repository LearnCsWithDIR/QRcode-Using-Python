# pip install pillow
# image save for use pillow library

# pip install qrcode
import qrcode

# you can use any link or String data
pass_data = "Welcome to my GitHub \n "
link = "https://github.com/LearnCsWithDIR"

concat = pass_data + link
image = qrcode.make(concat)

image.save("Qr1.png")  # you can save that QR code png , jpg or svg format
