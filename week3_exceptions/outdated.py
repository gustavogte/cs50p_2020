def main():
    while True:
        try:
            date = input("Date: ")
        except EOFError:
            print()
            break
        try:
            dates_string(date)
            if exit:
                break
        except (ValueError, EOFError):

            try:
                dates_int(date)
                if exit:
                    break

            except (ValueError, EOFError):
                pass


def dates_int(date):
    date = date.strip().replace('"', "")
    month, day, year = date.split("/")
    if int(month) >= 0 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
        f = "{:02d}"
        print(f"{year}-{f.format(int(month))}-{f.format(int(day))}")
        return exit
    else:
        main()


def dates_string(date):
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
        "December",
    ]
    month, day, year = date.split(" ")
    day = day.replace(",", "")
    year = year
    if month in months and int(day) >= 1 and int(day) <= 31:
        for i in range(len(months)):
            if months[i] == month:
                month_num = i + 1
        f = "{:02d}"
        print(f"{year}-{f.format(month_num)}-{f.format(int(day))}")
        return exit
    else:
        main()


main()
