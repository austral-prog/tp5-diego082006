def number_to_month(month):
    months = ["Janaury", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if 1 <= month <= 12:
        return months[month - 1]
    else:
        return "error"

print(number_to_month(1))
print(number_to_month(12))
print(number_to_month(99))
