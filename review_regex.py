import re

pattern = re.compile(r'\d+')
m = pattern.match('abc123swe',3,6)
print(m.group())

pattern2 = re.compile(r'([a-z]+) ([a-z]+)',re.I)
m2 = pattern2.match('Hello World hello python')
for i in range(3):
    print(m2.group(i))
    print(m2.span(i))#下标