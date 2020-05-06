import requests

"""QR Codes generation using API service
http://qrcode.youlikeshare.com
found at https://rapidapi.com/ resource"""


API_URL = "https://pierre2106j-qrcode.p.rapidapi.com/api"


# GENERATING QR CODE AND GETTING ITS URL
def get_generated_qr_url(text, type="url", width="10",
                     backcolor="ffffff", forecolor="000000") -> str:
    querystring = {
        "backcolor": backcolor,
        "pixel": width,
        "ecl": "H",
        "forecolor": forecolor,
        "type": type,
        "text": text
    }

    headers = {
        "x-rapidapi-host": "pierre2106j-qrcode.p.rapidapi.com",
        "x-rapidapi-key": "f8bb72f15cmshb9c497207c8216ap12c4d4jsn38b4d6da75a3"
    }

    response = requests.request("GET", API_URL, headers=headers, params=querystring)
    print(response.text)
    return response.text


# DOWNLOADING QR CODE IMAGE
def download_qr_image_by_url(url, file_name, download_directory="C:/Users/Kate/Downloads/"):
    response = requests.get(url)
    if response.status_code == 200:
        with open(download_directory+file_name, 'wb') as f:
            f.write(response.content)
