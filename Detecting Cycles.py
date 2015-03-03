import sys, re

'''this is not my solution, but it was so cool I just had to use it.'''
            
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    
    regex = re.compile(r'(.+ .+)( \1)+')
    match = regex.search(test)
    x = match.group(1)
    final = regex.search(x)
    if final is not None:
        result = final.group(1).split()
        if result.count(result[0]) == len(result):
            print result[0]
        else:
            print final.group(1)
    else:
        print match.group(1)

test_cases.close()

