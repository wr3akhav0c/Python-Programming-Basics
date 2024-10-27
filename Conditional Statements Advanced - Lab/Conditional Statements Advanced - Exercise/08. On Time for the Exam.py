# Input exam and arrival times
examHour = int(input())
examMin = int(input())
arrivalHour = int(input())
arrivalMinute = int(input())

# Convert both times to total minutes from the start of the day
examTotalMinutes = examHour * 60 + examMin
arrivalTotalMinutes = arrivalHour * 60 + arrivalMinute

# Calculate the time difference between arrival and exam time
timeDifference = arrivalTotalMinutes - examTotalMinutes

# Determine the status
if timeDifference > 0:
    print("Late")
    if timeDifference < 60:
        print(f"{timeDifference} minutes after the start")
    else:
        hours = timeDifference // 60
        minutes = timeDifference % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif -30 <= timeDifference <= 0:
    print("On time")
    if timeDifference < 0:
        print(f"{abs(timeDifference)} minutes before the start")
else:
    print("Early")
    if -60 < timeDifference:
        print(f"{abs(timeDifference)} minutes before the start")
    else:
        hours = abs(timeDifference) // 60
        minutes = abs(timeDifference) % 60
        print(f"{hours}:{minutes:02d} hours before the start")
