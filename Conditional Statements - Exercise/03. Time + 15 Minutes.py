inputHour = int(input())
inputMinute = int(input())

newMinute = inputMinute + 15

if newMinute >= 60:
    newMinute -= 60
    inputHour += 1

if inputHour >= 24:
    inputHour = 0

print(f"{inputHour}:{newMinute:02d}")