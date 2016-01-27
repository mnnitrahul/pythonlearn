import re

__author__ = 'rahul.ka'
s = '100 BROAD'

print re.sub('ROAD$', 'RD.', s)
print  re.sub('\\bROAD$', 'RD.', s)

print  re.sub(r'\bROAD$', 'RD.', s)

s = '100 BROAD ROAD APT. 3'
print  re.sub(r'\bROAD$', 'RD.', s)
print  re.sub(r'\bROAD\b', 'RD.', s)
