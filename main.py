from scrapping import *
scrapping = scrapping("libro")
scrapping.getLinksPage(2)
for i in scrapping.getPageLinks():
    print(f"{i}")
#hola