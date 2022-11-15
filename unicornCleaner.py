import csv
import re
from langdetect import detect


class unicornCleaner():
    
    def __init__(self) -> None:
        self.reviews = []
    
    def readAndClean(self):
        with open('C:/Users/luism/Desktop/comments_bueno.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    language = detect(row[0])
                    if language == "es" and len(row[0])>0:
                        self.reviews.append(row)
                except:
                    print("error")
            print(len(self.reviews))
        w = open('C:/Users/luism/Desktop/comments_correcto.csv', "w", encoding='utf-8')
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
        for review in self.reviews:
            review[0] = emoji_pattern.sub(r'', review[0])
            data = f"\"{review[0]}\",\" {review[1]} \"\n"
            w.write(data)
            num = num + 1
            if(num%100 == 0):
                print(num)
        w.close()
        
        
        
            
            
            
            
    
    