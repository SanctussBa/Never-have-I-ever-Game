import random

score_p1 = 0
score_p2 = 0

score = score_p2 + score_p2


print("Welcome! This is NEVER HAVE I EVER game.\n")
print("Submit your answer if its true. Participants: P1 = Player 1 and P2 = Player 2")

while score < 5:
    file = open("never.txt").read().splitlines()
    line = random.choice(file)
    print(line)
    print("(1) Both\n (2) None\n (3) P1\n (4) P2")
    choice = input("Please choose the number >>>")
    if choice == "1":
        score_p1 += 1
        score_p2 += 1
        score += 2

    elif choice == "2":
        continue
    elif choice == "3":
        score_p1 += 1
        score += 1

    elif choice == "4":
        score_p2 +=1
        score += 1

    else:
        print("Please choose only answers 1; 2; 3 or 4")

print(f"You had {score} questions. Player 1 did {score_p1} positive answers \n and Player 2 {score_p2} answers")
if score_p1 > score_p2:
    print ( "Player 1 Won! Congratulations!")
elif score_p2 > score_p1:
    print("Player 2 Won! Congratulations!")
else:
    print("You both had same amount of positive answers.")

print("Goodbye")









