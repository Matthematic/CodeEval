import sys


class FizzBuzz():
    def __init__(self, A, B, N):
        self.A = int(A)
        self.B = int(B)
        self.N = int(N)
        sys.stdout.write('\n')


    def play(self):
        for i in range(1, self.N+1):
            if i % self.A == 0 and i % self.B == 0:
                sys.stdout.write('FB')
            elif i % self.A == 0:
                sys.stdout.write('F')
            elif i % self.B == 0:
                sys.stdout.write('B')
            else:
                sys.stdout.write(str(i))


            if i < self.N+1:
               sys.stdout.write(' ')








test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = [x.strip() for x in test.split(' ')]
    A = test[0]
    B = test[1]
    N = test[-1]
    test = FizzBuzz(A, B, N).play()

test_cases.close()
