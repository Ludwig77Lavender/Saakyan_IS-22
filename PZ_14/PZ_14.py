import re

with open("pazzl.html", "r") as file:
    html_file = file.read()

img_tags = re.findall(r"img", html_file)

img_count = len(img_tags)

print(f'Количество тегов "img": {img_count}')
