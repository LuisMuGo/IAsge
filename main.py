from scrapping import *
scrapping = scrapping("libro")
scrapping.getLinksPage(2)
scrapping.getAllReviewLinks()
scrapping.getComments()
scrapping.writeCsv()
#hola