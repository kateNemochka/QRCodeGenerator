from qr_code_generator import *

"""QR Code Generator v1.0
Features:
- generating QR code for a given URL
- using custom colors and size for code generation
- downloading qr code as .png file to specific directory"""

"""TO-DO:
- module that reads a list of URLs from Excel spreadsheet and generates QRs for that list"""


if __name__ == "__main__":
    qr_url = get_generated_qr_url("kztdop.npu.edu.ua/vydani-sertyfikaty/q200429n00",
                                  width="10", forecolor="0f355a", backcolor="fdbb22")
    download_qr_image_by_url(qr_url, "1.png", download_folder="C:/Users/Kate/Desktop/")
