months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
            break
    except:
        month_1, day_1, year = date.split(" ")
        for i in range(len(months)):
            if month_1 == months[i]:
                month = i + 1
        day = day_1.replace(",", "")
        if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
            break
            print()
            pass #loop again
print(f"{year}-{int(month):02}-{int(day):02}")



