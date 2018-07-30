#the game begins with a 0 score.
user_score = 0

#simon outputs a sequence of 10 characters. We will use 4 for now.
#user must repeat the sequence.
simon_pattern = 'RRGBRYYBGY'
user_pattern =    'RRGBBRYBGY'
#create a for loop that compares the two strings.

for i in range(len(simon_pattern)):
    if(user_pattern[i] == simon_pattern[i]):
        user_score += 1
    else:
        break
        
#for each match, add 1 pt to the user_score.

#if a mismatch, the game ends
