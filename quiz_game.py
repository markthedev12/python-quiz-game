print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play")
score = 0
answer = input("What does CPU stand for? ")

if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")

if answer == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")

if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print ("You Got" + str(score) + " questions correct!")
percentage = (score / 3) * 100
print(f"You got {percentage}%.")
