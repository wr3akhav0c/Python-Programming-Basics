videoCard = 250
cpuPercent = 0.35
ramPercent = 0.10
discountPercent = 0.15

budget = float(input())
numVideoCards = int(input())
numCPUs = int(input())
numRams = int(input())

sumVideoCards = numVideoCards * videoCard
sumPriceCPU = numCPUs * (sumVideoCards * cpuPercent)
sumRam = numRams * (sumVideoCards * ramPercent)

totalSum = sumVideoCards + sumPriceCPU + sumRam

if numVideoCards > numCPUs:
    totalSum -= (totalSum * discountPercent)

if budget >= totalSum:
    print(f"You have {budget - totalSum:.2f} leva left!")
else:
    print(f"Not enough money! You need {totalSum - budget:.2f} leva more!")