__author__ = 'rahul.ka'

collapse = 1
processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
s = "this is\na\ttest"
print processFunc(s)
collapse = 0
processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
print processFunc(s)