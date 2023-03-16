import qrcode
qr = qrcode.QRCode(box_size=15,border=8)

pass_data = "Welcome to my GitHub \n "
link = "https://github.com/LearnCsWithDIR"

concat = pass_data + link

qr.add_data(concat)
qr.make(fit=True)

image = qr.make_image(fill_color = "#5B50C7" , back_color = "white") # you can use any colors for QR code
image.save("Qr2.jpg")