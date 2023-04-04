# Terminal-Based Sleep Calculator
# Designed, built and crafted by SoroushMBabaei❤️!
# Enjoy!
# -------Libraries-------
from time import strftime,sleep
from os import system
import platform
# -----Main Functions----
def terminal_cleaner():
    os_name = platform.system()
    if os_name == "Windows":
        system("cls")
    elif os_name == "Linux" or os_name == "Darwin":
        system("clear")
def main():
    print("""\nHi,my name is Soroush and this is my program for making your sleep times algorithms
    so much better.Before we start,I want you to know some facts about your body:
    1:You need 15 minutes to fall a sleep and that will get considered in this app
    2:Every cycle of your sleeping process is a 90-minute cycle which means that 
    if you want to wake up with a better mood you should do it before the start of 
    next cycle!
    3:Cold shower and a cup of coffee will also give an extra feeling of awareness if you care about that.
    Now, without further ado, lets see what times you can wake up better than ever!""")
    sleep(2)
    input_time = input("Time:")
    present_time()
    user_time(input_time)
# --Calculators Functions--
def present_time():
    time = strftime("%H:%M")
    hour, minute = time.split(":")
    hour, minute = int(hour), int(minute)
    # Time needed to fall a sleep
    minute += 15
    if minute > 60:
        minute -= 60
    elif minute == 60:
        minute = 0
    else:
        minute = int(minute)
    # Cycles
    hour_to_minute = hour * 60
    sum_of_all = hour_to_minute + minute
    for i in range(6):
        sum_of_all += 90
        sleep_hour = sum_of_all//60
        if sleep_hour >= 24:
            sleep_hour -= 24
        sleep_minute = sum_of_all%60
        print(f"Best moments to wake up: {sleep_hour}:{sleep_minute}")
        print(30*"__")
    print("It's the best if you wake up at the last one!")
def user_time(time):
    hour, minute = time.split(":")
    hour, minute = int(hour), int(minute)
    # Time needed to fall a sleep
    minute += 15
    if minute > 60:
        minute -= 60
    elif minute == 60:
        minute = 0
    else:
        minute = int(minute)
    # Cycles
    hour_to_minute = hour * 60
    sum_of_all = hour_to_minute + minute
    for i in range(6):
        sum_of_all += 90
        sleep_hour = sum_of_all//60
        if sleep_hour >= 24:
            sleep_hour -= 24
        sleep_minute = sum_of_all%60
        print(f"Best moments to wake up: {sleep_hour}:{sleep_minute}")
        print(30*"__")
    print("It's the best if you wake up at the last one!")
# -------Execution-------
if __name__ == "__main__":
    terminal_cleaner()
    main()