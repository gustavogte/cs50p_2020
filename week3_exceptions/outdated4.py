def main():
    while True:
        date = input("Date: ")
        try:
            dates_string(date)
        except ValueError:
            try:
                dates_string(date)
            except ValueError:
                break




def dates_int(date):
    while True:
        try:
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
        "December"
    ]
    while True:
        try:
            month, day, year = date.split(" ")
            day = day.replace(",", "")
            year = year
            if month in months and int(day) >= 1 and int(day) <= 31:
                for i in range(len(months)):
                    if months[i] == month:
                        month_num = i + 1
                f = "{:02d}"
                print(f"{year}-{f.format(month_num)}-{f.format(int(day))}")
            else:
                pass
        except ValueError:
            True
        except EOFError:
            print()
            break
main()