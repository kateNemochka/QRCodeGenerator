import openpyxl


def get_urls_list(file_path, column, start_row=2, worksheet_name=None) -> list:
    urls_list = []
    wb = openpyxl.open(file_path, read_only=True)
    worksheet = wb[worksheet_name] if worksheet_name else wb.active

    print("Reading URLs...")

    while worksheet[column + str(start_row)].value is not None:
        url = worksheet[column + str(start_row)].value
        print(url)
        urls_list.append(url)
        start_row += 1

    wb.close()
    return urls_list
