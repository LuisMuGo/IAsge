from scrapping import *
scrapping = scrapping("libro")
for i in range(1,50):
    scrapping.getLinksPage(i)
scrapping.getAllReviewLinks()
scrapping.getComments()
scrapping.writeCsv()
#hola