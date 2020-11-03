#Initialize all variables to 0
numberOfScores = 0
score = 0
total= 0
scoreCount = 0
average = 0.0

#Accept the number of scores to average
numberOfScores = int(input("Please enter the number of scores you want to average:"))


#Add a loop to make this code repeat until scorecount=numberOfScores
while (scoreCount < numberOfScores):
    score = int(input("Please enter a score: "))
    total= total + score
    scoreCount = scoreCount + 1

#To turn into a string, print average.
average= total / numberOfScores
print("The average of the test score is: " +str(average))

