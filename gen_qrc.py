import qrcode # type: ignore

# Créer le QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.theroastalchemist.com')
qr.make(fit=True)

# Enregistrer le QR code
img = qr.make_image(fill_color="black", back_color="white")
img.save("/Users/sofianem8/Desktop/QRCode_Généré.png")
