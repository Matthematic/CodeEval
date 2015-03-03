import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = [x.strip() for x in test.split(',')]
    n = int(test[-1])
    
    while n <= int(test[0]):
        n += int(test[-1])
        
    print (n)
    

test_cases.close()
