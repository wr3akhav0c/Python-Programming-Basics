nylon = 1.50
paint = 14.50
razreditel = 5.00

#input
neededNylon = int(input())
neededPaint = int(input())
neededRazdelitel = int(input())
hoursWork = int(input())

#calculations
priceNylon = (neededNylon + 2) * nylon
pricePaint = (neededPaint + (0.10 * neededPaint)) * paint
priceRazdelitel = neededRazdelitel * razreditel
bags = 0.40
totalAmountMaterials = priceNylon + pricePaint + priceRazdelitel + bags

priceWorkers = (totalAmountMaterials * 0.30) * hoursWork
endResult = totalAmountMaterials + priceWorkers

print(endResult)