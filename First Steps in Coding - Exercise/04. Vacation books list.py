pagesInBook = int(input())
pagesPerHour = int(input())
daysToReadBook = int(input())

totalAmountToReadABook = pagesInBook / pagesPerHour
neededTimePerDay = round(totalAmountToReadABook / daysToReadBook)
print(neededTimePerDay)