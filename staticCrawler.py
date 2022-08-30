from dis import findlinestarts
import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment

class StaticCrawler:
    bigTopic=[]
    url = 'https://www.w3schools.com/python/'
    def __init__(self) : 
        pass 
        
        
    
    
    def contribute(self):
        r = requests.get(self.url)
        soup = bs(r.content,'html.parser')
        self.findingTopics(soup,'hich')
        
    def findingTopics(self,soup,sub):
        topic = soup.find(id= 'leftmenuinnerinner')
        bigTopics= topic.findAll('h2',class_="left")
        counter=1
        for element in bigTopics:
            print(str(counter) + '- ' + element.text)
            counter+=1
        print('----------------')
        theChosenOne = self.userInputManager(counter,sub)
        
        counter2=1
        temp = bigTopics[theChosenOne-1]
        list=[]
        while(True):
            if temp.nextSibling != bigTopics[theChosenOne] :
                if isinstance(temp,Comment):
                    temp = temp.nextSibling
                    continue
                if temp.text!= '\n':
                    list.append(temp)
                temp = temp.nextSibling
            else:
                break
        
        for items in list:
            if items.name != 'div':
                print(str(counter2) + '- ' + items.text)
                counter2+=1
        print('----------------')
        theChosenOne = self.userInputManager(counter2-1,sub)
        temp = list[theChosenOne-1]
        if list[theChosenOne].name != 'div':
            newURL=str(list[theChosenOne]['href'])
            print(newURL)
            
        else:
            subTopics = list[theChosenOne].findAll('a')
            for subtopic in subTopics:
                print(subtopic.text)
                
                
        
    def userInputManager(self,size,sub):
        while (True):
            # if(sub=='BigTopics'):
            try:
                userIn= int(input("Please enter the number of the topic that you want..."))
                if (userIn in range (size)):
                    return userIn
                else:
                    print("invalid")
            except:
                print("invalid number")
                
            
        
p1 = StaticCrawler()
p1.contribute()

