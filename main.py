from time import sleep
from scrapping import *
from unicornCleaner import unicornCleaner
from ia import ia
#
#for i in range(1, 20):
 #   sleep(1)
  #  scrapping.getLinksPage(i)
# 1 = scrapping
# 2 = IA
# 3 = EXIT


while(True):
    str = input("Menu: ")
    if(str == "1"):
        scrapping = scrapping("anillo")
        for i in range(1, 2):
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