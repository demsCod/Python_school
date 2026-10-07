import time
from datetime import datetime


def main():
    timestamp = time.time()

    print(f"Seconds since January 1, 1970: {timestamp:,.4f} "
          f"or {timestamp:.2e} in scientific notation")
    print(datetime.now().strftime("%b %d %Y"))


if __name__ == "__main__":
    main()
