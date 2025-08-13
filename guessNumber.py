import random 

random_to_guess=random.randint(1,100)
while True:
 try:
   guess=int(input("inter a number between 1:100 : "))
    
   if guess<random_to_guess:
      print("too low..")

   elif guess>random_to_guess:
      print("too high")
    
   else: 
      print("congratulation, you guessed it right..")
      break
    
 except ValueError:
    print("invalid input , please enter a number..")