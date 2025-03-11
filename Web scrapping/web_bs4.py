from bs4 import BeautifulSoup

with open("file.html","r") as f:
    html=f.read()

soup = BeautifulSoup(html,'html.parser')

print(soup.title.text)




# soup.title
# # <title>The Dormouse's story</title>

# soup.title.name
# # u'title'

# soup.title.string
# # u'The Dormouse's story'

# soup.title.parent.name
# # u'head'

# soup.p
# # <p class="title"><b>The Dormouse's story</b></p>

# soup.p['class']
# # u'title'

# soup.a
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# soup.find_all('a')
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# soup.find(id="link3")
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# for link in soup.find_all('a'):
#     print(link.get('href'))
# # http://example.com/elsie
# # http://example.com/lacie
# # http://example.com/tillie

# print(soup.get_text())
# # The Dormouse's story