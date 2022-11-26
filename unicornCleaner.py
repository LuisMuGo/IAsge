import csv
import re
from langdetect import detect
import os

class unicornCleaner():
    
    def __init__(self) -> None:
        self.reviews = []
        
    def readAndClean(self):

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"comments_bueno.csv"), encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    language = detect(row[0])
                    if language == "es" and len(row[0])>0:
                        self.reviews.append(row)
                except:
                    print("error")
            print(len(self.reviews))
        w = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"comments_correcto.csv"), "w", encoding='utf-8')
        num = 0
        emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                           "]+", flags=re.UNICODE)
        w.write("\"review\",\"sentiment\"\n")
        for review in self.reviews:
            review[0] = emoji_pattern.sub(r'', review[0])
            replacements = (
            ("á","a"),
            ("é","e"),
            ("í","i"),
            ("ó","o"),
            ("ú","u")
            )
            for a, b in replacements:
                review[0] = review[0].replace(a,b).replace(a.upper(),b.upper())
            # review[0] = normalize().sub(r'', review[0]) # Revisar
            review[1] = review[1].replace(" ","")
            if(review[1] == "1" or review[1] == "2" or review[1] == "3"):
                review[1] = "0"
            elif(review[1] == "4" or review[1] == "5"):
                review[1] = "1"
            data = f"\"{review[0]}\",\"{review[1]}\"\n"
            w.write(data)
            num = num + 1
            if(num%100 == 0):
                print(num)
        w.close()
        
        
        
            
            
            
            
    
    
