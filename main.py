import random

symbols = ["scissors", "rock", "paper"]
counter = 0

name = input('Enter your name: ')
print(f"Hello, {name}")

print(f"{name=}")
print(f"Name to: {name}")

rating_file = open('rating.txt', 'r', encoding='utf-8')

name_list = []
rating_list = []

for line in rating_file:
    name_from_file = line.split(' ')[0]
    name_list.append(name_from_file)
    rating_from_file = line.split(' ')[1]
    rating_from_file = rating_from_file.replace("\n", "")
    rating_list.append(rating_from_file)

if name in name_list:
    index = name_list.index(name)
    rating = int(rating_list[index])
else:
    name_list.append(name)
    rating = 0
    rating_list.append(rating)

while True:
    option = input()
    option_pc = random.choice(symbols)

    if option == "!rating":
        print(rating)
        continue

    if option == "!exit":
        print("Bye!")
        break

    if option == option_pc:
        print(f'There is a draw ({option})')
        rating += 50
        continue

    if option != "scissors" and option != "rock" and option != "paper" and option != "!exit":
        print("Invalid input")
        continue

# Scissors
    if option == "scissors" and option_pc == "rock":
        print(f'Sorry, but the computer chose {option_pc}')
        continue
    elif option == "scissors" and option_pc == "paper":
        print(f'Well done. The computer chose {option_pc} and failed')
        rating += 100
        continue

# Rock
    if option == "rock" and option_pc == "paper":
        print(f'Sorry, but the computer chose {option_pc}')
        continue
    elif option == "rock" and option_pc == "scissors":
        print(f'Well done. The computer chose {option_pc} and failed')
        rating += 100
        continue

# Paper
    if option == "paper" and option_pc == "scissors":
        print(f'Sorry, but the computer chose {option_pc}')
        continue
    elif option == "paper" and option_pc == "rock":
        print(f'Well done. The computer chose {option_pc} and failed')
        rating += 100
        continue

rating_file.close()
