pens = 5.80
markers = 7.20
cleaningAgent = 1.20 #per liter

numberOfPens = int(input())
numberOfMarkers = int(input())
litersCleaningAgent = int(input())
percentDiscount = int(input())

pricePens = pens * numberOfPens
priceMarkers = markers * numberOfMarkers
priceCleaningAgent = cleaningAgent * litersCleaningAgent
totalAmountMaterials = pricePens + priceMarkers + priceCleaningAgent
discount = percentDiscount / 100
priceAfterDiscount = totalAmountMaterials - (totalAmountMaterials * discount)
print(priceAfterDiscount)