# Import library
import time
import keyboard

# Function to choose a format 
def choose_a_format():
    while True:
        try:
            format = int(input("Choose a format 24h or 12h\n'24' or '12' : "))
            if format == 24:
                print("You chose 24h format")
                return format
            elif format == 12:
                print("You chose 12h format")
                return format
        except ValueError:
            print("Please enter valid numeric values...")

# Function Origin set/local
def origin():
     while True:
        try:
            choice = input("\nEnter '1' to set time or '2' for local time: ")
            if choice == '1':
                print("You chose to set a time by yourself")
                return ask_time()
            elif choice == '2':
                print("You chose to get local time")
                hours = int(time.strftime('%H'))
                minutes = int(time.strftime('%M'))
                seconds = int(time.strftime('%S'))
                t_origin = hours, minutes, seconds
                return t_origin
            else:
                print("Please enter '1' or '2'.")
        except ValueError:
            print("Please enter valid numeric values...")

# Function to set the time
def ask_time():
    while True:
        print("\nSet the time...")
        hours = input("Enter a hour (0-23): ")
        minutes = input("Enter a minute (0-59): ")
        try:
            hours = int(hours)
            minutes = int(minutes)
        except ValueError:
            print("Please enter valid numeric values...")
            continue
        if 0 <= hours < 24 and 0 <= minutes < 60:
            seconds = 0
            t_origin = (hours, minutes, seconds)
            return t_origin
        else:
            print("Hours must be between 0-23 and minutes between 0-59.")

# Function to ask to set an alarm
def set_alarm():
    while True:
        setalarm = input("\nDo you want to set an alarm?\n'y' for yes or 'n' for no : ")
        if setalarm == 'y':
            print("\nSet an alarm...")
            h = input("Enter a hour (0-23): ")
            m = input("Enter a minute (0-59): ")
            try:
                h = int(h)
                m = int(m)
            except ValueError:
                print("Please enter valid numeric values...")
                continue
            if 0 <= h < 24 and 0 <= m < 60:
                s = int(0)
                alarm = (h, m, s)
                return alarm
        elif setalarm == 'n':
            print("You chose to don't set an alarm")
            alarm = (None, None, None)
            return alarm

# Function afficher_heure
def afficher_heure(t_origin,format):
    hours, minutes, seconds = t_origin
    if format == 12:
        if hours > 12:
            meridiem = 'PM'
            hours -= 12
        elif hours < 12:
            meridiem = 'AM'
        elif hours == 12:
            meridiem = 'PM'
    elif format == 24:
        meridiem = ''
    print(f"\r{(hours):02}:{(minutes):02}:{(seconds):02} {meridiem}", end="")
    if meridiem == 'PM'and hours != 12:
        hours +=12

# Function to run clock
def running(format, t_origin, alarm):
    print("\nHold 'ESC' to return to the menu")
    while True:
        hours, minutes, seconds = t_origin
        alarm_h, alarm_min, alarm_sec = alarm
        afficher_heure(t_origin, format)
        
        time.sleep(1)
        seconds += 1

        if seconds == 60:
            seconds = 0
            minutes += 1
        elif minutes == 60:
            minutes = 0
            hours += 1
        elif hours == 24:
            hours = 0
        
        t_origin = (hours, minutes, seconds)
    
        if (hours + minutes + seconds) % 31 == 0:
            time.sleep(5)

        elif alarm_h==hours and alarm_min == minutes and alarm_sec== seconds:
            print("\n\n DING DING !!!\n")

        elif keyboard.is_pressed('esc'):
            print("\n\n")
            break

# Function Menu
def menu():
    while True:
        print("\n--- MENU ---")
        running(choose_a_format(),origin(),set_alarm())

# Program execute
if __name__ == "__main__":
    menu()