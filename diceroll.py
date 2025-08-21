import random

while True:
    number1=random.randint(1,6)
    number2=random.randint(1,6)
    message=input("roll the 🎲 ? (y/n) : ").lower()
    if message=="y":
        
        print(f'({number1},{number2})')
        
    elif message == "n":
        print("thanks for playing...")
        break
    
    else:
        print('invalid input..')
