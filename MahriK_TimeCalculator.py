# Write a function named add_time that takes in two required parameters and one start_day parameter:

# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (start_day) a starting day of the week, case insensitive
# The function should add the duration time to the start time and return the result.

# If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

# If the function is given the start_day starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

# Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)
# Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

def add_time(start_time, duration_time, start_day=None):
    print(start_day)  # Testing if an start_day parameter was appointed corrected

    # Defining the lists containing time value and a term (AM or PM)  
    start_value = start_time.split(" ")[0]  # Hour and minute
    start_term = start_time.split(" ")[1]  # Term AM or PM
    # Extracting the hour and minute values  
    start_hour = start_value.split(":")[0]
    start_minute = start_value.split(":")[1]

    # Converting string to integer  
    start_hour = int(start_hour)
    start_minute = int(start_minute)

    # Extracting duration hour value and duration minute value.  
    duration_hour=duration_time.split(":")[0]
    duration_minute=duration_time.split(":")[1]
    # Converting strings to integers
    duration_hour=int(duration_hour)
    duration_minute=int(duration_minute)

    # Introducing the 24 hour format
    if start_term.upper() == "PM":  # The  text is case insensitive
        start_hour = start_hour + 12

    # Calculating final hour and minute
    final_hour = start_hour + duration_hour 
    final_minute = start_minute + duration_minute 

    # Converting numerical minute value to time value
    if final_minute >= 60:
        final_hour += 1
        final_minute = final_minute - 60
        print("This is line 67 check. The final minute is ", final_minute)
    
    # Calculating if the duration hour results in the next day or n days using remainder from division
    ndays=final_hour//24  # Here the ndays variable stores  how many days have passed
    remainder_hour=final_hour%24  # Here remainder_hour is  the actual hour
    print("This is line 72 check. The n days and the actual hour is : ", ndays, " days later and the current hour is ", remainder_hour)

    # Defining the term (AM or PM)
    if remainder_hour >= 12:
        final_term = "PM"
        if remainder_hour > 12:
            remainder_hour = remainder_hour - 12
        print("This is line 78 check. The hour is: ", remainder_hour, " ", final_term)
    else:
        final_term = "AM"
        print("This is line 81 check. The hour is: ",  remainder_hour, " ", final_term)
        if remainder_hour == 0:
            remainder_hour =  remainder_hour + 12
    print("This is line 82 check. The hour is: ", remainder_hour, " ", final_term)

    # Defining if the final hour is next day or n days later
    if ndays ==  1:
        day = "(next day)"
        print("This is line 87 check. The day is : ", day)
    elif  ndays > 1:
        day = "(%d days later)"%ndays
        print("This is line 190 check. The day is : ", day, "days later")

    # Calculating what day it is. The list is used as a reference and index of the list is used to calculate the current day of the week.
    week=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if start_day is not None:  # Only runs when the optional variable startt_day exists  
        for day_week in week:
            if start_day.lower() == day_week.lower():
                day_number = week.index(day_week) 
                total_day = day_number + ndays

    #  Utilizing the if statement to make sure the  week of the day is identified correctly even when the total_day value is higher than 7, meaning that the duration hour value was higher than 168 hr (aka 7 days)    
    if start_day is not None:
        if total_day < 7:
            start_day = week[total_day]
        else:
            start_day = week[total_day%7]
        print("This is line  146. The day of the week is: ", start_day)

    # Styling the minute value when the value is smaller than 10 minutes since the format requires there to be a 0 before the value.
    if final_minute < 10:
        final_minute = "0"+str(final_minute)

    comma = ","    

    print("Returns : %d:%s %s%s %s %s"%(remainder_hour, final_minute, final_term,comma if start_day else "", start_day if start_day else "", day if ndays >= 1 else "" ))
    print("The above checkled line 111")

add_time("11:43 PM", "24:20","tueSday")

# How to get rid of the comma on line 115 that goes into the print statement 
# How to get rid of the extra space when printing next day or n days later when there is no start_day week day input
# Automating step on line 83 with time value being equal to 0
