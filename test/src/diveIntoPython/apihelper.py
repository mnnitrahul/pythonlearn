import string
import helloworld
import ifcondition

__author__ = 'rahul.ka'
def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    print methodList
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                 (method.ljust(spacing),
                  processFunc(str(getattr(object, method).__doc__)))
                 for method in methodList])
li = []
info(helloworld)
print "dir of ifcondition is ", dir(ifcondition)
print "type of hello world is ", type(helloworld)
print callable(string.join)
print callable(string.join.__doc__)
print string.join(['a', 'b', 'c'])
print getattr(li, "pop")