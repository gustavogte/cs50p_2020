# faces (🙂 🙁)

def main():
    text = input()
    result = convert(text)
    print(result)

def convert(text):
    text1 = text.replace(":)", "🙂")
    text2 = text1.replace(":(", "🙁")
    return text2

main()



