from bs4 import BeautifulSoup

with open('test.html', 'r', encoding='utf-8') as file:
    html = file.read()
    # html2 = file.readlines()
    # print(html2)
    soup = BeautifulSoup(html, 'html.parser')
    with open('prettify.html', 'w', encoding='utf-8') as data:
        data.write(soup.prettify())
