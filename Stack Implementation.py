def push(value):
    global result
    result.append(value)

def pop():
    global result
    result = result[1:]

import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    result = []
    popped = False
    test = test.split(' ')
    
    for num in test:
        push(num.strip())

    result.reverse()
    
    for integer in result:
        if not popped:
            sys.stdout.write(str(result[0]) + " ")
        pop()
        popped = not popped


    print ('\n')

test_cases.close()
