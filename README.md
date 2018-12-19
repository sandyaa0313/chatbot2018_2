# chatbot2018

a.my fsm image\n
 https://i.imgur.com/CqTRgNR.png\n

b.how to implement my chatbot

user state:
  Type everything you like.
  (1)If the users type 'know more',then go to state1.
  (2)If the users type 'contact',then go to state2.
  (3)If the users type neither 'know more' nor 'contact',then back to user state.

state1:
  The users will see 3 buttons,which we can choose one service.
  (1)If the users choose 'blockbusters',then go to state2.
  (2)If the users choose 'high score movies',then go to state3.
  (3)If the users choose 'movie introduction',then go to state4.

state2:
  The users will see top3 blockbusters in theather now.
  Pick one movie we are interested in.
  After we choose,then we can go to choice state.
 
state3:
  The users will see top3 movies with highest score in theather now.
  Pick one movie we are interested in.
  After we choose,then we can go to choice state.

state4:
  We can get a link for movie introduction.

choice state:
  Now we just pick uo  one movie,so we are going to choose one movie theather in Tainan.
  The users will see 3 buttons,which we can choose one theather.
  (1)If we choose theather1,go to theather state.
  (1)If we choose theather2,go to theather2 state.
  (1)If we choose theather3,go to theather3 state.
 
theather state:
  It will print the movie broadcast time(just for today) and the picture for the location of the theather.
  Now you can back to user state if you type anything you like again.
  
theather2 state:
  It will print the movie broadcast time(just for today) and the picture for the location of the theather2.
  Now you can back to user state if you type anything you like again.
  
theather3 state:
  It will print the movie broadcast time(just for today) and the picture for the location of the theather3.
  Now you can back to user state if you type anything you like again.