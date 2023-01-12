from art import logo, vs
from game_data import data

import random



import random
from game_data import data

def create_compare():
    compare_a = data[random.randint(0, len(data) - 1)] 
    compare_b = data[random.randint(0, len(data) - 1)] 
    if compare_a == compare_b:
        compare_b = data[random.randint(0, len(data) - 1)] 
    return compare_a, compare_b
    # if compare_a equal to compare_b, then choose the compare data again



def compare_game():
    compare_a, compare_b = create_compare()

    compare_a_count = compare_a['follower_count']
    compare_a_name = compare_a['name']
    compare_a_description = compare_a["description"]
    compare_a_country = compare_a["country"]
    
    compare_b_count = compare_b['follower_count']
    compare_b_name = compare_b['name']
    compare_b_description = compare_b["description"]
    compare_b_country = compare_b["country"]
   
    score = 0
    is_on = True
    while is_on:
        print(logo)
        print(f"Compare a: {compare_a_name}, a {compare_a_description}, from {compare_a_country}.")
        print(f"Compare b: {compare_b_name}, a {compare_b_description}, from {compare_b_country}.")
        
        user_choice =  input("\nWho do you think has more followers? Type 'a', or 'b': ").lower()
    
        if user_choice == 'a' and compare_a_count >= compare_b_count:
            score += 1 
            print(f"Correct! Your current score is: {score}.")
        elif user_choice == 'b' and compare_a_count <= compare_b_count:
            score += 1
            print(f"Correct! Your current score is: {score}.")
        else:
            print(f"\nIncorrect, your final score is {score}.")

        play_again = input("\nDo you want to play again? Type 'y' or 'n': ")
        if play_again == 'y':
            compare_game()
        elif play_again == 'n':
            print(f"Your final score is {score} ")
            print("Thanks for playing!")
            is_on = False

compare_game()







