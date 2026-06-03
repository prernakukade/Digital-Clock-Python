# Story Generator with Python Created By Prerna Kukade
# Our task is to generate a random stroy every time the stories in diffrenet lists,then the random module can be used to select the random parts of the story stored in different lists : 

import random
when = ['A few year ago','yesterday','last night','on 3rd June']
who = ['a rabbit','an elephant','a mouse','a turtle','a cat']
name = ['prerna','jyoti','sejal','akshay','aniket']
residence = ['India','Germany','France','Canada','London']
went = ['cinema','university','seminar','school','hotel']
happend = ['made a lot of friends','eats a pizza','found a key','worte a book','sloved a mistery']

print(random.choice(when) + ' , '+ random.choice(who) + ' named ' + random.choice(name) + ' that lived in '+ random.choice(residence) + ', went to the '+ random.choice(went) + ' and '+ random.choice(happend))