import schedule
import time
import datetime
def display():
    print("jay ganesh...",datetime.datetime.now())

def main():
    print("autometion script started")
    schedule.every(1).minute.do(display)


if __name__=="__main__":
    main()