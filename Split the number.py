import sys


def find_operands(num, pattern, operators):
    num = str(num)
    for i in xrange(len(pattern)):
        if pattern[i] in operators:
            #print num[:i],
            for x in xrange(len(num[i:])):  # remove leading zeros so eval() doesnt fail
                if num[i:][x] != '0':
                    new_num = num[i:][x:]
                    break
                else:
                    new_num = '0'

            return num[:i] + pattern[i] + new_num
            
operators = ('+', '-')

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    parts = test.split()
    num = parts[0]
    pattern = parts[1]

    expression = find_operands(num, pattern, operators)

    print eval(expression)

test_cases.close()