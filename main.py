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
DOWNLOAD_DIRECTORY = "D:/Projects/Graphics/Сертифікати/Квест - День безпекових наук/QR/"
SPREADSHEET_PATH = "D:/Projects/Graphics/Сертифікати/Квест - День безпекових наук/Учасники.xlsx"
WORKSHEET = "Сертифікати"
COLUMN = "B"
INIT_ROW = 1

# STYLE
FORECOLOR = "0f355a"
BACKCOLOR = "fdbb22"


def generate_qrs_from_spreadsheet(api_key):
    start_time = time()
    urls = get_urls_list(SPREADSHEET_PATH, column=COLUMN, start_row=INIT_ROW, worksheet_name=WORKSHEET)

    print("Generating QR Codes...")
    for url in urls:
        qr_file_name = url[-2:] + ".png"
        qr_url = get_generated_qr_url(api_key, url, width="10", forecolor=FORECOLOR, backcolor=BACKCOLOR)
        download_qr_image_by_url(qr_url, qr_file_name, download_directory=DOWNLOAD_DIRECTORY)
    print("DONE!")
    print("Time spent: " + str(time() - start_time))


def generate_single_qr(api_key, file_name, url):
    start_time = time()
    print("Generating QR Code...")
    qr_url = get_generated_qr_url(api_key, url, width="10", forecolor=FORECOLOR, backcolor=BACKCOLOR)
    download_qr_image_by_url(qr_url, file_name, download_directory=DOWNLOAD_DIRECTORY)


def generate_qr_from_base_link(api_key, link_base, start_number, end_number):
    for number in range(start_number, end_number + 1):
        generate_single_qr(api_key, file_name=str(number) + ".png", url=link_base + ('0' + str(number))[-2:])


if __name__ == "__main__":
    API_KEY = input("Enter your API key: ")
    # generate_qrs_from_spreadsheet(API_KEY)
    # generate_single_qr(API_KEY, "p02.png", "https://kztdop.npu.edu.ua/vydani-sertyfikaty/p200429n02")
    generate_qr_from_base_link(api_key=API_KEY, link_base="https://kztdop.npu.edu.ua/vydani-sertyfikaty/q200429n",
                               start_number=55,
                               end_number=72)
