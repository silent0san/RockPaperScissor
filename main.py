import random

all_signs = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf", "sponge",
             "paper", "air", "water", "dragon", "devil", "lightning", "gun", "rock",
             "fire", "scissors", "snake", "human", "tree", "wolf", "sponge", "paper",
             "air", "water", "dragon", "devil", "lightning", "gun"]

signs_winning_synergies, temporary_list = {}, []

for sign in all_signs:
    sign_index = all_signs.index(sign)
    for i in range(1, 8):
        temporary_list.append(all_signs[i + sign_index])
    signs_winning_synergies[sign] = temporary_list
    temporary_list = []
    if sign_index > 14:
        break

name = input('Enter your name: ')
print(f"Hello, {name}")

rating_file = open('rating.txt', 'r')

name_list, rating_list = [], []

for line in rating_file:
    name_from_file = line.split(' ')[0]
    name_list.append(name_from_file)
    rating_from_file = line.split(' ')[1]
    rating_from_file = rating_from_file.replace("\n", "")
    rating_list.append(rating_from_file)

if name in name_list:
    name_index = name_list.index(name)
    rating = int(rating_list[name_index])
else:
    name_list.append(name)
    rating = 0
    rating_list.append(rating)

# User enters playable_signs that will participate in games
signs_chosen_by_player = input("Enter signs you wish to play with: ")

if not signs_chosen_by_player:
    signs_chosen_by_player = "rock, paper, scissors"

signs_chosen_by_player = signs_chosen_by_player.replace(" ", "").lower().split(",")

chosen_signs_winning_synergies, chosen_temporary_list = {}, []

for sign in signs_chosen_by_player:
    signs_win_vs = signs_winning_synergies.get(sign)
    for sign_B in signs_win_vs:
        if sign_B in signs_chosen_by_player:
            chosen_temporary_list.append(sign_B)
    chosen_signs_winning_synergies[sign] = chosen_temporary_list
    chosen_temporary_list = []

print("Okay, let's start")

while True:
    option = input()
    option_pc = random.choice(signs_chosen_by_player)

    if option == "!rating":
        print(rating)
        continue
    elif option == "!exit":
        print("Bye!")
        break
    elif option not in signs_chosen_by_player:
        print("Invalid input")
        continue
    elif option == option_pc:
        print(f'There is a draw ({option})')
        rating += 50
        continue

    for op, sign in chosen_signs_winning_synergies.items():
        if option == op:
            beaten_signs = sign
            if option_pc in beaten_signs:
                print(f'Well done. The computer chose {option_pc} and failed')
                rating += 100
                continue
            elif option_pc not in beaten_signs:
                print(f'Sorry, but the computer chose {option_pc}')
                break
