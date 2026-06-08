#print any IP that gets a 404 status code

"""
The purpose of this script is to return 404 source IP if its found
"""


#libraries utilized
import re

def main():
    LOG_FILE = r"/Users/raygpeckham/IT-102-Spring-2026/start/CH07/access.log"
    with open(LOG_FILE, "r") as f:
        for line in f:
            #status code which is right after request and first nuymbers
            ip = line.split()[0]
            match = re.search(r'" 404 ', line)
            if match:
                print(f"{ip}")


if __name__ == "__main__":
    main()

