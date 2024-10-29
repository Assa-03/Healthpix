import numpy as np
import wikipedia 
from joblib import load 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# print("Welcome to Workout Plan Generator\n")

# print("Enter the below details to create the plan\n")
# [age,height(m),weight(kg),bmi_score,bmi_index,dance]


# name = input("Name: \n")
# age = float(input("Age: \n"))
# Gender = input("Gender: \n")
# height = float(input("Height(meter): \n"))
# weight = float(input("Weight(kg): \n"))
# dance = input("Like to get dance based Excercise:(y/n)\n").lower()
# if dance=='yes' or dance=='y':
#     dance = 1
# elif dance=='no' or dance=='n':
#     dance = 0

class Item(BaseModel):
    age: str
    height: str 
    weight: str
    dance: str 
    weeks: str

class Chat(BaseModel):
    query: str
    

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def create_item(item: Item):
    age = float(item.age)
    height = float(item.height)
    weight = float(item.weight)
    weeks = int(item.weeks)
    if item.dance == "yes":
        dance = 1
    else:
        dance = 0
    bmi_score = float(weight/(height*height))
    if bmi_score>=30:
        bmi_index = 0 
        print("Your Current Level: Obese\n")
        
        # '''Obese'''  
    elif bmi_score > 25.0 and bmi_score<= 29.9:
        bmi_index = 1
        print("Your Current Level: Heavy Weight\n")
        # '''Heavy Weight'''
        
    elif bmi_score <= 18.5 :
        bmi_index = 2
        print("Your Current Level: Under Weight\n")
        # '''Under Weight'''
    else:
        bmi_index = 3
        print("Your Current Level: Normal Weight\n")
        # '''normal weight''' 
    
    print([age,height,weight,bmi_score,bmi_index,dance])

    
    from joblib import load
    # [age,height(m),weight(kg),bmi_score,bmi_index,dance]
    # [56, 1.80,98.50,30.401235,1,0] >>>>> Cardio
    # [35,1.93,109.9, 29.504148,2,0] >>>>> cardio+strength_trainig(1)
    # [57,1.47,36.00,16.659725,3,1] >>>>>> dance
    # [60,1.46,35.90,16.841809,3,0] >>>>>>> strength_training(3)

    model = load('D:/69/Aids/server/workout/model.pkl')



    y = np.array([[age,height,weight,bmi_score,bmi_index,dance]])
    y = y.reshape(1,-1)
    p = model.predict(y)
    print(p[0])

    x=[]
    if p[0]==2 and dance==1:
        print("dance")
        x.append("dance")
    elif dance==1:
        print("dance")
        x.append("dance")
            
    elif p[0]==0 and bmi_index==0:
        print("cardio")
        x.append("cardio")
        
    elif bmi_index==0:
        print("cardio")
        x.append("cardio")
        
    elif p[0]==2 and bmi_index==2:
        print("strength_training")
        x.append("strength_training")
    elif bmi_index==2:
        print("strength_trainig")
        x.append("strength_training")
        
    elif p[0]==1 and bmi_index==1:
        print("Cardio + strength_training")
        x.append("cardio+strength_training")
    elif bmi_index==1:
        print("Cardio + strength_training")
        x.append("cardio+strength_training")

    elif p[0]==3 and bmi_index==3:
        print("Cardio + strength_training")
        x.append("cardio+strength_training")
    elif bmi_index==3:
        print("Cardio + strength_training")
        x.append("cardio+strength_training")

    if x[0]=="dance":
        from workout_dance import workout_dance
        res = workout_dance(weeks)
    elif x[0]=="strength_training":
        from workout_strength import workout_strength
        res = workout_strength(weeks)
    elif x[0]=="Cardio + strength_training":
        from workout_strdio import workout_strdio
        res = workout_strdio(weeks)
    else:
        from workout_cardio import workout_cardio
        res = workout_cardio(weeks)
    print(x,res)

    return res

@app.post("/chat")
async def chat(cht: Chat):
    query = cht.query+" disease"
    r = wikipedia.search(query)
            # print("possible problmes")
            # print("\n")
            # print(r)
            # print("\n")
    res = {}
    for i in range(len(r)):
        try:
                    
                    
                    
            results = wikipedia.summary(r[i])
                   
            res[r[i]]=results
                    
        except Exception:
            print()
    return res







# print("Your BMI Score: \n",bmi_score)


    

    

# if x[0]=="dance":
#     from workout_dance import workout_dance
#     workout_dance()
# elif x[0]=="strength_training":
#     from workout_strength import workout_strength
#     workout_strength()
# elif x[0]=="Cardio + strength_training":
#     from workout_strdio import workout_strdio
#     workout_strdio()
# else:
#     from workout_cardio import workout_cardio
#     workout_cardio()