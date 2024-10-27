waterResistanceDistance = 15
waterResistanceDelay = 12.5

recordInSec = float(input())
distanceInM = float(input())
timeInSec = float(input())

delayInSec = (distanceInM // waterResistanceDistance) * waterResistanceDelay
swimmingRecord = (timeInSec * distanceInM) + delayInSec

if swimmingRecord < recordInSec:
    print(f"Yes, he succeeded! The new world record is {swimmingRecord:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(recordInSec - swimmingRecord):.2f} seconds slower.")