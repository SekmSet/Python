import qrcode
import sys
from PIL import Image


def generate_for_linkedin():
    logo_link = 'linkedin.png'
    logo = Image.open(logo_link)
    url = "https://www.linkedin.com/in/priscilla-joly-44ba9a140/"
    fill = "black"
    background = "white"
    img = generate_qrcode(logo, fill, background, url)
    img.save("qrcode_linkedin.png")


def generate_for_malt():
    logo_link = 'logo_malt.webp'
    logo = Image.open(logo_link)
    url = "https://www.malt.fr/profile/priscillajoly"
    fill = "black"
    background = "white"

    img = generate_qrcode(logo, fill, background, url)
    img.save("qrcode_malt.png")


def generate_qrcode(logo, fill, background, url):
    base_width = 100
    with_percent = (base_width/float(logo.size[0]))
    hight_size = int((float(logo.size[1])*float(with_percent)))

    logo = logo.resize((base_width, hight_size), Image.LANCZOS)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=1,
    )

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color=background)

    position = ((img.size[0] - logo.size[0]) // 2,
                (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, position)
    return img


args = sys.argv
args.pop(0)

for arg in args:
    if arg == 'malt':
        generate_for_malt()
    elif arg == 'linkedin':
        generate_for_linkedin()
    else:
        print('Not supported')
