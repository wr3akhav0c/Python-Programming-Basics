import math

serialName = input()
durationEp = int(input())
durationBreak = int(input())

lunchTime = durationBreak / 8
chillTime = durationBreak / 4
neededTime = durationEp + lunchTime + chillTime
timeLeft = durationBreak - neededTime

if timeLeft >= 0:
    print(f"You have enough time to watch {serialName} and left with {math.ceil(timeLeft)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serialName}, you need {math.ceil(abs(timeLeft))} more minutes.")