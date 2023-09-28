import sys
from datetime import datetime
input = sys.stdin.readline

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)