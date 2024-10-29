import datetime
import wikipedia 
import webbrowser
import os
import smtplib


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        ("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")   

    else:
        print("Good Evening!")  
        
    name = 'chat'
    
    print("I am  {name}. Hear to Help You Out")
    
    print("Kindly Enter the Below details correctly")
    
    name = input("Name:\n")
    age = input("Age:\n")       
    sex = input("Sex(M/F):\n").lower()       
    print("\n")
    print("Hi %s\n"%name)
        
    print("happy to see you here\n")
    print("may i get your problem...")
           
           

def takeCommand():
    #It takes microphone input from the user and returns string output
    
    
    proce_ = input("Do You want to continue:(Yes/No)__.\n")
    if proce_.lower()=='yes':
            
        
        r = input("problem: ")
        # with sr.Microphone() as source:
        #     print("Listening...")
        #     r.pause_threshold = 1
        #     audio = r.listen(source)

        try:
    
            query = r
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query
    else:
        print("Thanks for the service")


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if query:
            print('Processing...')
            query = query+" disease"
            r = wikipedia.search(query)
            print("possible problmes")
            print("\n")
            print(r)
            print("\n")

            for i in range(len(r)):
                try:
                    print("_"*100)
                    print(str(i+1)+'.'+r[i]) 
                    print("_"*100)
                    results = wikipedia.summary(r[i])
                    print("According to My Knowledge:\n")
                    print("\n")
                    print(results)
                    print("\n")
                except Exception:
                    print()

        