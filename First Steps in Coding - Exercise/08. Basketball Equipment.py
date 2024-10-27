taxYear = int(input())

shoes = taxYear - (taxYear * 0.40)
clothes = shoes - (shoes * 0.20)
ball = clothes * 0.25
accessories = ball * 0.20

total = taxYear + shoes + clothes + ball + accessories
print(total)