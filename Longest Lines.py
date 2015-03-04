import sys
test_cases = open(sys.argv[1], 'r')
N = 0
arr = []
for test in test_cases:
  if N == 0:
    N = int(test)
    continue

  arr.append(str(test))
  
arr.sort(key = len)  
for i in range(1, N+1):
  print (arr[-i])
  
  

test_cases.close()
