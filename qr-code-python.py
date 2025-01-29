import qrcode
from PIL import Image  # Image processing library

# List of links to convert to QR Codes
links = {
    "aminetriki_site": "https://aminetriki.com.tn",
    "aminetriki_youtube": "https://www.youtube.com/@aminetrikitv"
}

# QR Code Settings
qr_settings = {
    "version": 1,
    "error_correction": qrcode.constants.ERROR_CORRECT_H,
    "box_size": 10,
    "border": 4,
}

# Create and save QR Codes with size 300x300 pixels
for name, link in links.items():
    # Create QR Code object
    qr = qrcode.QRCode(**qr_settings)
    
    # Add data (link)
    qr.add_data(link)
    qr.make(fit=True)
    
    # Generate QR Code Image Using PIL
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Make sure the image is 300x300 pixels in size.   
    img = img.resize((300, 300), Image.LANCZOS)
    
    # Save the image with the desired extension
    img.save(f"{name}.png", format="PNG")

print("QR Codes generated successfully!")
