import sys

def make_row(row):
    new = []
    for i in xrange(len(row)):
        new.append(row[i-1]+row[i] if (i-1) >= 0 else row[i])
    #new.append(1)
    return new + [1]
    
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    depth = int(test)
    base = 1
    triangle = [[base]]
    for i in xrange(depth-1):
        triangle.append(make_row(triangle[i]))

    for i in xrange(len(triangle)):
        for num in triangle[i]:
            print num,

    print 
    
test_cases.close()
