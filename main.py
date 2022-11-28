from time import sleep
from scrapping import *
from unicornCleaner import unicornCleaner
from ia import ia

# 1 = scrapping
# 2 = IA
# 3 = EXIT

while(True):

    print("1 = scrapping \n" +
            "2 = IA \n" +
            "3 = EXIT \n")
    str = input("Menu: ")
    if(str == "1"):
        word = input("Articulo a buscar: ")
        paginas = int(input("Numero de paginas a buscar: "))
        
        scrapping = scrapping(word)
        paginas = paginas + 1
        for i in range(1, paginas):
            sleep(1)
            scrapping.getLinksPage(i)
        scrapping.getAllReviewLinks()
        scrapping.getComments()
        scrapping.writeCsv()

        unicornCleaner = unicornCleaner()
        unicornCleaner.readAndClean()
    elif(str == "2"):
        ia = ia()
    elif(str == "3"):
        break