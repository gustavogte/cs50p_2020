def main():
    #dates_int()
    dates_string()


def dates_int():
    while True:
        try:
            date = input("Date: ")
            month, day, year = date.split("/")
            if int(month) >= 0 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
                f = "{:02d}"
                print(f"{year}-{f.format(int(month))}-{f.format(int(day))}")
                break
        except ValueError:
            True
        except EOFError:
            print()
            break

def dates_string():
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
        try:
            date = input("Date: ")
            month_1, day_1, year_1 = date.split(" ")
            print(month_1, day_1, year_1)
            day = day_1.replace(",","")
            month = [months[int(month_1)]]
            year = int(year)
            print(month, day, year)
            if int(month) >= 0 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
                f = "{:02d}"
                print(f"{year}-{f.format(int(month))}-{f.format(int(day))}")
        except ValueError:
            True
        except EOFError:
            print()
            break
        pass
main()