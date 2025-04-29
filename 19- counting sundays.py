startYear = 1900

totalSundays = 0
dayOfWeek = 0
# days of week are 0 for Monday and 6 for Sunday
def Month(daysOfTheMonth, startingDay):
    global totalSundays

    for dayOfmonth in range(1,daysOfTheMonth+1):
        if dayOfmonth == 1 and startingDay == 6:
             totalSundays += 1
             print(f"found a Sunday!")
        startingDay +=1
        if startingDay >6:
            startingDay = 0

    return startingDay

def year(startYear, startingDay):

    months = {
        0: 31, #Jan
        2: 31, #Mar
        3: 30, #apr
        4: 31, #may
        5: 30, #jun
        6: 31, #jul
        7: 31, #aug
        8: 30, #sep
        9: 31, #oct
        10: 30, #nov
        11: 31 #dec
    }

    for month in range(12):
        days = 0
        if month != 1:
            days = months[month]
        else:                           #work out number of days to iterate.
            if startYear % 100 == 0:
                if startYear % 400 == 0: # for a century year
                    days = 29
                else:
                    days = 28
            else:
                if startYear %4 == 0: #for a normal year
                    days = 29
                else:
                    days = 28
        print(f"\t{month}:")

        startingDay = Month(days, startingDay)

    return startingDay

while startYear < 2001:
    print(f"{startYear}:")
    dayOfWeek = year(startYear,dayOfWeek)

    input(f"In {startYear}, there were {totalSundays} Sundays on  the first day of the month.")
    startYear += 1
print(f"That makes {totalSundays} in total.")


