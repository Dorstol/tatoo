import datetime
from time import sleep


def main():
    print("Hello world")
    while True:
        print(datetime.datetime.now())
        sleep(1)


if __name__ == "__main__":
    main()
