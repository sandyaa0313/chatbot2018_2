from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_button_message
from utils import send_url_message
from utils import send_image_message
from bs4 import BeautifulSoup

import requests


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            if 'text' in event['message']:
                text = event['message']['text']
                return text.lower() == 'know more'
        return False

    def is_going_to_contact(self, event):
        if event.get("message"):
            if 'text' in event['message']:
                text = event['message']['text']
                return text.lower() == 'contact'
        return False

    def is_going_to_intro(self, event):
        if event.get("message"):
            if 'text' in event['message']:
                text = event['message']['text']
                return True
        return False    

    def is_going_to_hug(self, event):
        if event.get("message"):
            if 'text' in event['message']:
                text = event['message']['text']
                return text.lower() == 'give me a hug'
        return False    

    def is_going_to_state2(self, event):
        if event.get("postback"):
            if 'payload' in event['postback']:
                text = event['postback']['payload']
                return text.lower() == 'blockbusters'
        return False

    def is_going_to_state3(self, event):
        if event.get("postback"):
            if 'payload' in event['postback']:
                text = event['postback']['payload']
                return text.lower() == 'high score movies'
        return False

    def is_going_to_state4(self, event):
        if event.get("postback"):
            if 'payload' in event['postback']:
                text = event['postback']['payload']
                return text.lower() == 'movie introduction'
        return False

    def is_going_to_choice(self, event):
        if event.get("postback"):
            if 'payload' in event['postback']:
                text = event['postback']['payload']
                global m
                m=text
                return True
        return False
       
    def is_going_to_theather(self, event):
        if event.get("postback"):
            if 'payload' in event['postback']:
                text = event['postback']['payload']
                return text=='台南大遠百威秀影城'
        return False

    def is_going_to_theather2(self, event):
        if event.get("postback"):
            if 'payload' in event['postback']:
                text = event['postback']['payload']
                return text=='台南南紡威秀影城'
        return False

    def is_going_to_theather3(self, event):
        if event.get("postback"):
            if 'payload' in event['postback']:
                text = event['postback']['payload']
                return text=='台南國賓影城'
        return False    
    
    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        buttons=[
            {
                "type":"postback",
                "title":"blockbusters",
                "payload":"blockbusters"
            },
            {
                "type":"postback",
                "title":"high score movies",
                "payload":"high score movies"

            },
            {
                "type":"postback",
                "title":"movie introduction",
                "payload":"movie introduction"

            }
        ]
        responese = send_button_message(sender_id,"Hi !\nHere are some movies in theathers.\nChoose one type you are interested in.",buttons)
        #self.go_back()

    def on_exit_state1(self,event):
        print('Leaving state1')

    def on_enter_contact(self,event):
        print("I'm entering state contact")

        sender_id = event['sender']['id']
        send_text_message(sender_id,"Write an email to sandyaa0313@gmail.com to reflect your problem.\nType 'know more' to get more information.")
        self.go_back()

    def on_exit_contact(self):
        print('Leaving state contact')    

    def on_enter_intro(self,event):
        print("I'm entering state intro")

        sender_id = event['sender']['id']
        send_text_message(sender_id,"This is a chatbot for simply searching movie broadcast time.\nType 'know more' to get more information.\nType 'contact' to reflect problems.\nType 'give me a hug' to give me some encouragement.")
        self.go_back()

    def on_exit_intro(self):
        print('Leaving state intro')

    def on_enter_hug(self,event):
        print("I'm entering state intro")

        sender_id = event['sender']['id']
        send_text_message(sender_id,"thank you!!!")
        self.go_back()

    def on_exit_hug(self):
        print('Leaving state hug')                

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']

        url = "https://movies.yahoo.com.tw/chart.html"
        res=requests.get(url)
        soup=BeautifulSoup(res.text,"html.parser")
        movie1=soup.find('h2')
        movie2=soup.find_all(class_='rank_txt')

        buttons=[
            {
                "type":"postback",
                "title":movie1.text,
                "payload":movie1.text
            },
            {
                "type":"postback",
                "title":movie2[0].text,
                "payload":movie2[0].text

            },
            {
                "type":"postback",
                "title":movie2[1].text,
                "payload":movie2[1].text
            }

        ]

        send_button_message(sender_id,"Here are top 3 movies now.",buttons)
        #self.go_back()

    def on_exit_state2(self,event):
        print('Leaving state2')
    
    def on_enter_state3(self,event):
        print("I'm entering state3")

        sender_id=event['sender']['id']
        url="https://movies.yahoo.com.tw/chart.html?cate=rating"
        res=requests.get(url)
        soup=BeautifulSoup(res.text,"html.parser")
        movie1=soup.find('h2')
        movie2=soup.find_all(class_='rank_txt')
        buttons=[
            {
                "type":"postback",
                "title":movie1.text,
                "payload":movie1.text
            },
            {
                "type":"postback",
                "title":movie2[0].text,
                "payload":movie2[0].text

            },
            {
                "type":"postback",
                "title":movie2[1].text,
                "payload":movie2[1].text
            }

        ]

        send_button_message(sender_id,"Here are 3 movies with highest score",buttons)
        #self.go_back()

    def on_exit_state3(self,event):
        print('Leaving state3')
    
    def on_enter_state4(self,event):
        print("I'm entering state4")

        sender_id=event['sender']['id']
        buttons=[
            {
                "type":"web_url",
                "url":"https://movies.yahoo.com.tw/movie_thisweek.html",
                "title":"movie introduction",
                "webview_height_ratio":"full"
            },

        ]

        send_url_message(sender_id,"Here is the link.",buttons)
        self.go_back()

    def on_exit_state4(self):
        print('Leaving state4')

    def on_enter_choice(seif,event):
        print("I'm entering choice state")

        sender_id=event['sender']['id']
        if event.get('postback'):
            text=event['postback']['payload']
            text=text.lower()
            send_text_message(sender_id,text)

            buttons=[
                {
                    "type":"postback",
                    "title":"台南大遠百威秀影城",
                    "payload":"台南大遠百威秀影城"
                },
                {
                    "type":"postback",
                    "title":"台南南紡威秀影城",
                    "payload":"台南南紡威秀影城"
                },
                {
                    "type":"postback",
                    "title":"台南國賓影城",
                    "payload":"台南國賓影城"
                }

            ]
            send_button_message(sender_id,"For movie theathers in South Taiwan.",buttons)

    def on_exit_choice(self,event):
        print('Leaving state choice')

    def on_enter_theather(self,event):
        print("I'm entering state theather")

        sender_id = event['sender']['id']
        url="http://www.atmovies.com.tw/showtime/t06609/a06/" #大遠百
        res=requests.get(url)
        soup=BeautifulSoup(res.text,"html.parser")

        aa = soup.select("#theaterShowtimeTable > li.filmTitle > a")
        t1 = [a.text for a in aa]

        r="just for today\n"
        j=0
        k=0
        bb=soup.select("#theaterShowtimeTable > li:nth-of-type(2) > ul:nth-of-type(2) > li")
        t2 = [b.text for b in bb]

        cc=soup.select("#theaterShowtimeTable > li:nth-of-type(2) > ul:nth-of-type(2) > li.filmVersion")
        t3 = [c.text for c in cc]

        for i in range(len(t2)):
            n=ord(t2[i][0])-48
            if n==0 or n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9:
                    if t2[i]!="4DX" and t2[i]!='3D版':
                        if aa[j-1].text==m:
                            r+=t2[i]+"  "
            else:
                if k%2==0:
                    if aa[j].text==m:
                        r+="\n"+aa[j].text+"("+cc[j].text+")"+"\n"
                    j=j+1
                k=k+1  
        if r=="just for today\n":
            r="The movie you choose is not broadcast on this theather" 
        send_image_message(sender_id,"http://iphoto.ipeen.com.tw/photo/map_cache/new/1/7/6/140671/300x300.png")
        send_text_message(sender_id,r)
        self.go_back()
   


    def on_exit_theather(self):
        print('Leaving state theather')

    def on_enter_theather2(self,event):
        print("I'm entering state theather2")

        sender_id=event['sender']['id']
        url="http://www.atmovies.com.tw/showtime/t06610/a06/" #南紡
        res=requests.get(url)
        soup=BeautifulSoup(res.text,"html.parser")
        tt = soup.find_all(class_="filmTitle")

        aa = soup.select("#theaterShowtimeTable > li.filmTitle > a")
        t1 = [a.text for a in aa]

        r="just for today\n"
        j=0
        k=0
        bb=soup.select("#theaterShowtimeTable > li:nth-of-type(2) > ul:nth-of-type(2) > li")
        t2 = [b.text for b in bb]

        cc=soup.select("#theaterShowtimeTable > li:nth-of-type(2) > ul:nth-of-type(2) > li.filmVersion")
        t3 = [c.text for c in cc]

        for i in range(len(t2)):
            n=ord(t2[i][0])-48
            if n==0 or n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9:
                if t2[i]!="4DX" and t2[i]!='3D版':
                    if aa[j-1].text==m:
                            r+=t2[i]+"  "
            else:
                if k%2==0:
                    if aa[j].text==m:
                        r+="\n"+aa[j].text+"("+cc[j].text+")"+"\n"
                    j=j+1    
                k=k+1
        if r=="just for today\n":
            r="The movie you choose is not broadcast on this theather"        
        send_image_message(sender_id,"http://iphoto.ipeen.com.tw/photo/map_cache/new/5/7/7/1201775/600x360.png")
        send_text_message(sender_id,r)
        self.go_back()
   

    def on_exit_theather2(self):
        print('Leaving state theather2')

    def on_enter_theather3(self,event):
        print("I'm entering state theather3")

        sender_id=event['sender']['id']
        url="http://www.atmovies.com.tw/showtime/t06608/a06/" #台南國賓影城
        res=requests.get(url)
        soup=BeautifulSoup(res.text,"html.parser")

        aa = soup.select("#theaterShowtimeTable > li.filmTitle > a")
        t1 = [a.text for a in aa]

        r="just for today\n"
        j=0
        k=0
        bb=soup.select("#theaterShowtimeTable > li:nth-of-type(2) > ul:nth-of-type(2) > li")
        t2 = [b.text for b in bb]
        #print(t2)
       
        cc=soup.select("#theaterShowtimeTable > li:nth-of-type(2) > ul:nth-of-type(2) > li.filmVersion")
        t3 = [c.text for c in cc]
        #print(t3)

        for i in range(len(t2)):
            n=ord(t2[i][0])-48
            if n==0 or n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9:
                    if t2[i]!="4DX" and t2[i]!='3D版':
                        if k%2==0:
                            if aa[j-1].text==aa[j].text:
                                if aa[j-1].text==m:
                                    r+="\n"+t2[i]+"  "   
                                j=j+1
                            else:
                                if aa[j-1].text==m:
                                    r+="\n"+aa[j].text+t2[i]+"  "    
                        else:
                            if aa[j-1].text==m:    
                                r+=t2[i]+"  "
            else:
                if k%2==0:
                        if aa[j].text==m:
                            r+="\n"+aa[j].text+"\n"
                        j=j+1    
                k=k+1  

        if r=="just for today\n":
            r="The movie you choose is not broadcast on this theather"        
        send_image_message(sender_id,"http://www.ambassador.com.tw/external/events/shinefilm2018/images/cinema_a2.jpg")
        send_text_message(sender_id,r)
        self.go_back()
   

    def on_exit_theather3(self):
        print('Leaving state theather3')          
        

        
