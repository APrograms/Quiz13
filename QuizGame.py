print("Welcome to the computer quiz!")

playing = input("Do you want to play now? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is known as temporary memory? ")
if answer.lower() == "ram":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

answer = input("What does ALU stand for in the context of computers? ")
if answer.lower() == "arithmetic logic unit":
        print('Correct')
        score += 1
else:
        print("Incorrect!")

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
            print('Correct')
            score += 1
else:
            print("Incorrect!")

print("You got " + str(score)+" questions correct!")
print("You got " + str((score / 3) * 100) + "%.")
