import re
# I use parenthesis to capture stuff with regex

name = input("What's your name?: ").strip()
"""
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
"""
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
    print(f"hello, {name}")
