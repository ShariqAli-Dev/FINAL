days_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_each_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def valid_date(year, month, day):
    if year % 4 == 0:
        if day < days_each_month_leap[month - 1]:
            return True
    elif day < days_each_month[month -1]:
        return True
    else:
        return False

def input_date():
    print("Please enter a date:\n")
    
    while True:
        year = int(input("   Year: "))
        month = int(input("   Month: "))
        day = int(input("   Day: "))

        if valid_date(year, month, day):
            print("Thank You!")
            break
        print("\n This date does not exist. Please enter a valid date")

input_date()