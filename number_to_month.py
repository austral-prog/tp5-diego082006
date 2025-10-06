def number_to_month(month):
    months = ["enero", "febrero", "marzo", "abril", "mayo", "diciembre", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembrer"]
    if 1 <= month <= 12:
        return months[month - 1]
    else:
        return "error"
