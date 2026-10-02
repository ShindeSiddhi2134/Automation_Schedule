import schedule
import time
import datetime
def display():
    print("jay ganesh...",datetime.datetime.now())

def main():
    print("automation script is started")
    schedule.every(10).seconds.do(display)
    while True:
        schedule.run_pending()
        time.sleep(1)

    print("end of automation script")

if __name__=="__main__":
    main()