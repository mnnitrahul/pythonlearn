import sys

__author__ = 'rahul.ka'
def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters and Returns string."""
    return "\n".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    myParams = {"server":"mpilgrim", \
                "database":"master", \
                "uid":"sa", \
                "pwd":"secret" \
                }
    print buildConnectionString(myParams)
    print buildConnectionString.__doc__
    print sys.path