# Created by AcnSoft - Arda Çalışkan
# Instagram: https://www.instagram.com/AcnSoft
# Github: https://github.com/AcnSoft


import random

class chatai():
    

    # hello

    def costumhello(hello):
        # You need to provide "hello" to show to api the words
        # ex. hello = ["hi","hello"] , costumhello(hello)
        x = random.choice(hello)
        print(x)

    def casualhello():
        #You can add your own words here if you want
        casualhello = [
            "Hi",       #We know the person well, and we see them quite often
            "Hi there", #We know the person well but have not seen them so recently
            "Hey" ,     #We know the person very well
            "Hello",    #We know the person, but not so closely
            "Hey you"   #We know them so well, we can become playful
        ]
        q = random.choice(casualhello)
        print(q)
    

    def formalhello():
        #You can add your own words here if you want
        formalhello = [
            "Greeting",                   #You don’t know the person
            "Hello, nice to meet you",    #You know them, but not very well
            "Hello, nice to see you" ,    #You know them in a formal and regular situation, such as at work
            "Hello, how are you doing?",  #You know them a little more closely enough to use their name
            "Hello there"                 #You know them but haven’t seen them for some time

        ]
        w = random.choice(formalhello)
        print(w)



    # how are you


    def costumhru(hru):
        # You need to provide "hru" to show to api the words
        # ex. hello = ["How are you?","How’s it going?"] , costumhello(hello)
        e = random.choice(hru)
        print(e)

    def casualhru():
        #You can add your own words here if you want
        casualhello = [
            "How are you?",
            "How’s it going?",
            "How are things?" , 
            "How’s everything?",
            "What’s been going on?"
        ]
        r = random.choice(casualhello)
        print(r)

    def formalhru():
        #You can add your own words here if you want
        formalhru = [
            "Are you well?",
            "How are you keeping?"
        ]
        t = random.choice(formalhru)
        print(t)

    def friendshru():
        #You can add your own words here if you want
        friendshru = [
            "What’s up?",
            "What’s new?",
            "All right?"
       ]
        y = random.choice(friendshru)
        print(y)