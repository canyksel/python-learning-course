import time
hour_value = 0
minute_value = 0
formatted_hour = 0
formatted_minute = 0
hour = 0
minute = 0
second = 0
is_alarm_set = False
answer = ''

class fcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CWHITE  = '\33[37m'

colors = [fcolors.HEADER, fcolors.OKBLUE, fcolors.OKCYAN, fcolors.OKGREEN, fcolors.WARNING, fcolors.FAIL]
current_color_index = 0

print(fcolors.OKBLUE +'Welcome to alarm app!' + fcolors.CWHITE)

print(len(colors))

while is_alarm_set is False:
    hour_value = int(input('Enter the hour (0-23):'))
    minute_value = int(input('Enter the minute (0-59):'))

    if (0 <= hour <= 23 ) and (0 <= minute_value <= 59) :
        is_alarm_set = True
        print('Please enter a valid hour and minute')
        continue

if hour_value >= 12:
    print('Your alarm set: {:02d}:{:02d} pm'.format(hour_value, minute_value))
else :
    print('Your alarm set: {:02d}:{:02d} am'.format(hour_value, minute_value))


while is_alarm_set is True:
    second += 1

    if second is 60:
        second = 0
        minute += 1

        if minute is 60:
            minute = 0
            hour += 1

            if hour is 24:
                hour = 0
    
    print(colors[second % len(colors)] + 'Current time: {:02d}:{:02d}:{:02d}'.format(hour, minute, second))
    time.sleep(1)

    if hour is hour_value and minute is minute_value:
        print(fcolors.OKGREEN + 'Your alarm ringing!')
        answer = input('Can you close the alarm or delay 1 minutes? (Confirm/Delay): ')
        if answer is 'Confirm' or answer.lower().startswith('c'):
            is_alarm_set = False
            quit()
        else :
            is_alarm_set = True
            hour_value = hour_value
            minute_value = minute_value + 1