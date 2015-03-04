import sys

#break the array into key-sized chunks, and then reverse each chunk
def parse(arr, key):
    if key < 1: key = 1  #key cannot be < 1
    result = [arr[i:i + key] for i in range(0, len(arr), key)] 
    for tuple in result:
      if len(tuple) == key: tuple.reverse()

    return result

#this parses the test string and pushes all numbers into an array, unsorted
def get_array(arr):
  global save
  element = ""

  for character in range(0, len(test)-1): #ignore the key and last comma, step twice to avoid other commas
    if test[character].isdigit(): #if our next char is a digit, we are not done with this element yet
        element += test[character]
    else: #were done, so lets append it and reset
      arr.append(element)
      element = ""


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = str.strip(str(test)) #strip any whitespace
  key = int(test[-1]) #get key from last number
  arr = []

  get_array(arr) #get the numbers
  x = parse(arr, key) #parse it


  #outputting result without commas. Used stdout.write because print includes spaces 
  for chunk in range(len(x)):
    for element in range(len(x[chunk])):

      if element == (len(x[chunk])-1) and chunk == (len(x)-1): #if its the last character, dont add a comma on the end
         sys.stdout.write (str(x[chunk][element]))
      else:
        sys.stdout.write ((str(x[chunk][element]) + ','))
        
        
  print ('\n')

test_cases.close()