import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=20,
                   border=2)

qr.add_data("https://github.com/GrandeTB")
qr.make(fit=True)

img = qr.make_image(fill_color="dark", back_color="white")
img.save("MyGithubQRCode.png")

