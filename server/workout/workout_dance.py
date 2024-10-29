import random


workout_dict = {'Running':'https://www.youtube.com/watch?v=_kGESn8ArrU&pp=ygUTcHJvcGVyIHJ1bm5pbmcgZm9ybQ%3D%3D', 
                'Cycling':'https://www.youtube.com/watch?v=jLYSX9AcXQM&pp=ygUTcHJvcGVyIGN5Y2xpbmcgZm9ybQ%3D%3D', 
                'Jumping Jacks':'https://www.youtube.com/watch?v=nGaXj3kkmrU&pp=ygUUcHJvcGVyIGp1bXBpbmcgamFja3M%3D', 
                'Burpees':'https://www.youtube.com/watch?v=NCqbpkoiyXE&pp=ygUPcHJvcGVyIGJ1cnBlZXMg', 
                'Rowing':'https://www.youtube.com/watch?v=Y1GhfJoWLko&pp=ygUNcHJvcGVyIHJvd2luZw%3D%3D',
                'Stretching':'https://www.youtube.com/watch?v=FI51zRzgIe4&pp=ygUic3RyZXRjaGluZyBleGVyY2lzZXMgZm9yIGJlZ2lubmVycw%3D%3D',
                'Yoga':'https://www.youtube.com/watch?v=m756Gz8de4M&pp=ygUSeW9nYSBmb3IgYmVnaW5uZXJz', 
                'Pilates':'https://www.youtube.com/watch?v=Iv3r2kulhI8&pp=ygUTcHJvcGVyIHBpbGF0ZXMgZm9ybQ%3D%3D',
                'Zumba':'https://www.youtube.com/watch?v=F4BJst5d9Ac&pp=ygULenVtYmEgZGFuY2U%3D',
                'Hip-hop':'https://www.youtube.com/watch?v=QPFyyKqFi4k&pp=ygUjaGlwIGhvcCBkYW5jZSB3b3Jrb3V0IGZvciBiZWdpbm5lcnM%3D',
                'Salsa':'https://www.youtube.com/watch?v=c1pB0NjYO2A&pp=ygUhc2Fsc2EgZGFuY2Ugd29ya291dCBmb3IgYmVnaW5uZXJz',
                'Bollywood':'https://www.youtube.com/watch?v=uZfLwf2oixg&pp=ygUlYm9sbHl3b29kIGRhbmNlIHdvcmtvdXQgZm9yIGJlZ2lubmVycw%3D%3D',
                'Ballet':'https://www.youtube.com/watch?v=hzzJX7VRHmo&pp=ygUiYmFsbGV0IGRhbmNlIHdvcmtvdXQgZm9yIGJlZ2lubmVycw%3D%3D',
                'Lat pulldown,Suspended row':('https://www.youtube.com/watch?v=n-lzgClH99Q&pp=ygUZcHJvcGVyIGxhdCBwdWxsZG93bnMgaG9tZQ%3D%3D','https://www.youtube.com/watch?v=6uN0OU4AlHI&pp=ygUbc3VzcGVuZGVkIHJvdyBleGVyY2lzZSBob21l'),
                'Quadruped single-arm dumbbell row,chin Ups':('https://www.youtube.com/watch?v=ZRSGpBUVcNw&pp=ygUYcXVhZHJhcGxlIHNpbmdsZSBhcm0gcm93','https://www.youtube.com/watch?v=brhRXlOhsAM&pp=ygUHY2hpbnVwcw%3D%3D'),
                'Tense and Hold Press-Ups, Wide Grip Press-Up, T Press-Up':('https://www.youtube.com/watch?v=pupwibLXtO8&pp=ygUWdGVuc2UgYW5kIGhvbGQgcHJlc3N1cA%3D%3D','https://www.youtube.com/watch?v=rr6eFNNDQdU&pp=ygUSd2lkZSBncmlwIHByZXNzIHVw','https://www.youtube.com/watch?v=Iu8E67jcXQ4&pp=ygUKdCBwcmVzcyB1cA%3D%3D'),
                'Spiderman Press-Up,Normal Press-Up':('https://www.youtube.com/watch?v=qG2oWGqXSdw&pp=ygUTc3BpZGVyIG1hbiBwcmVzcyB1cA%3D%3D','https://www.youtube.com/watch?v=IODxDxX7oi4&pp=ygUQbm9ybWFsIHByZXNzIHVwcw%3D%3D'), 
                'Decline Press-Up, Inclined Press-Up':('https://www.youtube.com/watch?v=5QFjmotLfW4&pp=ygUQZGVjbGluZSBwdXNoIHVwcw%3D%3D','https://www.youtube.com/watch?v=Me9bHFAxnCs&pp=ygUQaW5jbGluZSBwdXNoIHVwcw%3D%3D'),
                'Bicycle Crunches,Mountain Climbers,Leg Raises,Reverse Crunch':('https://www.youtube.com/watch?v=O0pIQ2UqeCY&pp=ygUIQ3J1bmNoZXM%3D','https://www.youtube.com/watch?v=nmwgirgXLYM&pp=ygURTW91bnRhaW4gQ2xpbWJlcnM%3D','https://www.youtube.com/watch?v=Zr-PtqcpeWM&pp=ygUKbGVnIHJhaXNlcw%3D%3D','https://www.youtube.com/watch?v=hyv14e2QDq0&pp=ygUOcmV2ZXJzZSBjcnVuY2g%3D'),
                'Normal Squates, Sumo Squates, Lunges':('https://www.youtube.com/watch?v=YaXPRqUwItQ&pp=ygUNbm9ybWFsIHNxdWF0cw%3D%3D','https://www.youtube.com/watch?v=kjlfpqXnyL8&pp=ygULc3VtbyBzcXVhdHM%3D','https://www.youtube.com/watch?v=MxfTNXSFiYI&pp=ygUObHVuZ2VzIHdvcmtvdXQ%3D'),
                'Spiderman Press-Up,Normal Press-Up':('https://www.youtube.com/watch?v=qG2oWGqXSdw&pp=ygUSc3BpZGVybWFuIHB1c2h1cHMg','https://www.youtube.com/watch?v=IODxDxX7oi4&pp=ygUQbm9ybWFsIHByZXNzIHVwcw%3D%3D'),
                'Diamond PushUP,wide grip push ups':('https://www.youtube.com/watch?v=ZR5U3sb-KeE&pp=ygUQZGlhbW9uZCBwdXNoIHVwcw%3D%3D','https://www.youtube.com/watch?v=rr6eFNNDQdU&pp=ygUSd2lkZSBncmlwIHByZXNzIHVw'),
                'Bottle Slider Flyes,Kitchen Sieve Close-Grip Press-Up,The Alternating Shuffle Press-up':('https://www.youtube.com/watch?v=NgN6vJWMepc&pp=ygUTQm90dGxlIFNsaWRlciBGbHllcw%3D%3D','https://www.youtube.com/watch?v=ABi1Z1Gc9Tw&pp=ygUhS2l0Y2hlbiBTaWV2ZSBDbG9zZS1HcmlwIFByZXNzLVVw','https://www.youtube.com/watch?v=eqksAtUx7OE&pp=ygUgVGhlIEFsdGVybmF0aW5nIFNodWZmbGUgUHJlc3MtdXA%3D'),
                'Tricep PushUP,Tricep dips':('https://www.youtube.com/watch?v=kZi0j-7rDe8&pp=ygUOdHJpY2VwIHB1c2h1cHM%3D','https://www.youtube.com/watch?v=6kALZikXxLc&pp=ygULdHJpY2VwIGRpcHM%3D'),
                'Walking, Jogging(Mixed)':('https://www.youtube.com/watch?v=Dqe5pTF4mIc&pp=ygUVbWl4ZWQgd2Fsa2luZyBqb2dnaW5n'),
                'walking':('https://www.youtube.com/watch?v=Dqe5pTF4mIc&pp=ygUVbWl4ZWQgd2Fsa2luZyBqb2dnaW5n'),
                'jogging':('https://www.youtube.com/watch?v=Dqe5pTF4mIc&pp=ygUVbWl4ZWQgd2Fsa2luZyBqb2dnaW5n'),
                'Butt Kicks, High Knees, toe taps':('https://www.youtube.com/watch?v=-dtvAxibgYQ&pp=ygUKYnV0dCBraWNrcw%3D%3D','https://www.youtube.com/watch?v=ZNDHivUg7vA&pp=ygUTaGlnaCBrbmVlcyBleGVyY2lzZQ%3D%3D','https://www.youtube.com/watch?v=03qmWg4Qk5g&pp=ygURdG9lIHRhcHMgZXhlcmNpc2U%3D'),
                'Squat Jumps, Toe Taps':('https://www.youtube.com/watch?v=f-9Gmlt57YM&pp=ygULc3F1YXQganVtcHM%3D','https://www.youtube.com/watch?v=98td_hCxync&pp=ygUJdG9lIHRhcHMg'),
                'Standing alternative Toe touches':'https://www.youtube.com/watch?v=TOseXxRQwdI&pp=ygUgc3RhbmRpbmcgYWx0ZXJuYXRpdmUgdG9lIHRvdWNoZXM%3D',
                'box jumps,lung jumps':('https://www.youtube.com/watch?v=AV2Oaq1KFJ4&pp=ygUXYm94IGp1bXBzIGZvciBiZWdpbm5lcnM%3D','https://www.youtube.com/watch?v=0lxr_mvYQeQ&pp=ygULbHVuZ2UganVtcHM%3D'),
                'plank jacks, rope jump':('https://www.youtube.com/watch?v=xcBz0TtHqWI&pp=ygUMcGxhbmNrIGphY2tz','https://www.youtube.com/watch?v=-mB2fq560bc&pp=ygUJcm9wZSBqdW1w')}

