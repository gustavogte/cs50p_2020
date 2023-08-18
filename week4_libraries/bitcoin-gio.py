import sys
import requests

# Get value from the command-line
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line is not a number")
        sys.exit(1)

else:
    print("Missing command-line argument")
    sys.exit(1)

# Get current bitcoin price as a float and multiply with the value of the command line

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total_amount = bitcoin * value
    print(f"${total_amount:,.4f}")

except requests.RequestException:
    print("Request Exception")
    sys.exit(1)

