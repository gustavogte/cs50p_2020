import requests
import sys
import json

def main():
    amount = get_amount()

    rate = get_bitIndex()
    total = amount * rate

    print(f"${total:,.4f}")


def get_amount():
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    elif len(sys.argv) != 2:
        print("Too many argument")
        sys.exit(1)
    else:
        try:
            amount = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    return amount

def get_bitIndex():

    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response = r.json()
        bitcoin = response['bpi']['USD']['rate_float']
        return bitcoin

    except requests.RequestException:
        print("Request Exception")
        sys.exit(1)


if __name__ == "__main__":
    main()
