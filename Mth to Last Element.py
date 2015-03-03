
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = [x.strip() for x in test.split()]
    num = test[-1]
    test = test[:len(test)-1]
    
    if not (int(num) > len(test)):
        print (test[-int(num)])
    
test_cases.close()
