from openpyxl import Workbook
from io import BytesIO

def export_to_excel(headers: list, rows: list):
    workbook = Workbook()
    sheet = workbook.active

    # Write headers
    sheet.append(headers)

    # Write rows
    for row in rows:
        sheet.append(row)

    # Save to bytes
    file_stream = BytesIO()
    workbook.save(file_stream)
    file_stream.seek(0)

    return file_stream
