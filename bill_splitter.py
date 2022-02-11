import random

num_of_friends = int(input("Enter the number of friends joining (including you): "))
friend_dictionary = {}

print()

if num_of_friends <= 0:
        print("No one is joining for the party")
        exit()
        
else:
    for friends in range(num_of_friends):
        friend = {input("What is the name of your friend? "): 0}
        friend_dictionary.update(friend)

    print()

bill_total = int(input("Enter the total bill value: "))

print()

lucky = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: ").upper().strip()

print()

if lucky == "YES":
    winner = random.choice(list(friend_dictionary))
    print(f"{winner} is the lucky one!")

    split_bill = bill_total / (num_of_friends - 1)
    round_bill = round(split_bill, 2)

    for val in friend_dictionary:
        friend_dictionary[val] += round_bill

    friend_dictionary.update({winner: 0})

    print(friend_dictionary)

else:
    print("No one is going to be lucky")

    split_bill = bill_total / (num_of_friends)
    round_bill = round(split_bill, 2)

    for val in friend_dictionary:
        friend_dictionary[val] += round_bill

    print()

    print(friend_dictionary)







