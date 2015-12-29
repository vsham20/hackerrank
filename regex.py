__author__ = 'vaishali'
import re
for i in range(int(raw_input())):
    try:
        s = raw_input()
        re.compile(s)
    except:
        print False
        continue
    print True  