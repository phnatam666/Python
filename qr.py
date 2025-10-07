import qrcode
from PIL import Image
import os


def generate_Qr_code(text, file_name, icon_path=None):
    """
    Generate a QR code with optional center icon.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=6,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#fcfcfc", back_color="#08080C").convert("RGB")

    if icon_path and os.path.exists(icon_path):
        try:
            icon = Image.open(icon_path)
            # Resize icon to fit in the center (e.g., 1/4th of QR code size)
            qr_width, qr_height = img.size
            icon_size = qr_width // 4
            icon = icon.resize((icon_size, icon_size), Image.LANCZOS)
            # Calculate position to paste the icon
            pos = ((qr_width - icon_size) // 2, (qr_height - icon_size) // 2)
            img.paste(icon, pos, mask=icon if icon.mode == "RGBA" else None)
        except Exception as e:
            print(f"Warning: Could not add icon. {e}")

    img.save(file_name)


# To encode a "like" (e.g., a heart emoji) instead of a link:
text = input(" ")  # or use "LIKE" or "👍" or any other symbol/text you want

file_name = "qr_code.png"

icon_path = "like.png"  # Path to your like/heart icon PNG

generate_Qr_code(text, file_name, icon_path)
print(f"QR code saved as {file_name}")
