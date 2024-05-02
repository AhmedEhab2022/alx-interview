#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
(if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:

Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""
import re
import sys
import signal


flag = True
count = fileSizes = 0
statusCodes = [200, 301, 400, 401, 403, 404, 405, 500]
statusCodesDict = {}
constStr = "\"GET /projects/260 HTTP/1.1\""
pattern = r"^\d+\.\d+\.\d+\.\d+ - \[.*\]" + re.escape(constStr)
pattern += r"\d+ \d+$"

for line in sys.stdin:
    if not re.match(pattern, line):
        continue

    if count == 10:
        count = 0
        sys.exit()

    if int(line.split()[len(line) - 2]) in statusCodes:
        statusCodesDict[line.split()[len(line) - 2]] += 1
    else:
        flag = False

    fileSizes += int(line.split()[len(line) - 1])
    count += 1


def handler(signum, frame):
    """CTRL + C handler"""
    print("File size: {:d}".format(fileSizes))
    if flag:
        for code in statusCodes:
            print("{:d}: {:d}".format(code, statusCodesDict[code]))

    fileSizes = 0
    statusCodesDict = {}


signal.signal(signal.SIGINT, handler)
