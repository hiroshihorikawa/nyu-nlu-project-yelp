import json
import sys
from pprint import pprint

count = 0
for line in sys.stdin:
 count+=1
 if count==20:
  break
 lines = line.strip()
 lines2 = lines.split('text":"')[1]
 lines3 = lines2.split('"')[0]
 print(lines3)
