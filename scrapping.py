import mechanicalsoup

class scrapping():
    #String word
    #String base
    def __init__(self,word) -> None:
        self.base = "https://www.amazon.es/"  #Link inicial
        self.word = word                      #Palabra
        self.pageLinks = []                   #Links de las webs
        self.reviewLinks = []                 #Links review

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
                link = links[0]['href']
                link = self.base + link
                self.reviewLinks.append(link)
            pass
        browser.close()
        # Devolvemos tabla con links
    def getPageLinks(self):
        return self.pageLinks 
    
    def getReviewLinks(self):
        return self.reviewLinks