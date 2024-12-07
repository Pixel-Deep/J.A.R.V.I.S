from datetime import datetime

def get_current_time():
 
    return datetime.now().strftime('%I:%M %p')  # %I for 12-hour format, %p for AM/PM

def get_greeting():

    current_time = get_current_time()
    # Split the time string into hour, minute, and period (AM/PM)
    time_parts = current_time.split(" ")
    hour, minute = map(int, time_parts[0].split(":"))
    period = time_parts[1]

    # Adjust hour based on AM/PM
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    # Determine the greeting based on the hour
    if 5 <= hour < 12:
        return "Good Morning Sir"
    elif 12 <= hour < 18:
        return "Good Afternoon Sir"
    else:
        return "Good Evening Sir"



