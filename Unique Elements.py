
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = [x.strip() for x in test.split(',')]
    result = []

    for element in test:
        if element not in result:
            result.append(element)

    print (','.join(result))

test_cases.close()
