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


count = fileSizes = 0
statusCodes = [200, 301, 400, 401, 403, 404, 405, 500]
statusCodesDict = {}
for code in statusCodes:
    statusCodesDict[code] = 0
p = r'^\d+\.\d+\.\d+\.\d+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'


def displayStatus():
    """Display the status every 10 times and/or KeyboardInterrupt(CTRL + C)"""
    print("File size: {:d}".format(fileSizes))
    for code in sorted(statusCodesDict):
        if statusCodesDict[code] > 0:
            print("{:d}: {:d}".format(code, statusCodesDict[code]))


def handler(signum, frame):
    """CTRL + C handler"""
    displayStatus()


signal.signal(signal.SIGINT, handler)

try:
    for line in sys.stdin:
        match = re.match(p, line)
        if not match:
            continue

        if int(match.group(1)) in statusCodesDict:
            statusCodesDict[int(match.group(1))] += 1
            fileSizes += int(match.group(2))
            count += 1

        if count == 10:
            displayStatus()
            count = 0

except KeyboardInterrupt:
    displayStatus()
    sys.exit(0)
