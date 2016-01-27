__author__ = 'rahul.ka'
if __name__ == "__main__":
    dictionary = {
        'server' : 'localhost',
        "database" : "master",
        'host' : 3,
        1 : 'test',
        '1' : 'test2'
    }

print dictionary['database']
dictionary['database'] = 'local'
print dictionary['database']
print dictionary
print dictionary['host']
print dictionary[1]
print dictionary['1']
del dictionary['1']
print dictionary

if __name__ == "__main__":
    list = ["abcd", 1, 'efgh']


print "complete list ", list
print "printing list from last ", list[-1]
print "sublist ", list[:2]
list.extend(list[:])
print "appending list ", list
print list.index('abcd')
list.remove("abcd")
list.remove("efgh")
print list
list += ['4', '5']
print "same as extend ", list
list *= 2
print "repearting same  ", list

v = ('a', 'b', 'c', 'd')
(x, y, z, z2) = v
print "x = %s y = %s and z = %s  " % (x, y, z)


list2 = [1, 9, 8, 4]
list2 = [elem*2 for elem in list2]
print list2
for it in list2:
    print it


