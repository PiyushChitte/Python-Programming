# Task Schedular
# schedule a program to run after every 1 minute on console

import schedule
import time
import datetime

def Task_Minute():
    print("Task based on minutes gets scheduled at : ",datetime.datetime.now())

def Task_Hour():
    print("Task based on hour gets scheduled at : ",datetime.datetime.now())

def Task_Day():
    print("Task based on day gets scheduled at : ",datetime.datetime.now())


def main():
    print("Inside task schedular")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).minute.do(Task_Minute)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every().saturday.at("18:00").do(Task_Day)

    while(True):         # unconditional infinite loop
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
