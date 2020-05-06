from qr_code_generator import *
from spreadsheet_reader import *
from time import time

"""QR Code Generator v1.0
Features:
- generating QR code for a given URL
- using custom colors and size for code generation
- downloading qr code as .png file to specific directory"""

"""TO-DO:
- module that reads a list of URLs from Excel spreadsheet and generates QRs for that list"""


# FILES INFORMATION
DOWNLOAD_DIRECTORY = "D:/Projects/Graphics" \
                     "/Сертифікат конференція - Безпекова компонента сучасного життєвого середовища/QR/"
SPREADSHEET_PATH = "D:/Projects/Graphics" \
                   "/Сертифікат конференція - Безпекова компонента сучасного життєвого середовища/Учасники.xlsx"
WORKSHEET = "Сертифікат"
COLUMN = "F"
INIT_ROW = 2

# STYLE
FORECOLOR = "0f355a"
BACKCOLOR = "fdbb22"


def generate_codes_from_spreadsheet():
    start_time = time()
    urls = get_urls_list(SPREADSHEET_PATH, column=COLUMN, start_row=INIT_ROW, worksheet_name=WORKSHEET)
    qr_number = 1

    print("Generating QR Codes...")
    for url in urls:
        qr_file_name = str(qr_number) + ".png"
        qr_url = get_generated_qr_url(url, width="10", forecolor=FORECOLOR, backcolor=BACKCOLOR)
        download_qr_image_by_url(qr_url, qr_file_name, download_directory=DOWNLOAD_DIRECTORY)
        qr_number += 1
    print("DONE!")
    print("Time spent: " + str(time() - start_time))


if __name__ == "__main__":
    generate_codes_from_spreadsheet()
