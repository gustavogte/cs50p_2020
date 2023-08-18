def main():
    i_list()

def i_list():
    items ={}
    while True:
        try:
            item = input().upper()
            if item not in items:
                items[item] = 1
            elif item in items:
                items[item] = items[item] + 1
        except EOFError:
            for item in sorted(items):
                print(items[item], item)
            break
main()