
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = str.strip(str(test))
    letter = str(test[-1])
    found = False

    if test != '':
        for n in range(len(test)-2, -1, -1):
          if (test[n] == letter):
              print (n)
              found = True
              break

        if not found:
            print (-1)
        
test_cases.close()
