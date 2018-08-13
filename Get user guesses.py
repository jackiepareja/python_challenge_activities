#Write a loop to populate user guesses with num_guesses integers.
#Read integers using int(input()).
num_guesses = 3
user_guesses = []

guess = 0
print()

while guess < num_guesses:
    num = int(input())
    user_guesses.append(num)
    guess += 1

print(user_guesses)







