def number_to_month(month):
    months = ["enero", "febrero", "marzo", "abril", "mayo", "diciembre", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembrer"]
    if 1 <= month <= 12:
        return months[month - 1]
    else:
        return "error"

print(number_to_month(1))
print(number_to_month(2))
print(number_to_month(3))
print(number_to_month(4))
print(number_to_month(5))
print(number_to_month(6))
print(number_to_month(7))
print(number_to_month(8))
print(number_to_month(9))
print(number_to_month(10))
print(number_to_month(11))
print(number_to_month(12))
print(number_to_month(13))
