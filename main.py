from qr_code_generator import *
from spreadsheet_reader import *
from time import time

"""QR Code Generator v1.0
Features:
- generating QR code for a given URL
- using custom colors and size for code generation
- downloading qr code as .png file to specific directory
- reading list of URLs from spreadsheet and generating QR codes for them"""


# FILES INFORMATION
DOWNLOAD_DIRECTORY = "D:/Projects/Graphics/Сертифікат квест - День безпекових наук/QR/"
SPREADSHEET_PATH = "D:/Projects/Graphics/Сертифікат квест - День безпекових наук/Учасники Quest.xlsx"
WORKSHEET = "Сертифікати"
COLUMN = "B"
INIT_ROW = 1

# STYLE
FORECOLOR = "0f355a"
BACKCOLOR = "fdbb22"


def generate_qrs_from_spreadsheet():
    start_time = time()
    urls = get_urls_list(SPREADSHEET_PATH, column=COLUMN, start_row=INIT_ROW, worksheet_name=WORKSHEET)

    print("Generating QR Codes...")
    for url in urls:
        qr_file_name = url[-2:] + ".png"
        qr_url = get_generated_qr_url(url, width="10", forecolor=FORECOLOR, backcolor=BACKCOLOR)
        download_qr_image_by_url(qr_url, qr_file_name, download_directory=DOWNLOAD_DIRECTORY)
    print("DONE!")
    print("Time spent: " + str(time() - start_time))


def generate_single_qr(file_name, url):
    start_time = time()
    print("Generating QR Code...")
    qr_url = get_generated_qr_url(url, width="10", forecolor=FORECOLOR, backcolor=BACKCOLOR)
    download_qr_image_by_url(qr_url, file_name, download_directory=DOWNLOAD_DIRECTORY)


if __name__ == "__main__":
    generate_qrs_from_spreadsheet()
    # generate_single_qr("qr.png", "google.com")
