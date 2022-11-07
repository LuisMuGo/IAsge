import mechanicalsoup
import csv

class scrapping():
    #String word
    #String base
    
    def __init__(self,word) -> None:
        self.base = "https://www.amazon.es/"  #Link inicial
        self.word = word                      #Palabra
        self.pageLinks = []                   #Links de las webs
        self.reviewLinks = []                 #Links review
        self.text_comments = []
        self.stars_comments = []

    def getLinksPage(self,page:int):
        browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup') #Creamos el browser
        url = f"{self.base}s?k={self.word}&page={page}" #URL DE WEB
        browser.open(url) #Abrimos el browser
        print(f"Url: {browser.url}")
        #Obtenemos la pagina
        page = browser.page #Obtenemos web
        
        #Obtenemos los spans que contienen los links
        spans = page.find_all("span", {"class": "rush-component"}) #Buscamos spans contenedores
        print(f"Hola")
        for span in spans:
            #Obtenemos los links
            links = span.find_all("a",{"class":"a-link-normal s-no-outline"}) #Buscamoss links
            for link in links:
                href = link['href']
                href = self.base + href
                self.pageLinks.append(href) #Gardamos datos en una tabla
        #Cerramos objeto browser
        browser.close()
        pass

    def getAllReviewLinks(self):
        browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
        for i in range(len(self.pageLinks)):
            url = self.pageLinks[i]
            browser.open(url)
            page = browser.page
            links = page.find_all("a",{"class":"a-link-emphasis a-text-bold"})
            if(len(links) > 0 ):
                if len(self.reviewLinks) > 3:
                    print("finish")
                    break
                link = links[0]['href']
                link = self.base + link
                self.reviewLinks.append(link)
            pass
        browser.close()
        # Devolvemos tabla con links
    
    def writeCsv(self):
        tabla = []
        for i in range(len(self.text_comments)):
            tabla.append(self.text_comments[i])
            tabla.append(self.stars_comments[i])
            print(self.text_comments[i])
            print(self.stars_comments[i])
            print("----------------")
        print(tabla)
        
        
        
    
    def getComments(self):
        browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')     #Creamos el browser
        for link in self.reviewLinks:
            print("-----------------------")
            print(link)
            host = link                                                                #URL DE WEB
            browser.open(host) 
            #Abrimos el browser
            page = browser.page
            spans = page.find_all("span", {"class": "a-size-base review-text review-text-content"})
            stars = page.find_all("i", {"data-hook": "review-star-rating"})
            if len(spans) == len(stars):
                for star in stars:
                    total_stars = star.find_all("span", {"class": "a-icon-alt"})
                    for i in total_stars:
                        i = (str) (i)
                        self.stars_comments.append(i.replace("<span class=\"a-icon-alt\">", "").replace(" de 5 estrellas</span>",""))

                for span in spans:
                    comments = span.find_all("span")
                    for comment in comments:
                        texto = (str) (comment)
                        self.text_comments.append(texto.replace("<span>", "").replace("</span>", "").replace("<br/>", ""))
            else:
                print("El link (" + link + ") no tiene estrellas")
            
        browser.close()
    
    def getPageLinks(self):
        return self.pageLinks 
    
    def getReviewLinks(self):
        return self.reviewLinks