def workout_dance(weeks):
    n = weeks
    
    cardio_exercises = ['Running', 'Cycling', 'Jumping Jacks', 'Burpees', 'Rowing']
    set2 = "complete 1hr process, take 5 mins break between each 20 mins"

    flexibility_exercises = ['Stretching', 'Yoga', 'Pilates']
    set3 = "30 mins process no rest"

    dances = ['Zumba', 'Hip-hop', 'Salsa', 'Bollywood', 'Ballet']
    set4 = "complete 1hr process, take 5 mins break between each 20 mins"

    n = n
    out=[]
    work={}
    final=[]
    for i in range(n):
        def generate_workout_plan(user_preferences):
            workout_plan = {}
            days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

            for day in days_of_week:
                workout_plan[day] = []

            for day in days_of_week:
                # Generate a random workout based on user preferences
                workout = generate_random_workout(user_preferences)
                workout_plan[day] = workout

            return workout_plan

        def generate_random_workout(user_preferences):
            # Sample workout generation code - adjust based on user preferences
            workouts = ['Strength Training', 'Cardio', 'Flexibility', 'Dance']
            workout = random.choice(workouts)
            
            if workout == 'Cardio':
                cardio_exercises = ['Running', 'Cycling', 'Jumping Jacks', 'Burpees', 'Rowing']
                workout_plan = random.sample(cardio_exercises, k=1)  
            elif workout == 'Flexibility':
                flexibility_exercises = ['Stretching', 'Yoga', 'Pilates']
                workout_plan = random.sample(flexibility_exercises, k=1) 
            else:
                dances = ['Zumba', 'Hip-hop', 'Salsa', 'Bollywood', 'Ballet']
                workout_plan = random.sample(dances, k=3)  # Select 1 random dance style
            return workout_plan

        # Example user preferences
        user_preferences = {
            'goals': ['lose weight', 'increase muscle mass'],
            'preferences': ['strength training', 'cardio', 'dance'],
            'requirements': ['no equipment', 'limited time']
        }

        # Generate a weekly workout plan based on user preferences
        weekly_workout_plan = generate_workout_plan(user_preferences)

        # Print the generated workout plan
        res=[]
        for day, workout in weekly_workout_plan.items():
            work[day]=workout
            curr = {}
            workout = workout[0]
            if workout in cardio_exercises:
                
                x = workout_dict.get(workout)
                
                # curr["duration"]=set2
                curr["links"]=x
                
                
            elif workout in flexibility_exercises:
              
                x = workout_dict.get(workout)
                
                # curr["duration"]=set3
                curr["links"]=x
           
                
            elif workout in dances:
                x = workout_dict.get(workout)
                # curr["duration"]=set4
                curr["links"]=x
            res.append(curr)
        out.append(res)
        final.append(work)
        work={}
    return [final,out]
            
