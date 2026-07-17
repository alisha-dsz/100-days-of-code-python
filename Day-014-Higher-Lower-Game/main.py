import random
from art import logo, vs
from game_data import data

def format_data(id_data):
    name=id_data['name']
    description=id_data['description']
    country=id_data['country']
    return f"{name}, a {description}, from {country}."

def check_answer(guess, id_one_follower, id_two_follower):
    if id_one_follower > id_two_follower:
        return guess=='a'
    else:
        return guess=='b'


score=0
print(logo)
should_game_continue=True


identity_two=random.choice(data)
while should_game_continue:
    identity_one=identity_two
    identity_two=random.choice(data)

    if identity_one==identity_two:
        identity_two=random.choice(data)

    print(f"Compare A: {format_data(identity_one)}")
    print(vs)
    print(f"Compare B: {format_data(identity_two)}")

    user_input=input("Who has the most followers? Choose 'A' or 'B': ").lower()

    print("\n"*100)
    print(logo)

    identity_one_follower=identity_one['follower_count']
    identity_two_follower=identity_two['follower_count']

    is_correct=check_answer(user_input, identity_one_follower, identity_two_follower)

    if is_correct:
        score+=1
        print(f"You've got the correct answer. Current score: {score}.")
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        should_game_continue=False