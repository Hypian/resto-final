import qrcode # type: ignore

def create_qr(link, filename="qrcode.png"):
    # Create the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Convert to image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save image
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    user_link = input("Enter the link to encode in QR: ").strip()
    create_qr(user_link)
