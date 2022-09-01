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
        new = self.findingTopics(soup,'hich')
        newURL = self.url+new
        r2= requests.get(newURL)
        soupFinal = bs(r2.content,'html.parser')
        print("Now Try it Yourself!!!")
        tryItYourSelf = soupFinal.find_all("a", string="Try it Yourself »",target="_blank")
        for links in tryItYourSelf:
            print(self.url+links['href'])
        
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
                if isinstance(temp,Comment) :
                    temp = temp.nextSibling
                    continue
                if temp.text!= '\n' and temp.name != 'br':
                    list.append(temp)
                temp = temp.nextSibling
            else:
                break
        
        for items in list:
            if items.name != 'div':
                print(str(counter2) + '- ' + items.text)
                counter2+=1
        print('----------------')
        
        counter3=1
        theChosenOne = self.userInputManager(counter2-1,sub)
        #iterate subtopics and get new link
        noDiv=[]
        noDiv=self.divRemover(list)
        index = list.index(noDiv[theChosenOne-1])
        return self.newLinkMaker(list,index)
   
    def newLinkMaker(self,list,theChosenOne):
        subCounter = 1
        list2=[]
        if theChosenOne==len(list)-1 or list[theChosenOne+1].name != 'div':
            newURL=str(list[theChosenOne]['href'])
            return newURL
            
        else:
            subTopics = list[theChosenOne+1].findAll('a')
            for subtopic in subTopics:
                print(str(subCounter) + '- ' +subtopic.text)
                subCounter+=1
            theChosenOne = self.userInputManager(subCounter-1,'sub') 
            newURL = str(subTopics[theChosenOne-1]['href'])
            return newURL
                       
    def divRemover(self,list):
        newList=[]
        for items in list:
            if items.name != 'div':
                newList.append(items)
        return newList
        
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

