chicken = 10.35
fish = 12.40
veggie = 8.15
deliveryFee = 2.50

#input
numChicken = int(input())
numFish = int(input())
numVeggie = int(input())

priceChicken = chicken * numChicken
priceFish = fish * numFish
priceVeg = veggie * numVeggie

totalMenusPrice = priceChicken + priceFish + priceVeg
desert = 0.20 * totalMenusPrice

totalDeliveryFood = totalMenusPrice + desert + deliveryFee
print(totalDeliveryFood)