import time

my_timer = int(input("Enter the number in seconds (should be less than 180): "))
score = 0

start_time = time.time() #to start the counter 


if time.time() - start_time < my_timer:
    print('The first question is: What is the capital of Egypt?')
    capital = input('Your answer: ')
    if capital.lower() == 'cairo':
        score += 1


if time.time() - start_time < my_timer:
    print('The second question is: What is the capital of England?')
    capital = input('Your answer: ')
    if capital.lower() == 'london':
        score += 1


if time.time() - start_time < my_timer:
    print('The third question is: What is the capital of France?')
    capital = input('Your answer: ')
    if capital.lower() == 'paris':
        score += 1


if time.time() - start_time >= my_timer:
    print("\nTime is up!")


if score == 3:
    print('\nAll of your answers are correct')
elif score == 2:
    print('\nTwo of your answers are correct')
elif score == 1:
    print('\nOne of your answers is correct')
else:
    print('\n you got {score}answers correct out of 3')
    