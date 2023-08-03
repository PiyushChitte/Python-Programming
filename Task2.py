# Task Schedular
# schedule a program to run after every 1 minute on console

import schedule
import time
import datetime

def fun():
    print("Time is : ",datetime.datetime.now())

def main():
    print("Inside task schedular")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).minute.do(fun)

    while(True):         # unconditional infinite loop
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
