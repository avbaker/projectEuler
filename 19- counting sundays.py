startYear = 1901

totalSundays = 0
dayOfWeek = 0
# days of week are 0 for Monday and 6 for Sunday
days = {0 : "Monday",
1: "Tuesday",
2: "Wednesday",
3:"Thursday",
4: "Friday",
5: "Saturday",
6: "Sunday"}
def Month(daysOfTheMonth, startingDay):
    global totalSundays
    global days
    print()

    for dayOfmonth in range(1,daysOfTheMonth+1):
        print(f"{days[startingDay]} {dayOfmonth}")
        #print(f"{dayOfmonth}/{daysOfTheMonth}")
        if dayOfmonth == 1 and startingDay == 6:
             totalSundays += 1
             print(f"found a Sunday! total = {totalSundays}")
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
                print("It's a century", end="")
                if startYear % 400 == 0: # for a century year
                    days = 29
                    print(" leap year!")
                else:
                    days = 28
                    print("!")
            else:
                if startYear %4 == 0: #for a normal year
                    days = 29
                    print("It's a normal leap year!")
                else:
                    days = 28
        print(f"\t{month}:")

        startingDay = Month(days, startingDay)

    return startingDay

while startYear < 2001:
    print(f"{startYear}:")
    dayOfWeek = year(startYear,dayOfWeek)

    input(f"by the end of {startYear}, there were {totalSundays} Sundays on the first day of the month.")
    startYear += 1
print(f"That makes {totalSundays} in total.")


