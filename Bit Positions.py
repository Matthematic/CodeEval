import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = [x.strip() for x in test.split(',')]

    num_base2 = bin(int(test[0]))[2:]

    print (str((num_base2[-int(test[-1])] == num_base2[-int(test[-2])])).lower())
    
test_cases.close()
