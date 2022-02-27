import re

from numpy import full

def add_time(start, duration, start_day = None):
    # dividing start string into a list of lists that holds hours and minutes 
    # as a list at index 0 and AM or PM in the list at index 1
    full_divided_time = []
    time_divided = start.split()[0].split(":")
    full_divided_time.append(time_divided)
    am_pm = start.split()[1]
    full_divided_time.append(am_pm)
    # dividing duration into a list that holds hours and minutes
    divided_duration = duration.split(":")
    new_time = []
    new_am_pm = ""
    next_day_string = ""
    num_days_later = 0
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    end_day = ""
    # adding extra hour and subtracting 60 minutes from
    # minutes count if minutes go over 60 
    # appending new hours and minutes to new_time list
    if int(full_divided_time[0][1]) + int(divided_duration[1]) >= 60:
        new_hours = int(full_divided_time[0][0]) + int(divided_duration[0]) + 1
        new_time.append(new_hours)
        new_minutes = int(full_divided_time[0][1]) + int(divided_duration[1]) - 60
        new_time.append(new_minutes)
    else:
        new_hours = int(full_divided_time[0][0]) + int(divided_duration[0])
        new_time.append(new_hours)
        new_minutes = int(full_divided_time[0][1]) + int(divided_duration[1])
        new_time.append(new_minutes)
    # if statement for when initional time started with a 23, 
    # because works different than other cases
    if full_divided_time[0][0] == "12":
        if int(new_time[0]/12)%2 == 0:
            if full_divided_time[1] == "AM":
                new_am_pm = "PM"
            else:
                new_am_pm = "AM"
        else:
            new_am_pm = full_divided_time[1]
    # determining when to switch AM and PM
    elif new_time[0] > 11:
        if int(new_time[0]/12)%2 == 1:
            if full_divided_time[1] == "AM":
                new_am_pm = "PM"
            else:
                new_am_pm = "AM"
        else:
            new_am_pm = full_divided_time[1]
    else: 
        new_am_pm = full_divided_time[1]
    # determining how many days later it is. once again there is a separate 
    # if statement for when the initital time start at 12 because behaves differently
    if full_divided_time[0][0] == "12":
        if full_divided_time[1] == "AM" and new_time[0] >= 36:
            num_days_later = int((new_time[0]-12)/24)
        elif full_divided_time[1] == "PM" and new_time[0] >=24:
            num_days_later = int(new_time[0]/24)
    else:
        if full_divided_time[1] == "AM" and new_time[0] >= 24:
            num_days_later = int(new_time[0]/24)
        elif full_divided_time[1] == "PM" and new_time[0] >= 12:
            num_days_later = int((new_time[0]+12)/24)
    # creating number of days later string next_day_string
    if num_days_later == 1:
        next_day_string = " (next day)"
    elif num_days_later != 0:
        next_day_string = f" ({num_days_later} days later)"
    if start_day:
        new_day_index_nonadjusted = days_of_week.index(start_day.capitalize()) + num_days_later
        try:
            end_day = days_of_week[new_day_index_nonadjusted]
        except IndexError:
            end_day = days_of_week[new_day_index_nonadjusted - 7*(int(new_day_index_nonadjusted/7))]
    if new_time[0]%12 == 0:
        new_time[0] = new_time[0] - (new_time[0]-12)
    else:
        new_time[0] = new_time[0] - 12*int(new_time[0]/12)
    #creating new list new_time_as_strings with time values from new_time as strings   
    new_time_as_strings = list(map(str, new_time))
    # ensuring that minute values that are one digit long are proceeded by a "0"
    if len(new_time_as_strings[1]) == 1:
        new_time_as_strings[1] = "0" + new_time_as_strings[1]
    # assembling/formatting output string
    if start_day:
        new_time_string = ":".join(new_time_as_strings) + " " + new_am_pm + ", " + end_day + next_day_string
    else:
        new_time_string = ":".join(new_time_as_strings) + " " + new_am_pm + next_day_string
    return new_time_string

