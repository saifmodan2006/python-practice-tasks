import qrcode
import os

# Input from user
data = input("Enter the URL or text: ").strip() ## .strip method remove extra spaces

# Your exact folder path
folder_path = r"Your File Path"

# File name
file_path = os.path.join(folder_path, "qrcode.png")

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

# Generate image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save(file_path)

print(f"QR Code saved successfully at:\n{file_path}")

