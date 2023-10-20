def timeConversion(s):
    # Write your code here
    time, period = time_12hr.split()
    hh, mm, ss = map(int, time.split(':'))

    if period == 'PM' and hh != 12:
        hh += 12
    elif period == 'AM' and hh == 12:
        hh = 0

    # Format the time in 24-hour format
    military_time = f'{hh:02d}:{mm:02d}:{ss:02d}'
    
    return military_time

# Example usage:
time_12hr = "08:45:23 PM"
military_time = timeConversion(time_12hr)
print(military_time)